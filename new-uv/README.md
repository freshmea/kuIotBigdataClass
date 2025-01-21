# uv-project-test

이 프로젝트는 pygame 라이브러리를 사용하여 간단한 지렁이 게임을 구현합니다.

## 설치 방법

1. `uv`를 설치합니다.

    ```bash
    pip install uv
    ```

2. 프로젝트 디렉토리로 이동하여 필요한 라이브러리를 설치합니다.

    ```bash
    cd /home/aa/kuIotBigdataClass/uv-project-test
    pip install -r requirements.txt
    ```

## 실행 방법

1. `uv` 명령어를 사용하여 프로젝트를 실행합니다.

    ```bash
    uv run
    ```

## 파일 구조

```bash
uv-project-test
├── uv.yml
├── src
│   └── main.py
├── tests
│   └── test_main.py
└── requirements.txt
```

## 주요 파일 설명

- `uv.yml`: 프로젝트 설정 파일입니다.
- `src/main.py`: 게임의 진입점이 되는 파일입니다.
- `requirements.txt`: 프로젝트에 필요한 라이브러리 목록입니다.
- `tests/test_main.py`: 테스트 코드가 포함된 파일입니다.

## 게임 설명

이 게임은 간단한 지렁이 게임으로, pygame 라이브러리를 사용하여 구현되었습니다. 게임 화면은 검은색 배경으로 설정되어 있으며, 기본적인 게임 루프가 포함되어 있습니다.
