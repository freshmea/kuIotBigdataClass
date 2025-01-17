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

typedef struct {
	int x, y;
} Block;

typedef struct {
	Block blocks[4];
	SDL_Color color;
} Tetromino;

extern Tetromino tetrominos[];

void render_tetris_screen(SDL_Renderer *renderer, TTF_Font *font,
						  Tetromino *tetromino, int *block_x, int *block_y);
void rotate_tetromino(Tetromino *tetromino);
int check_collision(Tetromino *tetromino, int block_x, int block_y);
void place_tetromino(Tetromino *tetromino, int block_x, int block_y);

#ifdef __cplusplus
}
#endif

#endif // TETRIS_H
