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
	return getscore(input);
}

int getscore(vector<string> input)
{
	//
	// returns: total score
	//          -1 if interrupted by user
	// 

	const int nonumber = 99999;

	bool reading_fromuser = true;
	if(input.size())
		reading_fromuser = false;

	vector<short> scores;
	//bool wait_snd_roll = false; // waiting second roll
	//bool wait_trd_roll = false; // waiting third  roll
	bool quit = false;
	

	while(true)
	{
		int score = nonumber;
		
		// get score
		if(!reading_fromuser)
		{
			if(input.size())
			{
				score = getnpins(input.front());					
				input.erase(input.begin(),input.begin()+1);
			}
			else
			{
				break;
			}
		}
		else
		{
			string score_str;
			cout<<"Enter number of remaining pins in this roll: from 0 to 10 (or 'q' to exit the program) and press 'enter': "<< endl;		  
			cin>>score_str;
			score = getnpins(score_str);
			break;
		}

		// exit condition: user interrupt
		if(score == -1)
		{
			quit = true;
			break;
		}

		// save score

		// increment number of frames

		// trigger waiting for the second roll

		// trigger waiting for the third roll

		// exit condition: 10 frames + no spares/strikes 

		// exit condition: 10 frames + spare

		// exit condition: 10 frames + strike

	}

	// All ok
	if(quit)
		return -1;
	else
		return nonumber;
}

int getnpins(string& s)
{
	// returns n pins in this roll
	// returns: -1 if quit
	// returns: -2 if non-number characters
	// returns: -3 if . or - in the string 
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
	
	if(found_quit == 1 && !found_non_digit && !clean_string.size())
		return -1;
	else
		return 0;
}
