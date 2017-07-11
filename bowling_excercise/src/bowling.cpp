#include "bowling.h"
#include <vector>
#include <iostream>
#include <algorithm>
//#include <sstream>
//#include <regex>

using namespace std;


bool removeme()
{
	return true;
}

int getscore()
{
	vector<string> input;
	vector<string> errormessages;
	return getscore(input, errormessages);
}

void printmessage(vector<string>& errormessages, string message)
{
	errormessages.push_back(message);
	cout<<message;
}

int calculate_scores(vector<short> &result)
{
	bool open_frame = false;
	int framecount  = 0;
	int total = 0;
	for(auto value = result.begin(); framecount< BOWLING_MAX_FRAMES; value++)
	{
		if(open_frame) // frame is currently open, close it
		{
			framecount++;
			open_frame = false;
			if((*value) ==BOWLING_MIN_PINS) 
				total+= 2 * BOWLING_MAX_PINS - *(value+1);
			else
				total+= BOWLING_MAX_PINS - *value;
		}
		else if((*value)==BOWLING_MIN_PINS)
		{
			framecount++;
			if(*(value+1) ==BOWLING_MIN_PINS)
				total += 3 * BOWLING_MAX_PINS - *(value+2);
			else 
				total += 2 * BOWLING_MAX_PINS - *(value+2);
			
		}
		else 
		{
			open_frame = true;
		}
		
	}
	//cout<<"\n\n\n\n\n";
	//for_each(result.begin(),result.end(),[](short s){cout<<s;});
	//cout<<"\n\n\n\n\n";
	//cout<<"\n\n\n\n\ntotal="<<total<<"\n\n\n\n";
	return total;
}

int getscore(vector<string> input, vector<string>& errormesages)
{
	//
	// returns: total pins
	//          -1 if interrupted by user
	// 

	const int nonumber = 99999;

	bool reading_fromuser = true;
	if(input.size())
		reading_fromuser = false;

	vector<short> pinss;
	int framecounts = 0;
	//bool wait_snd_roll = false; // waiting second roll
	//bool wait_trd_roll = false; // waiting third  roll
	bool quit = false;
	bool finished = false;
	bool open_frame = false;
	int open_remaining = 0;
	//bool waitingstrike = false;
	//bool waitingspare = false;
	int  extrarolls = 0;
	

	// input and validate data
	while(!quit && !finished)
	{
		int pins = nonumber;
		int maxpins = open_frame ?  open_remaining : BOWLING_MAX_PINS;
		
		// ############################################
		// get pins
		// ############################################
		if(!reading_fromuser)
		{
			if(input.size())
			{
				pins = getnpins(input.front());					
				input.erase(input.begin(),input.begin()+1);
			}
			//else break; // ============================== REMOVE ME ==========================
		}
		else
		{
			string pins_str;
			cout<<"Enter number of remaining pins in this roll: from " << BOWLING_MIN_PINS << " to " << maxpins << " (or 'q' to exit the program) and press 'enter': "<< endl;		  
			cin>> pins_str;
			pins = getnpins(pins_str);
		}

		// maximum allowed pins for this roll
		//cout<<"open_frame="<<open_frame<<endl;
		//cout<<"open_remaining="<<open_remaining<<endl;
		//cout<<"maxpins="<<maxpins<<endl;

		// ############################################
		// check pins
		// ############################################
		if(pins == -1)
		{
			quit = true;  // user exit code
		}
		else if(pins == -2 || pins == -3)
		{
			//errormesages.push_back(BOWLING_WRONG_INPUT_FORMAT);
			//errormesages.push_back("dfd");
			//cout<<"wrong input format"
			printmessage(errormesages,BOWLING_WRONG_INPUT_FORMAT);
			printmessage(errormesages,"\n");

			printmessage(errormesages,BOWLING_WRONG_INPUT_INDICATE);
			printmessage(errormesages,to_string(BOWLING_MIN_PINS));
			printmessage(errormesages,BOWLING_WRONG_INPUT_INDICATE_2);
			printmessage(errormesages,to_string(maxpins));
			printmessage(errormesages,"\n");
			// ... doing nothing at this iteration
			
		}
		// non-negative pins
		else if(pins > maxpins)
		{
			printmessage(errormesages,BOWLING_WRONG_INPUT_NUMBER);
			printmessage(errormesages,"\n");

			printmessage(errormesages,BOWLING_WRONG_INPUT_INDICATE);
			printmessage(errormesages,to_string(BOWLING_MIN_PINS));
			printmessage(errormesages,BOWLING_WRONG_INPUT_INDICATE_2);
			printmessage(errormesages,to_string(maxpins));
			printmessage(errormesages,"\n");
			// .. doing nothing at this iteration
		}
		// ############################################
		// pins are okay, incrementing
		// ############################################
		else
		{
			// save pins
			pinss.push_back(pins);
		
			// open, close frame
			if(framecounts < BOWLING_MAX_FRAMES )
			{
				if(open_frame) // frame is currently open - close it
				{
					open_frame = false;
					framecounts++;
					if(framecounts == BOWLING_MAX_FRAMES && pins==BOWLING_MIN_PINS) extrarolls++;
					//if(pins==BOWLING_MIN_PINS) waitingstrike ++;
					if(reading_fromuser) cout<<"Frame finished;"<<endl<<endl;
					
				}
				else if(pins==BOWLING_MIN_PINS) //  strike
				{
					framecounts++;
					if(framecounts == BOWLING_MAX_FRAMES) extrarolls+=2;
					if(reading_fromuser) cout<<"Frame finished;"<<endl<<endl;
				}
				else  // open new frame
				{
					open_frame = true;
					open_remaining = pins;
				}
			}
			else
			{
				extrarolls--;
			}

			
			// finished condition
			if(framecounts==BOWLING_MAX_FRAMES && extrarolls==0)
			{
				finished=true;
			}
		}	
		
		

		




	}

	// All ok
	if(quit)
	{
		cout<<"Quit the program. Bye!"<<endl;
		return -1;
	}
	else
	{
		return calculate_scores(pinss);
	}
}

int getnpins(string& s)
{
	// returns n pins in this roll
	// returns: -1 if quit
	// returns: -2 if non-number characters
	// returns: -3 if unkown error
	string clean_string;	
	bool found_non_digit = false;
	int  found_quit  = 0;

	for_each(s.begin(),s.end(), [&](char c){
		if(isdigit(c))
			clean_string+=c;
		else if(c=='q' || c=='Q')
			found_quit += 1;
		else if(!isspace(c))
			found_non_digit = true;
			
	});
	
	
	if(clean_string.size() && ! found_non_digit && !found_quit)
	{
		int result;
		try{
			result = stoi(clean_string);
		}
		catch(int e){
			result = -3;	
		}
		return result;
	}
	else if(found_quit == 1 && !found_non_digit && !clean_string.size())
		return -1;
	else 
		return -2;
	
}
