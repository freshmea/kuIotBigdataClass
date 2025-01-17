#include "tetris.h"
#include "utils.h"
#include <gtest/gtest.h>

// Tetromino tetrominos[] = {
// 	{{{{0, 0}, {1, 0}, {2, 0}, {3, 0}},
// 	  {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
// 	  {{0, 0}, {-1, 0}, {-2, 0}, {-3, 0}},
// 	  {{0, 0}, {0, -1}, {0, -2}, {0, -3}}},
// 	 {255, 0, 0, 255},
// 	 0}, // I
// 	{{{{0, 0}, {0, 1}, {1, 0}, {1, 1}},
// 	  {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
// 	  {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
// 	  {{0, 0}, {0, 1}, {1, 0}, {1, 1}}},
// 	 {0, 255, 0, 255},
// 	 0}, // O
// 	{{{{0, 0}, {1, 0}, {2, 0}, {2, 1}},
// 	  {{0, 0}, {0, 1}, {0, 2}, {-1, 2}},
// 	  {{0, 0}, {-1, 0}, {-2, 0}, {-2, -1}},
// 	  {{0, 0}, {0, -1}, {0, -2}, {1, -2}}},
// 	 {0, 0, 255, 255},
// 	 0}, // J
// 	{{{{0, 1}, {1, 1}, {2, 1}, {2, 0}},
// 	  {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
// 	  {{0, 0}, {-1, 0}, {-2, 0}, {-2, -1}},
// 	  {{0, 0}, {0, -1}, {0, -2}, {-1, -2}}},
// 	 {255, 255, 0, 255},
// 	 0}, // L
// 	{{{{0, 1}, {1, 1}, {1, 0}, {2, 0}},
// 	  {{0, 0}, {0, 1}, {-1, 1}, {-1, 2}},
// 	  {{0, 0}, {-1, 0}, {-1, -1}, {-2, -1}},
// 	  {{0, 0}, {0, -1}, {1, -1}, {1, -2}}},
// 	 {0, 255, 255, 255},
// 	 0}, // S
// 	{{{{0, 0}, {1, 0}, {1, 1}, {2, 1}},
// 	  {{0, 0}, {0, 1}, {-1, 1}, {-1, 2}},
// 	  {{0, 0}, {-1, 0}, {-1, -1}, {-2, -1}},
// 	  {{0, 0}, {0, -1}, {1, -1}, {1, -2}}},
// 	 {255, 0, 255, 255},
// 	 0}, // Z
// 	{{{{0, 1}, {1, 0}, {1, 1}, {2, 1}},
// 	  {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
// 	  {{0, 0}, {-1, 0}, {-1, -1}, {-2, -1}},
// 	  {{0, 0}, {0, -1}, {1, -1}, {1, -2}}},
// 	 {128, 0, 128, 255},
// 	 0} // T
// };

// TEST(UtilsTest, AddFunction) {
// 	EXPECT_EQ(add(1, 1), 2);
// 	EXPECT_EQ(add(-1, 1), 0);
// 	EXPECT_EQ(add(-1, -1), -2);
// }

// TEST(TetrisTest, RotateTetromino) {
// 	Tetromino tetromino = tetrominos[0]; // I 테트로미노
// 	rotate_tetromino(&tetromino);
// 	EXPECT_EQ(tetromino.rotation, 1);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][0].x, 0);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][0].y, 0);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][1].x, 0);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][1].y, 1);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][2].x, 0);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][2].y, 2);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][3].x, 0);
// 	EXPECT_EQ(tetromino.blocks[tetromino.rotation][3].y, 3);
// }

// TEST(TetrisTest, CheckCollision) {
// 	Tetromino tetromino = tetrominos[0]; // I 테트로미노
// 	EXPECT_FALSE(check_collision(&tetromino, 100, 100));
// 	EXPECT_TRUE(check_collision(&tetromino, -100, 100));
// 	EXPECT_TRUE(check_collision(&tetromino, 100, -100));
// }

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
