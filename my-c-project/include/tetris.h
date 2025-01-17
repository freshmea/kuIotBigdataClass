#ifndef TETRIS_H
#define TETRIS_H

#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>

#ifdef __cplusplus
extern "C" {
#endif

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480
#define TETRIS_WIDTH (SCREEN_WIDTH / 3)
#define TETRIS_HEIGHT SCREEN_HEIGHT
#define BLOCK_SIZE 15
#define BOARD_WIDTH (TETRIS_WIDTH / BLOCK_SIZE)
#define BOARD_HEIGHT ((SCREEN_HEIGHT - BLOCK_SIZE * 3) / BLOCK_SIZE)

typedef struct {
	int x, y;
} Block;

typedef struct {
	Block blocks[4][4]; // 4가지 회전 상태
	SDL_Color color;
	int rotation; // 현재 회전 상태 (0-3)
} Tetromino;

typedef struct {
	int occupied;
	SDL_Color color;
} Cell;

extern Tetromino tetrominos[];
extern Cell board[BOARD_HEIGHT][BOARD_WIDTH];

void render_tetris_screen(SDL_Renderer *renderer, TTF_Font *font,
						  Tetromino *tetromino, int *block_x, int *block_y);
void rotate_tetromino(Tetromino *tetromino);
int check_collision(Tetromino *tetromino, int block_x, int block_y);
void place_tetromino(Tetromino *tetromino, int block_x, int block_y);
void clear_full_lines();
void render_next_tetromino(SDL_Renderer *renderer, TTF_Font *font,
						   Tetromino *next_tetromino);

#ifdef __cplusplus
}
#endif

#endif // TETRIS_H
