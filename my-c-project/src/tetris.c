#include "tetris.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void rotate_tetromino(Tetromino *tetromino) {
	tetromino->rotation = (tetromino->rotation + 1) % 4;
}

int check_collision(Tetromino *tetromino, int block_x, int block_y) {
	for (int i = 0; i < 4; i++) {
		int x = (block_x - (SCREEN_WIDTH - TETRIS_WIDTH) / 2) / BLOCK_SIZE +
				tetromino->blocks[tetromino->rotation][i].x;
		int y =
			block_y / BLOCK_SIZE + tetromino->blocks[tetromino->rotation][i].y;
		if (x < 0 || x >= BOARD_WIDTH || y >= BOARD_HEIGHT ||
			(y >= 0 && board[y][x].occupied)) {
			return 1;
		}
	}
	return 0;
}

void place_tetromino(Tetromino *tetromino, int block_x, int block_y) {
	for (int i = 0; i < 4; i++) {
		int x = (block_x - (SCREEN_WIDTH - TETRIS_WIDTH) / 2) / BLOCK_SIZE +
				tetromino->blocks[tetromino->rotation][i].x;
		int y =
			block_y / BLOCK_SIZE + tetromino->blocks[tetromino->rotation][i].y;
		board[y][x].occupied = 1;
		board[y][x].color = tetromino->color;
	}
	clear_full_lines();
}

void clear_full_lines() {
	for (int y = 0; y < BOARD_HEIGHT; y++) {
		int full = 1;
		for (int x = 0; x < BOARD_WIDTH; x++) {
			if (!board[y][x].occupied) {
				full = 0;
				break;
			}
		}
		if (full) {
			for (int k = y; k > 0; k--) {
				for (int x = 0; x < BOARD_WIDTH; x++) {
					board[k][x] = board[k - 1][x];
				}
			}
			for (int x = 0; x < BOARD_WIDTH; x++) {
				board[0][x].occupied = 0;
			}
		}
	}
}

void render_tetris_screen(SDL_Renderer *renderer, TTF_Font *font,
						  Tetromino *tetromino, int *block_x, int *block_y) {
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderClear(renderer);

	// 테트리스 벽 그리기
	int padding = 3;
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	SDL_Rect left_wall = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 - BLOCK_SIZE, 0,
						  BLOCK_SIZE, TETRIS_HEIGHT - BLOCK_SIZE * 3};
	SDL_Rect right_wall = {(SCREEN_WIDTH + TETRIS_WIDTH) / 2 - padding, 0,
						   BLOCK_SIZE, TETRIS_HEIGHT - BLOCK_SIZE * 3};
	SDL_Rect bottom_wall = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 - BLOCK_SIZE,
							SCREEN_HEIGHT - BLOCK_SIZE * 3,
							TETRIS_WIDTH + BLOCK_SIZE * 2 - padding,
							BLOCK_SIZE};
	SDL_RenderFillRect(renderer, &left_wall);
	SDL_RenderFillRect(renderer, &right_wall);
	SDL_RenderFillRect(renderer, &bottom_wall);

	// 테트리스 블럭 그리기
	SDL_SetRenderDrawColor(renderer, tetromino->color.r, tetromino->color.g,
						   tetromino->color.b, tetromino->color.a);
	for (int i = 0; i < 4; i++) {
		SDL_Rect block = {
			*block_x + tetromino->blocks[tetromino->rotation][i].x * BLOCK_SIZE,
			*block_y + tetromino->blocks[tetromino->rotation][i].y * BLOCK_SIZE,
			BLOCK_SIZE, BLOCK_SIZE};
		SDL_RenderFillRect(renderer, &block);
	}

	// 보드에 쌓인 블럭 그리기
	for (int y = 0; y < BOARD_HEIGHT; y++) {
		for (int x = 0; x < BOARD_WIDTH; x++) {
			if (board[y][x].occupied) {
				SDL_SetRenderDrawColor(renderer, board[y][x].color.r,
									   board[y][x].color.g, board[y][x].color.b,
									   board[y][x].color.a);
				SDL_Rect block = {(SCREEN_WIDTH - TETRIS_WIDTH) / 2 +
									  x * BLOCK_SIZE,
								  y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE};
				SDL_RenderFillRect(renderer, &block);
			}
		}
	}
}

void render_next_tetromino(SDL_Renderer *renderer, TTF_Font *font,
						   Tetromino *next_tetromino) {
	SDL_Color white = {255, 255, 255, 255};
	SDL_Surface *surface = TTF_RenderText_Solid(font, "Next Block", white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {10, 10, 100, 20};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);
	SDL_DestroyTexture(texture);

	SDL_Rect next_block_rect = {10, 40, 100, 100};
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	SDL_RenderDrawRect(renderer, &next_block_rect);

	SDL_SetRenderDrawColor(renderer, next_tetromino->color.r,
						   next_tetromino->color.g, next_tetromino->color.b,
						   next_tetromino->color.a);
	for (int i = 0; i < 4; i++) {
		SDL_Rect block = {20 + next_tetromino->blocks[0][i].x * BLOCK_SIZE,
						  50 + next_tetromino->blocks[0][i].y * BLOCK_SIZE,
						  BLOCK_SIZE, BLOCK_SIZE};
		SDL_RenderFillRect(renderer, &block);
	}
}
