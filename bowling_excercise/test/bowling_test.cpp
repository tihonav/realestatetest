#include "gtest/gtest.h"

#include <bowling.h>
#include <string>
#include <vector>

TEST(Bowling, ALL_STRIKES)
{
	vector<string> input = {
				"0","0","0","0","0","0",
				"0","0","0","0","0","0"
				};
	ASSERT_EQ(getscore(input),300);
}

TEST(Bowling, ALL_SPARES)
{
	vector<string> input = {"5","0","5","0","5","0",
				"5","0","5","0","5","0",
				"5","0","5","0","5","0",
				"5","0","5"};
	ASSERT_EQ(getscore(input), 150);
}


TEST(Bowling, NORMAL_GAME)
{
	vector<string> input = {    "0","5","0","1","0",
				"5","0","5","0","5","0",
				"5","0",    "0","5","0",
				"5","0","5"};
	ASSERT_EQ(getscore(input), 169);
}

TEST(Bowling, ALL_SPARES_AND_WRONGINPUT)
{
	vector<string> input = {"5","0","5","0","5","0",  "-1", "sometext",
				"5","0","5","0","5","0",  "11", "0.1",
				"5","0","5","0","5","6",  " 0", ""
				"5", "sometext",
				"0",
				"5"};
	ASSERT_EQ(getscore(input), 150);
}

TEST(Bowling, QUIT)
{
	vector<string> input = {"5","0","5","0","5","q"};
	ASSERT_LT(getscore(input), 0);
}


int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
