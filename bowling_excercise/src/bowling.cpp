#include "bowling.h"
#include <vector>
#include <iostream>
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

int getscore(vector<string>& input)
{
	
	vector<short> scores;
	//bool wait_snd_roll = false; // waiting second roll
	//bool wait_trd_roll = false; // waiting third  roll

	while(true)
	{
		// get score
		if(input.size())
		{
			break;	
		}
		else
		{
			cout<<"Enter number of remaining pins in this roll: from 0 to 10 (or 'q' to exit the program) and press 'enter': "<< endl;		  
			string score;
			cin>>score;
			break;
		}

		// save score

		// increment number of frames

		// trigger waiting for the second roll

		// trigger waiting for the third roll

		// exit condition: 10 frames + no spares/strikes 

		// exit condition: 10 frames + spare

		// exit condition: 10 frames + strike

		// exit condition: user interrupt
	}

	// All ok
	return 99999;
}
