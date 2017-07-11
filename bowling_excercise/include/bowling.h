#pragma once
#include <string>
#include <vector>

#define BOWLING_WRONG_INPUT_FORMAT     "Wrong input format"
#define BOWLING_WRONG_INPUT_NUMBER     "Number out of allowed range" 
#define BOWLING_WRONG_INPUT_INDICATE   "Should be a number in the range from " 
#define BOWLING_WRONG_INPUT_INDICATE_2 " to "
#define BOWLING_MIN_PINS               0
#define BOWLING_MAX_PINS               10
#define BOWLING_MAX_FRAMES             10

using namespace std;

bool removeme();
int  getscore(vector<string>, vector<string>&);
int  getscore();

int  getnpins(string& );
