#include "tetris.h"
#include "utils.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

Tetromino tetrominos[] = {
	{{{0, 0}, {1, 0}, {2, 0}, {3, 0}}, {255, 0, 0, 255}},	// I
	{{{0, 0}, {0, 1}, {1, 0}, {1, 1}}, {0, 255, 0, 255}},	// O
	{{{0, 0}, {1, 0}, {2, 0}, {2, 1}}, {0, 0, 255, 255}},	// J
	{{{0, 1}, {1, 1}, {2, 1}, {2, 0}}, {255, 255, 0, 255}}, // L
	{{{0, 1}, {1, 1}, {1, 0}, {2, 0}}, {0, 255, 255, 255}}, // S
	{{{0, 0}, {1, 0}, {1, 1}, {2, 1}}, {255, 0, 255, 255}}, // Z
	{{{0, 1}, {1, 0}, {1, 1}, {2, 1}}, {128, 0, 128, 255}}	// T
};

void render_main_screen(SDL_Renderer *renderer, TTF_Font *font) {
	SDL_Color white = {255, 255, 255, 255};
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderClear(renderer);

	SDL_Surface *surface =
		TTF_RenderText_Solid(font, "Press SPACE to start Tetris", white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {100, 100, 400, 50};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);
	SDL_RenderPresent(renderer);

	SDL_DestroyTexture(texture);
}

int main() {
	if (SDL_Init(SDL_INIT_VIDEO) != 0) {
		printf("SDL 초기화 실패: %s\n", SDL_GetError());
		return 1;
	}

	if (TTF_Init() == -1) {
		printf("TTF 초기화 실패: %s\n", TTF_GetError());
		SDL_Quit();
		return 1;
	}

	SDL_Window *window =
		SDL_CreateWindow("SDL 윈도우", SDL_WINDOWPOS_CENTERED,
						 SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_SHOWN);
	if (window == NULL) {
		printf("윈도우 생성 실패: %s\n", SDL_GetError());
		SDL_Quit();
		return 1;
	}

	SDL_Renderer *renderer =
		SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	if (renderer == NULL) {
		printf("렌더러 생성 실패: %s\n", SDL_GetError());
		SDL_DestroyWindow(window);
		SDL_Quit();
		return 1;
	}

	TTF_Font *font = TTF_OpenFont("NanumFont/NanumGothic.ttf", 24);
	if (font == NULL) {
		printf("폰트 로드 실패: %s\n", TTF_GetError());
		SDL_DestroyRenderer(renderer);
		SDL_DestroyWindow(window);
		SDL_Quit();
		return 1;
	}

	int running = 1;
	int show_tetris = 0;
	SDL_Event event;

	static int block_x = (SCREEN_WIDTH - TETRIS_WIDTH) / 2;
	static int block_y = 0;
	static int current_tetromino = -1;
	if (current_tetromino == -1) {
		srand(time(NULL));
		current_tetromino =
			rand() % (sizeof(tetrominos) / sizeof(tetrominos[0]));
	}
	Tetromino *tetromino = &tetrominos[current_tetromino];

	while (running) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = 0;
			} else if (event.type == SDL_KEYDOWN) {
				if (event.key.keysym.sym == SDLK_SPACE) {
					show_tetris = 1;
				} else if (event.key.keysym.sym == SDLK_q) {
					if (show_tetris) {
						running = 0;
					}
				} else if (event.key.keysym.sym == SDLK_a) {
					if (block_x >
						(SCREEN_WIDTH - TETRIS_WIDTH) / 2 - BLOCK_SIZE) {
						block_x -= BLOCK_SIZE;
					}
				} else if (event.key.keysym.sym == SDLK_d) {
					if (block_x <
						(SCREEN_WIDTH + TETRIS_WIDTH) / 2 - BLOCK_SIZE * 2) {
						block_x += BLOCK_SIZE;
					}
				} else if (event.key.keysym.sym == SDLK_w) {
					rotate_tetromino(tetromino);
				}
			}
		}

		if (show_tetris) {
			if (!check_collision(tetromino, block_x, block_y + BLOCK_SIZE)) {
				block_y += BLOCK_SIZE;
			} else {
				place_tetromino(tetromino, block_x, block_y);
				block_x = (SCREEN_WIDTH - TETRIS_WIDTH) / 2;
				block_y = 0;
				current_tetromino =
					rand() % (sizeof(tetrominos) / sizeof(tetrominos[0]));
				tetromino = &tetrominos[current_tetromino];
			}
			render_tetris_screen(renderer, font, tetromino, &block_x, &block_y);
			SDL_Delay(500); // 블럭이 내려오는 속도 조절
		} else {
			render_main_screen(renderer, font);
		}
	}

	TTF_CloseFont(font);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	TTF_Quit();
	SDL_Quit();

	return 0;
}