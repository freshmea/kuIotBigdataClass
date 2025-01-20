#include "main.h"
#include "tetris.h"
#include "utils.h"
#include <gtest/gtest.h>

TEST(UtilsTest, AddFunction) {
	EXPECT_EQ(add(1, 1), 2);
	EXPECT_EQ(add(-1, 1), 0);
	EXPECT_EQ(add(-1, -1), -2);
}

TEST(TetrisTest, RotateTetromino) {
	Tetromino tetromino = tetrominos[0]; // I 테트로미노
	rotate_tetromino(&tetromino);
	EXPECT_EQ(tetromino.rotation, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][0].x, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][0].y, 0);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][1].x, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][1].y, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][2].x, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][2].y, 2);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][3].x, 1);
	EXPECT_EQ(tetromino.blocks[tetromino.rotation][3].y, 3);
}

TEST(TetrisTest, CheckCollision) {
	Tetromino tetromino = tetrominos[0]; // I 테트로미노
	EXPECT_TRUE(check_collision(&tetromino, 100, 100));
	EXPECT_TRUE(check_collision(&tetromino, -100, 100));
	EXPECT_TRUE(check_collision(&tetromino, 100, -100));
}

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
