#include "gtest/gtest.h"

#include <bowling.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


bool contains_message(vector<string>& messeages, string && lookup_string)
{
	bool result = false;
	for_each(messeages.begin(), messeages.end(), [&](string& s){
		if(s== lookup_string)
		{
			result = true;
		}
	});
	return result;
}

TEST(Bowling, ALL_STRIKES)
{
	vector<string> messeages;
	vector<string> input = {
				"0","0","0","0","0","0",
				"0","0","0","0","0","0"
				};
	ASSERT_EQ(getscore(input,messeages),300);
}

TEST(Bowling, ALL_SPARES)
{
	vector<string> messeages;
	vector<string> input = {"5","0","5","0","5","0",
				"5","0","5","0","5","0",
				"5","0","5","0","5","0",
				"5","0","5"};
	ASSERT_EQ(getscore(input,messeages), 150);
}


TEST(Bowling, NORMAL_GAME)
{
	vector<string> messeages;
	vector<string> input = {    "0","5","0","1","0",
				"5","0","5","0","5","0",
				"5","0",    "0","5","0",
				"5","0","5"};
	ASSERT_EQ(getscore(input,messeages), 169);
}

TEST(Bowling, ALL_SPARES_AND_WRONGINPUT)
{
	vector<string> messeages;
	vector<string> input = {"5","0","5","0","5","0",  "-1", "sometext",
				"5","0","5","0","5","0",  "11", "0.1",
				"5","0","5","0","5","6",  " 0", ""
				"5", "sometext",
				"0", "1 sd",
				"5"};
	ASSERT_EQ(getscore(input,messeages), 150);
}

TEST(Bowling, ALL_SPARES_AND_SPACES)
{
	vector<string> messeages;
	vector<string> input = {"5","0","5","0","5","0", 
				"5","0","5","0","5","0",  
				"5","0","5","0","5","0\n",  
				"\r5", 
				"\t0",
				"  5"};
	ASSERT_EQ(getscore(input,messeages), 150);
}

TEST(Bowling, QUIT)
{
	vector<string> messeages;
	vector<string> input = {"5","0","5","0","5","q"};
	ASSERT_LT(getscore(input,messeages), 0);
}


TEST(Bowling, WRONG_INPUT_FORMAT1)
{
	vector<string> messeages;
	vector<string> input = {"df","q"};
	getscore(input,messeages);
	ASSERT_TRUE(contains_message(messeages,string(BOWLING_WRONG_INPUT_FORMAT)));
}

TEST(Bowling, WRONG_INPUT_FORMAT2)
{
	vector<string> messeages;
	vector<string> input = {"0.5","q"};
	getscore(input,messeages);
	ASSERT_TRUE(contains_message(messeages,BOWLING_WRONG_INPUT_FORMAT));
}

TEST(Bowling, WRONG_INPUT_FORMAT3)
{
	vector<string> messeages;
	vector<string> input = {"-5","q"};
	getscore(input,messeages);
	ASSERT_TRUE(contains_message(messeages,BOWLING_WRONG_INPUT_FORMAT));
}

TEST(Bowling, WRONG_INPUT_NUMBER)
{
	vector<string> messeages;
	vector<string> input = {"5","6","q"};
	getscore(input,messeages);
	ASSERT_TRUE(contains_message(messeages,BOWLING_WRONG_INPUT_NUMBER));
}

int main(int argc, char** argv)
{

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
