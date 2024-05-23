# kuIotBigdataClass

C/C++ database arduino raspberrypi Iot clas.....

---

## 2024-02-22

---

- 권한 설정

```text
sudo 권한 추가하는법
1. 터미널 열기 (Ctrl + Alt + T)
2. "su -" 치기 (큰 따옴표 제외)
3. 자신의 ubuntu 로그인 비밀번호 입력하기
4. 터미널 좌측 상단에, "root@bunt22:~#" 확인하기
5. 아래 링크에서, sudoers 파일에, ubuntu 사용자 이름 추가하기
   https://projooni.tistory.com/entry/%EB%A6%AC%EB%88%85%EC%8A%A4ubuntu%EC%97%90%EC%84%9C-sudoers-%EC%88%98%EC%A0%95%ED%95%B4%EC%84%9C-sudo-%EA%B6%8C%ED%95%9C-%EB%B6%80%EC%97%AC%ED%95%98%EA%B8%B0
```

- instruction.
- google slide share.
- gitHub sign up.
- gitHub create repository.
- ubuntu hangul setting.
- VsCode install
- git install

```shell
sudo apt-get install git
git clone https://github.com/freshmea/kuIotBigdataClass.git
```

- sql workbench install - windows
- MySQL DBMS install - windows
- sql workbench install - ubuntu
- MySQL DBMS install - ubuntu
- vscode mysql extension install
- Chapter01 데이터베이스 개론
- Chapter03 SQL 기초
  - 데이터베이스 만들기 create database;
  - 데이터베이스에 테이블 만들기 3개 (book, orders, customer)
  - 데이터베이스에 데이터 넣기 insert into ... values(...);
  - 유저 만들어서 권한 설정 하기;
    - grant all privileges on *.* to 'root'@'localhost' identified by '1234';
  - winddows cli 에서 testDB 생성하기

