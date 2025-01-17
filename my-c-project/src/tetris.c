#include "tetris.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BOARD_WIDTH (TETRIS_WIDTH / BLOCK_SIZE)
#define BOARD_HEIGHT ((SCREEN_HEIGHT - BLOCK_SIZE * 3) / BLOCK_SIZE)

int board[BOARD_HEIGHT][BOARD_WIDTH] = {0};

void rotate_tetromino(Tetromino *tetromino) {
	for (int i = 0; i < 4; i++) {
		int temp = tetromino->blocks[i].x;
		tetromino->blocks[i].x = tetromino->blocks[i].y;
		tetromino->blocks[i].y = -temp;
	}
}

int check_collision(Tetromino *tetromino, int block_x, int block_y) {
	for (int i = 0; i < 4; i++) {
		int x = (block_x - (SCREEN_WIDTH - TETRIS_WIDTH) / 2) / BLOCK_SIZE +
				tetromino->blocks[i].x;
		int y = block_y / BLOCK_SIZE + tetromino->blocks[i].y;
		if (x < 0 || x >= BOARD_WIDTH || y >= BOARD_HEIGHT || board[y][x]) {
			return 1;
		}
	}
	return 0;
}

void place_tetromino(Tetromino *tetromino, int block_x, int block_y) {
	for (int i = 0; i < 4; i++) {
		int x = (block_x - (SCREEN_WIDTH - TETRIS_WIDTH) / 2) / BLOCK_SIZE +
				tetromino->blocks[i].x;
		int y = block_y / BLOCK_SIZE + tetromino->blocks[i].y;
		board[y][x] = 1;
	}
}

void render_tetris_screen(SDL_Renderer *renderer, TTF_Font *font,
						  Tetromino *tetromino, int *block_x, int *block_y) {
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderClear(renderer);

	// 테트리스 벽 그리기
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	SDL_Rect left_wall = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 - BLOCK_SIZE, 0,
						  BLOCK_SIZE, TETRIS_HEIGHT - BLOCK_SIZE * 3};
	SDL_Rect right_wall = {(SCREEN_WIDTH + TETRIS_WIDTH) / 2 - BLOCK_SIZE, 0,
						   BLOCK_SIZE, TETRIS_HEIGHT - BLOCK_SIZE * 3};
	SDL_Rect bottom_wall = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 - BLOCK_SIZE,
							SCREEN_HEIGHT - BLOCK_SIZE * 3,
							TETRIS_WIDTH + BLOCK_SIZE * 2, BLOCK_SIZE};
	SDL_RenderFillRect(renderer, &left_wall);
	SDL_RenderFillRect(renderer, &right_wall);
	SDL_RenderFillRect(renderer, &bottom_wall);

	// 테트리스 블럭 그리기
	SDL_SetRenderDrawColor(renderer, tetromino->color.r, tetromino->color.g,
						   tetromino->color.b, tetromino->color.a);
	for (int i = 0; i < 4; i++) {
		SDL_Rect block = {*block_x + tetromino->blocks[i].x * BLOCK_SIZE,
						  *block_y + tetromino->blocks[i].y * BLOCK_SIZE,
						  BLOCK_SIZE, BLOCK_SIZE};
		SDL_RenderFillRect(renderer, &block);
	}

	// 보드에 쌓인 블럭 그리기
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	for (int y = 0; y < BOARD_HEIGHT; y++) {
		for (int x = 0; x < BOARD_WIDTH; x++) {
			if (board[y][x]) {
				SDL_Rect block = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 +
									  x * BLOCK_SIZE,
								  y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE};
				SDL_RenderFillRect(renderer, &block);
			}
		}
	}

	// "Press Q to quit" 글자 그리기
	TTF_Font *small_font = TTF_OpenFont("NanumFont/NanumGothic.ttf", 12);
	SDL_Color white = {255, 255, 255, 255};
	SDL_Surface *surface =
		TTF_RenderText_Solid(small_font, "Press Q to quit", white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {10, 420, 200, 20};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);

	// 글자 위쪽에 가로선 추가
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	SDL_RenderDrawLine(renderer, 10, 415, 210, 415);

	SDL_RenderPresent(renderer);

	SDL_DestroyTexture(texture);
	TTF_CloseFont(small_font);
}
