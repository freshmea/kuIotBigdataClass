#include "main.h"

void render_main_screen(SDL_Renderer *renderer, TTF_Font *font) {
	SDL_Color white = {255, 255, 255, 255};
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderClear(renderer);

	SDL_Surface *surface =
		TTF_RenderText_Solid(font, "Press ENTER to start Tetris", white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {100, 100, 400, 50};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);
	SDL_DestroyTexture(texture);
}

void render_pause_screen(SDL_Renderer *renderer, TTF_Font *font) {
	SDL_Color white = {255, 255, 255, 255};
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderClear(renderer);

	SDL_Surface *surface = TTF_RenderText_Solid(font, "Game Pause", white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {100, 200, 400, 100};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);
	SDL_DestroyTexture(texture);
	SDL_RenderPresent(renderer);
}

void render_score(SDL_Renderer *renderer, TTF_Font *font, int score) {
	SDL_Color white = {255, 255, 255, 255};
	char score_text[50];
	snprintf(score_text, sizeof(score_text), "Score: %d", score);

	SDL_Surface *surface = TTF_RenderText_Solid(font, score_text, white);
	SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	SDL_Rect dstrect = {500, 10, 120, 50};
	SDL_RenderCopy(renderer, texture, NULL, &dstrect);
	SDL_DestroyTexture(texture);
}

