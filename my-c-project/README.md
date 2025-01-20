# My C Project

이 프로젝트는 C 언어로 작성된 간단한 애플리케이션입니다. 이 README 파일은 프로젝트의 구조와 빌드 및 실행 방법에 대한 정보를 제공합니다.

이 프로젝트의 목적은 SDL 라이브러리를 사용하여 간단한 테트리스 게임을 만드는 것입니다.

## 프로젝트 구조

```bash
my-c-project
├── src
│   ├── main.c       # 애플리케이션의 진입점
│   ├── utils.c      # 유틸리티 함수 정의
│   └── tetris.c     # 테트리스 게임 로직
├── include
│   ├── utils.h      # 유틸리티 함수 선언
│   └── tetris.h     # 테트리스 게임 헤더 파일
├── tests            # 테스트 코드 디렉토리
│   └── test_main.cpp # gtest 테스트 코드
├── wave             # 오디오 파일 디렉토리
│   ├── move.wav     # 블럭 이동 효과음
│   ├── place.wav    # 블럭 배치 효과음
│   └── bgm.wav      # 배경음악
├── CMakeLists.txt   # CMake 빌드 파일
└── README.md        # 프로젝트 문서
```

## 기술 스택

- C 언어
- GCC (GNU Compiler Collection)
- CMake (빌드 자동화 도구)
- SDL (Simple DirectMedia Layer)
- SDL_ttf (TrueType Font 지원)
- SDL_mixer (오디오 지원)
- gtest (Google Test)

## 빌드 및 실행 방법

1. **디펜던시 설치**: SDL, SDL_ttf 및 SDL_mixer 라이브러리를 설치합니다.
   ```bash
   sudo apt-get install libsdl2-dev libsdl2-ttf-dev libsdl2-mixer-dev
   ```

2. **빌드**: 프로젝트 디렉토리에서 다음 명령어를 실행하여 CMake를 사용해 애플리케이션을 빌드합니다.
   ```bash
   mkdir build
   cd build
   cmake ..
   make
   ```

3. **실행**: 빌드가 완료되면 생성된 실행 파일을 다음 명령어로 실행합니다.
   ```bash
   ./my-c-project
   ```

## 테스트 방법

1. **gtest 설치**: gtest 라이브러리를 설치합니다.
   ```bash
   sudo apt-get install libgtest-dev
   cd /usr/src/gtest
   sudo cmake CMakeLists.txt
   sudo make
   sudo cp *.a /usr/lib
   ```

2. **테스트 빌드 및 실행**: 프로젝트 디렉토리에서 다음 명령어를 실행하여 테스트를 빌드하고 실행합니다.
   ```bash
   make
   ./test-my-c-project
   ```

## 추가 정보

- `src/main.c` 파일은 프로그램의 `main` 함수를 포함하고 있으며, 유틸리티 모듈의 함수를 호출합니다.
- `src/utils.c` 파일은 다양한 헬퍼 기능을 제공하는 유틸리티 함수의 정의를 포함합니다.
- `src/tetris.c` 파일은 테트리스 게임 로직을 포함합니다.
- `include/utils.h` 헤더 파일은 `utils.c`에서 사용되는 함수와 데이터 구조를 선언합니다.
- `include/tetris.h` 헤더 파일은 `tetris.c`에서 사용되는 함수와 데이터 구조를 선언합니다.
- `tests/test_main.cpp` 파일은 gtest를 사용한 테스트 코드를 포함합니다.
- `wave` 디렉토리는 게임에서 사용되는 오디오 파일을 포함합니다.
- `CMakeLists.txt`는 CMake를 사용하여 프로젝트를 빌드하는 방법을 지정합니다.

이 프로젝트에 대한 질문이나 피드백이 있으면 언제든지 문의해 주세요.