- 과제
  - MD 포스트 읽어 보기:
    [링크](https://www.heropy.dev/p/B74sNE)
  - 영상 시청 git:
    [링크](https://www.youtube.com/watch?v=YFNQwo7iTNc)
    [링크](https://www.youtube.com/watch?v=1I3hMwQU6GU&t=5618s)

---

## 2024-02-23

---

- mysql ubuntu 문제 해결
- user 를 새로 만들어서 권한을 주어 봤지만 해결되지 않음.
- 권한 설정 및 user create 시
  - `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '0000';` 명령어 사용
  - 새로운 유저를 만들때 mysql_native_password 를 사용하도록 설정
- 우분투 myworkbench 에서 코드를 작성하고 vscode 에서 git에 연동.
  - 추가한 파일:
    - create_database.sql
    - create_table.sql
    - insert_data.sql
    - create_user.sql
    - select1.sql
  - 3장 내용 추가
    - 셀렉트 쓰는 방법
  - 2장 데이터베이스 모델 진행.
  - 3장 group by 165p 까지 진행.
  - 윈도우 DBMS 를 우분투에서 연결.
    - 윈도우 DBMS 에 외부 IP 접근 가능한 user 생성.
    - 윈도우 방화벽에 3306 포트 열기.
    - 윈도우 DBMS 에 임이의 데이터 넣고 우분투에서 확인.
  - 우분투 DBMS 를 윈도우에서 연결.
    - 우분투 DBMS 에 외부 IP 접근 가능한 user 생성.
    - 우분투 방화벽에 전체 포트 열기.
    - 우분투 DBMS 에 임이의 데이터 넣고 윈도우에서 확인.
      - vertualbox 프로그램에서는 windows로 가는 ping 이 되지 않음.(학생들이 직접 확인 하지 못함)
      - VMware 프로그램에서는 windows로 가는 ping 이 잘 됨.(프로젝트 화면으로 보여만 줌)

- 과제
  - 프로그래머스 C 언어:
    - 3문제 풀기.
  - 프로그래머스 SQL 언어:
    - 0 문제 풀기.
  - 영상 과제:
    - [링크](https://www.youtube.com/watch?v=K9L9YZhEjC0)
    - [링크](https://www.youtube.com/watch?v=Xp1IKwJfDAA)

---

## 2024-02-29

---

- 빌드 과정 설명
  - make cmake for linux
  - 전처리 어셈블리 바이너리 링크
- make 실습
  - 기본 문법
  - 여러개 명령어 등록
  - 연속 실행
  - 생략 가능 명령어
  - 변수 사용
- 3장 끝까지 진행
  - DML
    - select
      - where, group by, having, order by
  - DDL
    - create, alter, drop
  - DCL
    - insert, update, delete
- 4장 내장함수
  - SQL 내장함수
    - 숫자함수
      - abs, ceil, floor, round, sign...
    - 문자열 함수
      - concat, replace, substr, length...
    - 날짜 함수
      - str_to_date, date_format, adddate, sysdate...
      - format 형식 %Y-%m-%d %H:%i:%s ...
- 과제
  - 프로그래머스 C 언어:
    - 3문제 풀기.
  - 프로그래머스 SQL 언어:
    - ‘인기 있는 아이스크림’
    - ‘3월에 태어난 여성 회원 목록’
    - ‘조건에 맞는 도서 리스트’
    - ‘흉부 외과 또는 일반외과’
  - 영상 과제:
  - 포스팅 과제:
    - [링크](https://www.tuwlab.com/ece/27193)

---

## 2024-03-7

---

- mysql 내장 함수
  - null ifnull
- 외래키 확인 및 삭제 방법

```sql
set sql_safe_updates=0;
-- 무시하고 삭제
SET foreign_key_checks = 0;
delete from Customer;
SET foreign_key_checks = 1;

-- 제약 조건 확인
select * from information_schema.table_constraints where table_name = 'Orders';

-- 확인된 제약 조건으로 외래키 삭제
alter table Orders drop foreign key Orders_ibfk_2;
```

- 부속질의
  - select 부속질의 (스칼라 부속질의)
  - from 부속질의 ( 인라인 뷰)
  - where 부속질의
    - 단일 - 비교 ( =, >, <, >=, <=, !=, <>, is null, is not null) [비교]
    - 다수의 열, 단일 행 ( all, some, any) [한정]
    - 다수의 행, 다수의 열 (in, not in, exists, not exists)
- 뷰
  - 뷰 생성 - create view 뷰이름 as select ...
  - 뷰 삭제 - drop view 뷰이름
  - 뷰 수정 - create or replace view 뷰이름 as select ...
- 인덱스
  - 인덱스 생성 - create index 인덱스이름 on 테이블이름(열이름)
  - 인덱스 삭제 - drop index 인덱스이름 on 테이블이름
  - 인덱스 재구성 - analyze table 테이블이름

- 저장 프로그램
  - procedure
    - call procedure이름(인수)
  - trigger
    - before, after (insert, update, delete)
  - function (사용자 정의)
- 파이썬 프로그램 ( pymysql 라이브러리 활용)
- C 프로그램 ( C API mysql.h 라이브러리 활용)
  - 컴파일 설정 `cc -o booklist booklist.c -lmysqlclient -I/usr/include/mysql -L/usr/lib/x86_64-linux-gnu`
- 과제
  - 프로그래머스 C 언어:
    3문제 풀기.

---

## 2024-03-8

---

- C 프로그램 ( C API mysql.h 라이브러리 활용)
  - C Api documentation
    - [링크](https://dev.mysql.com/doc/c-api/en/)

```c
#include <stdio.h>
#include <mysql.h>
#include <string.h>
// sudo apt install libmysql++*
int main(){
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;
    char *host = "localhost";
    char *user = "root";
    char *passwd = "0000";
    char *db = "madangdb";
    char query[255];
    int port = 3306;

    strcpy(query, "select * from Book");

    conn = mysql_init(NULL);
    if(mysql_real_connect(conn, host, user, passwd, db, port, NULL, 0)){
        printf("MySQL 연결 성공\n");
    }else{
        printf("MySQL 연결 실패\n");
    }

    if(mysql_query(conn, query)){
        printf("쿼리 실패\n");
    }

    res = mysql_store_result(conn);
    while(row = mysql_fetch_row(res)){
        printf("%s\t", row[0]);
        printf("%s\t", row[1]);
        printf("%s\t", row[2]);
        printf("%s\t\n", row[3]);
    }
    mysql_close(conn);
    return 0;
}

```

- CMake
  - 설치 sudo apt-get install cmake
  - 실습
    - CMakeLists.txt 작성
    - mkdir build && cd build
    - cmake ..
    - make
    - ./실행파일
- VsCode 디버깅 설정
- flask
  - 설치 sudo apt-get install python3-flask, pip3 install flask
  - 실습
    - app.py 작성
    - python3 app.py
    - 브라우저에서 localhost:5000 접속
- 정규화 설명
  - 1NF 정규화
    - 원자성을 가지는 데이터베이스 테이블을 만드는 것
  - 2NF 정규화
    - 불완전 함수 종송석을 제거 하는 데이터베이스 테이블을 만드는 것
  - 3NF 정규화
    - 이행적 종속성을 제거 하는 데이터베이스 테이블을 만드는 것
  - BCNF 정규화
    - 후보키에 의존하는 결정자를 제거 하는 데이터베이스 테이블을 만드는 것
  - 4NF 정규화
    - 생략
  - 5NF 정규화
    - 생략
- 트랜젝션
  - 트랜젝션의 특성
    - 원자성
    - 일관성
    - 독립성
    - 지속성
  - 락
    - 공유락
    - 배타락
  - 데드락
    - 데드락 발생 조건
- 과제
  - 프로그래머스 C 언어:
    - 문제 풀기.3
  - 영상과제:
    - [링크](https://www.youtube.com/watch?v=ZVuHZ2Fjkl4)
    - [링크2](https://www.youtube.com/watch?v=Y1FbowQRcmI)
  - 포스팅 과제:
    - [링크](https://www.tuwlab.com/ece/27234)
    - [링크2](https://gist.github.com/luncliff/6e2d4eb7ca29a0afd5b592f72b80cb5c?permalink_comment_id=3345588)
  - C api 둘러보기 :
    - [링크](https://dev.mysql.com/doc/c-api/8.0/en/mysql-real-connect.html)

---

2024_3_19

---

- c_game_project 시작
  - git repository 생성
  - .gitignore 생성
  - doxygen 세팅
    - sudo apt install doxygen graphviz
    - sudo apt install doxygen-gui
    - sudo apt install qt5
    - unset GTK_PATH
- cmake 배포 설정
  - install 명령어 사용
  - cpack 설정
- tetris 게임 설계
  - signal 60Hz 로 update 함수가 실행되게 만듬.
  - getch 함수로 실시간 키보드 입력.
  - 게임판
  - 블록
  - 블록 회전
  - 블록 이동
  - 블록 떨어짐
  - 블록 삭제
  - 블록 생성
  - 게임 오버

---

## 2024_5_03

---

- OpenCV 설치
- sudo apt install libopencv-dev python3-opencv
- cmake 설정
  - glob file 적용하기
- 영상처리 영상인식 기본 개념
- 모던 C++ 기초 문법
  - auto
  - lambda
  - range for
  - smart pointer
- 기본 클래스
  - Point 클래스
  - Size 클래스
  - Rect 클래스
  - Scalar 클래스
  - Mat 클래스
    - 얕은 복사 -대입 연산
    - 깊은 복사 -clone, copyTo
  - Vec 클래스
- 영상 입출력
  - imread
  - imshow
  - imwrite
- 동영상 입출력
  - VideoCapture
  - VideoWriter
- 직선 그리기
  - line 함수
  - 움직이는 line 함수 그리기

---

## 2024_5_7

---

- drawing
  - circle
  - rectangle
  - ellipse
- text
  - putText
  - freeStyle 한글 폰트 가능
- mouse
  - mouse callback 함수 사용
- keyboard
  - 키보드 입력 받기
- tickMeter
  - 시간 측정
  - frame 일정하게 만들기 최적화
- trackbar
  - trackbar Callback 함수 사용
- 4장 마지막 예제
  - 마우스 따라다니는 사각형 + BGR 정보 얻기 + 파일 저장
- 영상 밝기 조절
  - saturated cast 예제

---

## 2024_5_8

---

- 영상 밝기 조절
  - 트랙바 적용
- 영상 대비 조절
  - 단순 곱하기
  - 중간 영역 확장
  - 히스토그램 스트레칭
  - 히스토그램 평활화
- 영상의 산술 연산
  - add, addWeighted, subtract, absdiff
- 비트연산
  - bitwise_and, bitwise_or, bitwise_xor, bitwise_not
- Covolution 회선
  - 기본 개념
  - 가장자리 연산
  - filter2D
- 블러링
  - blur, GaussianBlur, medianBlur, bilateralFilter
- 샤프닝
  - 블러와 원본의 조합으로 샤프닝
- 노이즈 생성
  - 가우시안 노이즈
  - 소금-후추 노이즈 미디안 필터로 없애기
- 기하학적 변환 affine, perspective
  - 기본 개념
  - 이동 변환, 전단 변환, 회전 변환, 크기 변환
  - warpAffine, getAffineTransform
  - getRotationMatrix2D
  - warpPerspective, getPerspectiveTransform
- 미분 필터
  - 소벨 마스크
- 엣지
  - 캐니엣지

---

## 2024_5_21

---

- python 설치
  - linux 시스템에서는 기본적으로 설치가 되어 있다.
    - python3 --version
    - python -V
  - 파이썬 언어의 특징
    - 인터프리터 언어
    - 동적 타입 언어
    - 객체 지향 언어
    - 플랫폼 독립적 언어
  - 개발환경 설치
    - 가상환경 설치
      - virtualenv 설치 pip 와 같이 운용
      - miniconda 설치

      ```shell
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
      bash Miniconda3-latest-Linux-x86_64.sh
      cd miniconda3/bin
      ./conda config --set auto_activate_base false
      ./conda init
      source ~/.bashrc
      ```

      - Vscode 설정
        - VsCode 에서 가상환경 사용하기
    - 패키지 관리
      - 패키지가 설치되는 폴더
        - 패키지 설치 확인
          - pip list -v
          - conda list
          - pip show 패키지이름
        - 가상환경의 패키지 내보내기
          - pip freeze > requirements.txt
          - conda list --export > requirements.txt
        - 가상환경의 패키지 파일로 설치하기
          - pip install -r requirements.txt
          - conda install --file requirements.txt

- 파이썬 변수
  - 파이썬의 변수는 모두 클래스의 객체이다.
  - 파이썬의 기본 타입은 없다. 모두 클래스이다.
  - 파이썬의 클래스는 모두 object 클래스를 상속받는다.
  - 파이썬의 변수는 Heap 에 의해 동적으로 관리되고 GC garbage collection 이 된다.
- 파이썬의 연산자
  - C/C++ 과 다른 점
    - 나누기 연산자 / 는 정수와 실수를 구분하지 않는다.
    - 나머지 연산자 % 는 정수와 실수를 구분하지 않는다.
    - 제곱승 연산자 ** 를 사용한다.
    - 나누기 연산자 // 는 정수 나누기 연산자이다.
    - 비트 연산자는 사용하지 않는다.
    - 논리 연산자는 and, or, not 을 사용한다.
    - 증감연산자는 사용하지 않는다.
  - 자료형 확인
    - type 함수를 사용한다.
    - isinstance 함수를 사용한다.
    - id 함수를 사용한다.
    - isSubclass 함수를 사용한다.
- 화면 입출력
  - 화면 출력
    - print 함수를 사용한다.
    - f-string 을 사용한다.
    - format 함수를 사용한다.
    - sep, end, flush 를 사용한다.
  - 표준 입력 함수
    - input 함수를 사용한다.
    - 리턴 값은 str 이다.
  - 화씨 온도 변환기
    - 에러 처리 추가
- 리스트
  - 인덱싱과 슬라이싱
  - 리버스 인덱싱
  - 리스트 메소드
    - append, extend, insert, remove, pop, index, count, sort, reverse
    - 리스트 복사
      - 얕은 복사
      - 깊은 복사
  - 패킹과 언패킹
  - 이차원 리스트
  - 리스트의 메모리 관리 방식
- 조건문
  - if, elif, else
  - True, False
  - 삼항 연산자

---

## 2024_5_22

---

- 반복문
  - for ~ in ~:
  - for ~ in range():
  - while ~ :
  - break, continue
    - 구구단 프로그램
    - 진수 변환 프로그램
    - 숫자 찾기 프로그램
    - 평균 구하기 프로그램
- 함수
  - def 함수명(매개변수)
  - 매개변수 종류
    - 위치 매개변수
    - 키워드 매개변수
    - 디폴트 매개변수
    - 가변 매개변수 - 튜플의 형태로 넘어 간다.
    - 키워드 가변 매개변수 - 딕션너리의 형태로 넘어 간다.
  - 함수의 리턴 값 : 여러개를 리턴 하면 튜플로 전달
  - 함수 호출 방식
    - 기본적으로 모두 call by value 이다.
    - list 를 쓰면 call by referece 처럼 사용 가능하다.
  - 변수의 사용 범위
    - 지역 변수
    - 전역 변수 global 키워드
  - 람다 함수
    - lambda 매개변수 : 리턴값
    - map, filter, reduce
    - 함수의 인자로 함수를 넘길때 사용
  - 제너레이터
    - yield 키워드 사용
    - next 함수 사용
    - for ~ in ~ 사용
    - 제너레이터 표현식
  - 데코레이터
    - 함수를 감싸는 함수
    - 함수의 시작과 끝을 감싸는 함수
    - 함수의 인자를 검사하는 함수
    - 함수의 리턴값을 검사하는 함수
    - 함수의 실행시간을 측정하는 함수
- 문자열
  - 파이썬의 문자열은 클래스의 객체로서 시퀀스 자료형이다.
  - 문자열의 인덱싱과 슬라이싱
  - 문자열의 메소드
    - upper, lower, title, capitalize, swapcase
    - strip, lstrip, rstrip
    - split, join
    - replace, find, index, count
    - startswith, endswith
    - isalpha, isdigit, isalnum, isspace
  - 문자열 포맷팅
    - % 연산자
    - format 함수
    - f-string
    - 패딩 처리
  - 단어카운팅 프로그램
- 코딩 테스트 연습(프로그래머스-파이썬3)
  - 꼬리 문자열
  - 정수 찾기
  - 부분 문자열인지 확인하기
  - 부분 문자열
  - 0 떼기

---

## 2024_5_23

---

- 자료구조
  - 스택, 큐 구현 : 리스트로 구현할 수 있음
  - 튜플 - 메소드가 리스트와 거의 같음
  - 세트
    - add , remove, update, discard, pop, clear
    - 중복을 허용하지 않는다.
    - 순서가 없다.
    - 집합 연산이 가능하다.
      - 합집합, 교집합, 차집합
      - union, intersection, difference, -, &, |
  - 딕션너리
    - key, value 쌍으로 이루어진 자료형
    - key 는 중복이 되지 않는다.
    - value 는 중복이 되어도 상관없다.
    - key 는 변경이 되지 않는다.
    - value 는 변경이 가능하다.
    - 딕션너리 메소드
      - get, items, keys, values, pop, popitem, update
  - collections 모듈
    - deque
      - rotate, reverse, extend, appendleft, popleft
    - defaultdict
      - 새로운 키값에 접근하면 디폴트 값을 반환
    - OrderedDict
      - sorted 함수를 사용하여 정렬된 딕션너리를 만들 수 있다.
    - Counter
      - 갯수를 세어주는 딕션너리를 만들 수 있다.
    - namedtuple
      - 이름을 가진 튜플을 만들 수 있다.
      - C 언어의 구조체와 비슷하다.
    - 텍스트 마이닝 프로그램
- 파이썬 스타일 코드
  - split, join
  - list comprehension
    - [i for i in range(10) if ~]
    - [i if ~ else ~ for i in range(10)]
  - enumerate, zip
    - enumerate 는 인덱스를 같이 반환
    - zip 은 같은 인덱스의 값을 튜플로 묶어서 반환
  - lambda
    - 함수를 간단하게 만들어 준다.
  - map, filter, reduce
    - map 은 리스트의 요소를 지정된 함수로 처리
    - filter 는 리스트의 요소를 지정된 함수로 걸러낸다.
    - reduce 는 리스트의 요소를 누적으로 처리한다.