int main() {
	if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO) != 0) {
		printf("SDL 초기화 실패: %s\n", SDL_GetError());
		return 1;
	}

	if (TTF_Init() == -1) {
		printf("TTF 초기화 실패: %s\n", TTF_GetError());
		SDL_Quit();
		return 1;
	}

	if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) == -1) {
		printf("SDL_mixer 초기화 실패: %s\n", Mix_GetError());
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	SDL_Window *window =
		SDL_CreateWindow("SDL 윈도우", SDL_WINDOWPOS_CENTERED,
						 SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_SHOWN);
	if (window == NULL) {
		printf("윈도우 생성 실패: %s\n", SDL_GetError());
		Mix_CloseAudio();
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	SDL_Renderer *renderer =
		SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	if (renderer == NULL) {
		printf("렌더러 생성 실패: %s\n", SDL_GetError());
		SDL_DestroyWindow(window);
		Mix_CloseAudio();
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	char exe_path[256];
	ssize_t len = readlink("/proc/self/exe", exe_path, sizeof(exe_path) - 1);
	if (len != -1) {
		exe_path[len] = '\0';
	} else {
		printf("실행 파일 경로를 찾을 수 없습니다.\n");
		SDL_DestroyRenderer(renderer);
		SDL_DestroyWindow(window);
		Mix_CloseAudio();
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	char *dir = dirname(exe_path);
	char font_path[256];
	char move_sound_path[256];
	char place_sound_path[256];
	char bgm_path[256];
	snprintf(move_sound_path, sizeof(move_sound_path), "%s/../wave/move.wav",
			 dir);
	snprintf(place_sound_path, sizeof(place_sound_path), "%s/../wave/place.wav",
			 dir);
	snprintf(bgm_path, sizeof(bgm_path), "%s/../wave/bgm.wav", dir);
	Mix_Chunk *move_sound = Mix_LoadWAV(move_sound_path);
	Mix_Chunk *place_sound = Mix_LoadWAV(place_sound_path);
	Mix_Music *bgm = Mix_LoadMUS(bgm_path);
	if (!move_sound || !place_sound || !bgm) {
		printf("효과음 또는 배경음악 로드 실패: %s\n", Mix_GetError());
		SDL_DestroyRenderer(renderer);
		SDL_DestroyWindow(window);
		Mix_CloseAudio();
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	snprintf(font_path, sizeof(font_path), "%s/../NanumFont/NanumGothic.ttf",
			 dir);
	TTF_Font *font = TTF_OpenFont(font_path, 24);
	if (font == NULL) {
		printf("폰트 로드 실패: %s\n", TTF_GetError());
		Mix_FreeChunk(move_sound);
		Mix_FreeChunk(place_sound);
		Mix_FreeMusic(bgm);
		SDL_DestroyRenderer(renderer);
		SDL_DestroyWindow(window);
		Mix_CloseAudio();
		TTF_Quit();
		SDL_Quit();
		return 1;
	}

	int running = 1;
	int show_tetris = 0;
	int paused = 0;
	int score = 0;
	int volume = MIX_MAX_VOLUME / 2; // 초기 볼륨 설정
	SDL_Event event;

	static int block_x = (SCREEN_WIDTH - TETRIS_WIDTH) / 2;
	static int block_y = 0;
	static int current_tetromino = -1;
	static int next_tetromino_index = -1;
	static int rotation_state = 0; // 회전 상태 추가
	if (current_tetromino == -1) {
		srand(time(NULL));
		current_tetromino =
			rand() % (sizeof(tetrominos) / sizeof(tetrominos[0]));
		next_tetromino_index =
			rand() % (sizeof(tetrominos) / sizeof(tetrominos[0]));
	}
	Tetromino *tetromino = &tetrominos[current_tetromino];
	Tetromino *next_tetromino = &tetrominos[next_tetromino_index];

	Uint32 last_time = SDL_GetTicks();
	Uint32 block_last_time = SDL_GetTicks();
	const Uint32 block_interval = 500; // 블럭이 내려오는 속도 조절 (밀리초)

	Mix_PlayMusic(bgm, -1);	 // 배경음악 재생
	Mix_VolumeMusic(volume); // 초기 볼륨 설정

	while (running) {
		Uint32 current_time = SDL_GetTicks();
		Uint32 delta_time = current_time - last_time;
		last_time = current_time;

		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = 0;
			} else if (event.type == SDL_KEYDOWN) {
				if (event.key.keysym.sym == SDLK_RETURN) {
					show_tetris = 1;
				} else if (event.key.keysym.sym == SDLK_q) {
					if (show_tetris) {
						running = 0;
					}
				} else if (event.key.keysym.sym == SDLK_p) {
					paused = !paused;
					if (paused) {
						render_pause_screen(renderer, font);
						Mix_PauseMusic(); // 배경음악 일시 정지
					} else {
						Mix_ResumeMusic(); // 배경음악 재개
					}
				} else if (event.key.keysym.sym == SDLK_1) {
					volume = (volume + 8 > MIX_MAX_VOLUME) ? MIX_MAX_VOLUME
														   : volume + 8;
					Mix_VolumeMusic(volume); // 볼륨 업
				} else if (event.key.keysym.sym == SDLK_2) {
					volume = (volume - 8 < 0) ? 0 : volume - 8;
					Mix_VolumeMusic(volume); // 볼륨 다운
				} else if (!paused) {
					if (event.key.keysym.sym == SDLK_a) {
						if (!check_collision(tetromino, block_x - BLOCK_SIZE,
											 block_y)) {
							block_x -= BLOCK_SIZE;
							Mix_PlayChannel(-1, move_sound, 0);
						}
					} else if (event.key.keysym.sym == SDLK_d) {
						if (!check_collision(tetromino, block_x + BLOCK_SIZE,
											 block_y)) {
							block_x += BLOCK_SIZE;
							Mix_PlayChannel(-1, move_sound, 0);
						}
					} else if (event.key.keysym.sym == SDLK_w) {
						int next_rotation_state = (rotation_state + 1) % 4;
						Tetromino rotated_tetromino = *tetromino;
						rotate_tetromino(&rotated_tetromino);
						if (!check_collision(&rotated_tetromino, block_x,
											 block_y)) {
							*tetromino = rotated_tetromino;
							rotation_state = next_rotation_state;
							Mix_PlayChannel(-1, move_sound, 0);
						}
					} else if (event.key.keysym.sym == SDLK_s) {
						if (!check_collision(tetromino, block_x,
											 block_y + BLOCK_SIZE)) {
							block_y += BLOCK_SIZE;
							Mix_PlayChannel(-1, move_sound, 0);
						}
					} else if (event.key.keysym.sym == SDLK_SPACE) {
						while (!check_collision(tetromino, block_x,
												block_y + BLOCK_SIZE)) {
							block_y += BLOCK_SIZE;
						}
						Mix_PlayChannel(-1, move_sound, 0);
					}
				}
			}
		}

		if (show_tetris && !paused) {
			if (current_time - block_last_time >= block_interval) {
				block_last_time = current_time;
				if (!check_collision(tetromino, block_x,
									 block_y + BLOCK_SIZE)) {
					block_y += BLOCK_SIZE;
				} else {
					place_tetromino(tetromino, block_x, block_y);
					score += 10; // 블럭이 바닥에 놓일 때마다 10점 추가
					Mix_PlayChannel(-1, place_sound, 0);
					int lines_cleared =
						clear_full_lines(); // 한 줄이 모두 채워져 있으면 지우기
					score += lines_cleared * 100; // 라인 클리어 시 점수 증가
					block_x = (SCREEN_WIDTH - TETRIS_WIDTH) / 2;
					block_y = 0;
					current_tetromino = next_tetromino_index;
					tetromino = &tetrominos[current_tetromino];
					next_tetromino_index =
						rand() % (sizeof(tetrominos) / sizeof(tetrominos[0]));
					next_tetromino = &tetrominos[next_tetromino_index];
					rotation_state =
						0; // 새로운 테트로미노가 생성될 때 회전 상태 초기화

					// 블럭 생성 위치에 이미 블럭이 쌓여 있는지 확인
					if (check_collision(tetromino, block_x, block_y)) {
						running = 0; // 게임 종료
					}
				}
			}
			render_tetris_screen(renderer, font, tetromino, &block_x, &block_y);
			render_next_tetromino(renderer, font, next_tetromino);
			render_score(renderer, font, score);
		} else if (!show_tetris) {
			render_main_screen(renderer, font);
		}

		// 60fps 유지
		Uint32 frame_time = SDL_GetTicks() - current_time;
		if (frame_time < 16) {
			SDL_Delay(16 - frame_time);
		}
		SDL_RenderPresent(renderer); // 렌더링 업데이트
	}

	Mix_FreeChunk(move_sound);
	Mix_FreeChunk(place_sound);
	Mix_FreeMusic(bgm);
	Mix_CloseAudio();
	TTF_CloseFont(font);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	TTF_Quit();
	SDL_Quit();

	return 0;
}