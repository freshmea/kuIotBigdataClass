#include "tetris.h"
#include "utils.h"
#include <gtest/gtest.h>

TEST(UtilsTest, AddFunction) {
	EXPECT_EQ(add(1, 1), 2);
	EXPECT_EQ(add(-1, 1), 0);
	EXPECT_EQ(add(-1, -1), -2);
}

TEST(TetrisTest, RotateTetromino) {
	Tetromino tetromino = {{{0, 0}, {1, 0}, {2, 0}, {3, 0}}, {255, 0, 0, 255}};
	rotate_tetromino(&tetromino);
	EXPECT_EQ(tetromino.blocks[0].x, 0);
	EXPECT_EQ(tetromino.blocks[0].y, 0);
	EXPECT_EQ(tetromino.blocks[1].x, 0);
	EXPECT_EQ(tetromino.blocks[1].y, -1);
	EXPECT_EQ(tetromino.blocks[2].x, 0);
	EXPECT_EQ(tetromino.blocks[2].y, -2);
	EXPECT_EQ(tetromino.blocks[3].x, 0);
	EXPECT_EQ(tetromino.blocks[3].y, -3);
}

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
