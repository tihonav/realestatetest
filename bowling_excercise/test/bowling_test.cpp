#include "gtest/gtest.h"

#include <bowling.h>

TEST(Bowling, REPLACE_ME)
{
    // We want this test to fail on purpose to validate that everything is setup correctly.
    ASSERT_TRUE(false);
}

TEST(Bowling, REPLACE_ME2)
{
    ASSERT_TRUE(removeme());
}


int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
