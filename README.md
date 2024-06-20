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
- 객체 지향 프로그래밍
  - 클래스와 객체
    - 클래스는 객체를 만들기 위한 틀
    - 객체는 클래스를 이용하여 만들어진 것
  - 클래스 선언
    - class 클래스이름:
    - __init__ 함수
    - self 키워드
    - 노트북 프로그램 만들기
    - 상속
    - 다형성
      - 인터페이스
    - 가시성
      - __변수 : private
      - @property

---

## 2024_5_24

---

- 모듈과 패키지
  - 모듈
    - 파이썬 파일
    - import 모듈이름
    - from 모듈이름 import 함수이름
    - import 모듈이름 as 별칭
    - __name__ 변수
  - 패키지
    - 모듈을 모아놓은 디렉토리
    - __init__.py 파일
    - __all__ 변수
    - from 패키지이름 import 모듈이름
    - from 패키지이름.모듈이름 import 함수이름
    - from 패키지이름.모듈이름 import *
  - 패키지 만들기
    - roboadvisor 패키지 만들기
      - roboadvisor 디렉토리 만들기
      - __init__.py 파일 만들기
    - sub 패키지 만들기
      - crawling 디렉토리 만들기
      - __init__.py 파일 만들기
      - database 디렉토리 만들기
      - __init__.py 파일 만들기
      - analysis 디렉토리 만들기
      - __init__.py 파일 만들기
    - 메타 데이터 넣기
      - __init__.py 파일에 __version__ 변수 추가
    - 패키지 네임스페이스 설정
- 예외 처리와 파일 다루기
  - 예외 처리
    - try, except, else, finally
    - raise
    - assert
    - Exception 클래스
      - 상속 받아서 사용자 정의 예외 처리
  - 파일 다루기
    - open, close
    - read, write
    - readline, readlines
    - with
      - close 없이 파일을 다루기
    - pickle
      - 객체를 바로 저장 가능, 여러개의 객체도 저장 가능
- 로그 관리
  - logging
    - 로그 레벨
    - 로그 포맷
    - 로그 파일
    - 로그 핸들러
    - 로그 필터
    - 로그 포맷터
  - logging 환경 변수 설정 및 이용
    - 환경 변수 설정
    - configparser
    - argparse
    - logging.config
    - logging.config.fileConfig
- 웹 스크래핑
  - HTML 파싱
    - 정규 표현식
- xml 과 json
  - xml
    - BeautifulSoup
  - json
  - csv

---

## 2024-05-27 월

---

- 데이터 과학을 위한 통계

  - 1.1 정형 데이터의 종류
    - 수치형 데이터
      - 연속형 데이터: 일정 범위의 값
      - 이산 데이터: 정수만 취할 수 있는 데이터
    - 범주형 데이터
      - 이진 데이터: 값이 2개인 데이터(남/여, 참/거짓, 0/1)
      - 순서형 데이터: 수치 사이에 순위가 있는 데이터(성적)

- 1.2 테이블 데이터(데이터 분석에서 가장 대표적으로 사용되는 객체의 형태)
  - 데이터 프레임: 통계와 머신러닝 모델에서 가장 기본이 되는 테이블 형태의 데이터 구조
  - 피처(feature): SQL에서의 컬럼
  - 결과(outcome): 실험이나 연구에서 결과를 예측하기 위해 피처 사용
  - 레코드(record): 일반적으로 테이블의 각 행은 하나의 레코드
  - 테이블 형식이 아닌 데이터구조: 테이블 데이터로 변환 후 쓴다

  - 1.3 위치추정
    - 평균(mean/average)
    - 절사평균: 양 끝에서 일정 개수의 값을 삭제한 후 평균을 구한다.
    - 가중평균: 센서와 관련. 부정확한 센서는 가중값을 높게 준다. 데이터 수집 시 대조군이 항상 똑같은 수가 얻어지지는 않기 때문에, 가중값을 줘서 두 집단의 영향력을 비슷하게 맞출때 가중평균을 쓴다.
    - 중간값: 데이터를 일렬로 정렬했을 때, 한가운데에 위치하는 값.
    - 가중 중간값: //
    - 로버스트: //

    - 1.3.3_meanWeight.py [위치추정: 평균,절사평균,중간값,가중평균,가중중간값](python/pythonData/1.3.3_meanWeight.py)

  - 1.4 변이(variability)추정
    - 편차: 관측값과 위치 추정값 사이의 차이
      - 평균을 기준으로 편차의 합은 항상 0
      - 평균 절대 편차: 편차의 절대값의 평균
    - 분산: //
    - 표준편차: 분산에 제곱근을 한 값
    - 중위 절대 편차(MAD): 로버스트한 변이 추정값. 중간값과의 편차를 구하고, 그 값들의 절대값에 대한 중간값
    - 백분위수: //
      - 사분위범위(IQR): //

    - 1.4.3_deviation.py [변이추정: 표준편차,사분위범위(IQR), 중위절대편차(MAD)](python/pythonData/1.4.3_deviation.py)

  - 1.5 데이터 분포 탐색
    - boxplot(상자그림)
    - 도수분포표(frequency table)
    - 히스토그램(histogram)
    - 밀도그림(density plot)

    - 1.4.3_deviation.py [boxplot](python/pythonData/1.4.3_deviation.py)

    - 1.5.2_histogramTest.py [도수분포표와 히스토그램](python/pythonData/1.5.2_histogramTest.py)

  - 1.6 이진 데이터와 범주 데이터 탐색
    - 최빈값(mode)
    - 기댓값(expected value): 범주에 해당하는 어떤 수치가 있을때, 범주의 출현 확률에 따른 평균
    - 막대도표(bar chart)
    - 파이그림(pie chart)

    - p47_categoryDate.py [이진데이터 막대도표로 표현](python/pythonData/p47_categoryDate.py)

  - 1.7 상관관계
    - 상관계수
    - 상관행렬
    - 산점도(scatterplot)

    - p52_correlation.py [상관관계](python/pythonData/p52_correlation.py)

- numpy
  - numpyArray.py [numpy 실습](python/pythonData/numpyTest/numpyArray.py)

  - numpyMethod.py [reshape, flatten](python/pythonData/numpyTest/numpyMethod.py)

  - numpyIndexing.py [indexing, slicing](python/pythonData/numpyTest/numpyIndexing.py)

  - numpyConstruction.py [배열생성함수: ones(),zeros(),empty(), 통계분석함수](python/pythonData/numpyTest/numpyConstruction.py)

  - numpySum.py [연산함수: arange()](python/pythonData/numpyTest/numpySum.py)

  - numpyStack.py [연결함수](python/pythonData/numpyTest/numpyStack.py)

  - numpyDot.py [행렬연산](python/pythonData/numpyTest/numpyDot.py)

  - numpyBroadcasting.py [브로드캐스팅 연산](python/pythonData/numpyTest/numpyBroadcasting.py)

- 정리
  - 통계를 왜 배우는가 -> 빅데이터
  - 대표값: 평균, 중간값, 가중평균, 절사평균
            분산, 편차, 절대편차, 표준편차(분산에 루트씌운것), 백분위와 IQR
  - 이러한 값들을 가지고 그래프를 그림 (데이터 분포 탐색)
    - 수치 데이터 -> 히스토그램 x-y, box plot
    - 이산데이터, 범주데이터 -> 히스토그램
  - 상관관계 corr -> -1 ~ 1, heatmap으로 표현
  - numpy: []리스트가 기본 타입이지만, 약점이 있었다. c-type array사용.
    - 선언: ones(), zeros(), empty()등
    - 메소드: reshape (주의사항: 원소의 개수를 맞춰야한다)
    - 사칙연산
    - dot
    - broadcasting: 증식하여 행렬이 맞춰져 연산됨(논리적으로 증식이 가능할 것 같은 경우에만)

---

## 2024-05-28 화

---

- numpy
  - 비교 연산
    - numpyBoolIndex.py [비교연산, 비교연산함수, 인덱스 반환함수, 정렬된 값의 인덱스를 반환하는 함수(argsort,argmax,argmin)](python/pythonData/numpyTest/numpyBoolIndex.py)

    - numpyFancyIndex.py [인덱스를 활용한 데이터 추출: boolean index, fancy index](python/pythonData/numpyTest/numpyFancyIndex.py)

- pandas
  - python계의 엑셀
  - 시리즈(series): 컬럼이 1개인 데이터프레임
  - 시리즈를 여러개 모아놓으면 데이터프레임(데이터 테이블 전체를 포함하는 객체)
  - pandasSeries.py [Series 객체 생성, 이름변경](python/pythonData/pandasTest/pandasSeries.py)

  - pandas는 컬럼별로 타입을 다르게 지정할 수 있다.

  - 객체 생성
    - pandasDataFrame.py [데이터프레임 생성](python/pythonData/pandasTest/pandasDataFrame.py)

  - 데이터 추출
    - pandasExcel.py [엑셀 파일에서 데이터 추출](python/pythonData/pandasTest/pandasExcel.py)

  - 그룹별 집계
    - pandasGroup.py [그룹별 집계](python/pythonData/pandasTest/pandasGroup.py)

    - 그룹화된 상태에서(grouped)
    - pandasGroup2.py [그룹화된 상태_집계, 변환, 필터](python/pythonData/pandasTest/pandasGroup2.py)

  - 병합과 연결
    - pandasJoin.py [병합, 연결](python/pythonData/pandasTest/pandasJoin.py)

    - pandasConcat.py [](python/pythonData/pandasTest/pandasConcat.py)

- matplotlib
  - pyplotTest.py [](python/pythonData/visualTest/pyplotTest.py)
  - pyplotSubplot.py [](python/pythonData/visualTest/pyplotSubplot.py)
  - pyplotSubplot2.py [](python/pythonData/visualTest/pyplotSubplot2.py)
  - pyplotCustomizing.py [](python/pythonData/visualTest/pyplotCustomizing.py)
  - 산점도
    - pyplotGraph [산점도](python/pythonData/visualTest/pyplotGraph.py)
  - pyplotBar [막대그래프](python/pythonData/visualTest/pyplotBar.py)

- seaborn
  - seabornLinePlot.py [시본의 기본 그래프](python/pythonData/visualTest/seabornLinePlot.py)
  - seabornLinePlot.ipynb [Jupyter](python/pythonData/visualTest/seabornLinePlot.ipynb)

---

## 2024-05-29 수

---

- 플롯리(plotly)
  - plotlyTest.ipynb [플롯리](python/pythonData/visualTest/plotlyTest.ipynb)

- 데이터 과학을 위한 통계

  - 탐색적 데이터 분석

    - p52_correlation.py [전에 부족했던 부분 추가](python/pythonData/p52_correlation.py)

    - scatterTelecom.py [산점도그리기](python/pythonData/scatterTelecom.py)

    - multivariatePlot.py [육각형 구간과 등고선](python/pythonData/multivariatePlot.py)

    - categoryPlot.py [범주형 변수 대 범주형 변수, 범주형 변수 대 수치형 변수, 바이올린 도표, 다변수 시각화](python/pythonData/categoryPlot.py)

  - 데이터와 표본분포
    - 임의 표본 추출: 대상이 되는 모집단 내의 선택 가능한 원소들을 무작위로 추출하는 과정, 원칙 지키는 것 중요.
      계층(stratum): 공통된 특징을 가진 모집단의 동종 하위 그룹
      표본편향(sample bias): 모집단을 잘못 대표하는 표본
    - 편향 -> 통계적 편향은 계통적인(systematic) 오차를 의미한다.
    - 임의의 표본 추출이 정확하게 이루어져야 한다.
    - 선택편향: 관측 데이터를 선택하는 방식 때문에 생기는 편향
      데이터 스누핑: 뭔가 흥미로운 것을 찾아 광범위하게 데이터를 살피는 것
    - 평균으로의 회귀(regression to the mean)
      - ...
    - 중심 극한 정리(central limit theorem)
      - ...
    - 표준오차
      - 표본 값들의 표준편차s와 표본크기 n을 기반으로 한 통계량을 이용하여 추정
    - 부트스트랩
      - resampleTest.py [부트스트랩](python/pythonData/resampleTest.py)

    - 정규분포
      - qqgraph.py [표준정규분포](python/pythonData/qqgraph.py)

    - 긴꼬리분포
      - qqBlackSwan.py [긴꼬리분포](python/pythonData/qqBlackSwan.py)

    - T 분포
    - 이항분포
      - 이항식: 두 가지 결과를 갖는다.
        이항시행: 두 가지 결과를 가져오는 시행
        이항분포: n번의 시행에서 성공한 횟수에 대한 분포
      - binormTest.py [이항분포](python/pythonData/binormTest.py)
    - 카이제곱분포
    - F 분포
    - 푸아송 분포

---

## 2024-05-30 목

---

- orange
  - 머신러닝: 지도학습[target]
    - f(x, y) = ax + by + c

- 데이터 과학을 위한 통계

  - 통계적 실험과 유의성 검정
    - permuteSample.py [재표본추출.순열검정(웹사이트 정보)](python/pythonData/permuteSample.py)

    - permuteSample2.py [통계적유의성과 p값.순열검정](python/pythonData/permuteSample2.py)

    - pValue.py [p-value](python/pythonData/pValue.py)
    - tTest [t-test](python/pythonData/tTest.py)

    - 분산 분석(analysis of variance, ANOVA)
      - anovaTest.py [anova](python/pythonData/anovaTest.py)

    - fStatistics.py [f-statistic](python/pythonData/fStatistics.py)
    - chi2Statistics.py [chi2Statistics](python/pythonData/chi2Statistics.py)
    - effectiveSize.py [effectiveSize](python/pythonData/effectiveSize.py)

  - 회귀와 예측 (머신러닝과 직접관련)
    - 지도학습 (target이 있는 학습)
      비 지도학습 (target이 없는 학습)

    - 단순 선형 회귀
      - 응답변수(y값): 예측하고자 하는 변수
        독립변수(x값): 응답치를 예측하기 위해 사용되는 변수
        레코드: 한 특정 경우에 대한 입력과 출력을 담고 있는 벡터
      - linearRegresstionTest.py [](python/pythonData/linearRegresstionTest.py)
    - 다중 선형 회귀
      - multiLinearReg.py [다중선형회귀 예제](python/pythonData/multiLinearReg.py)

---

## 2024-05-31 금

---

- 빅데이터 -> IoT기기에서 센서설정을 먼저 해야함 -> data생성 -> MySQL에 저장(database에 저장) -> 분석 및 분석한 데이터로 의미있는 결과, 모델을 뽑아냄 -> 머신러닝으로 모델을 훈련, 예측
- 그래프 ( plt(matplot), sns(seaborn) )
- 기본 데이터 다루기( numpy(속도가 빠름), pandas(파이썬의 엑셀, 행과 열로 이루어진 2차원 데이터를 column, row를 이용해서 다룸)(Series, DataFrame) )
- 데이터의 분류
  - 수치형: 숫자, linear모델(linear regression)도 잘 작동함
  - 범주형: 범주형은 수치형으로 바꿀 수 있음.
- 모집단과 샘플

- chapter 4
  - y = f(x)에 대해
    - 수치형은 y값 자체가 중요
    - 범주형은 2차원 그래프에 그려진 선에서 위쪽인지 아래쪽인지가 중요
  - train(fit)

- 4장 회귀와 예측
  - subsetRegresstion.py [subsetRegression](python/pythonData/subsetRegresstion.py)
  - weightRegre [weightRegre](python/pythonData/weightRegre.py)
  - 회귀에서의 factor variable
  - 다수의 수준을 갖는 요인변수들
    - manyLevelStep.py [manyLevelStep](python/pythonData/manyLevelStep.py)

  - 회귀진단
    - 특잇값(outlier)
    - outlierAnalysis.py [outlierAnalysis](python/pythonData/cooksDistance.py)
  - cooksDistance.py [cookDistance](python/pythonData/cooksDistance.py)
  - heteroskedasticity.py [heteroskedasticiy](python/pythonData/heteroskedasticity.py)
  - partialResidualPlot.py [partialResidualPlot](python/pythonData/partialResidualPlot.py)
  - polynomialRegression.py [polynomialRegression](python/pythonData/polynomialRegression.py)

- 5장 분류
  - 나이브 베이즈(naive Bayes): 나이브 베이즈 알고리즘은 주어진 결과에 대해 예측변숫값을 관찰할 확률을 사용하여, 예측변수가 주어졌을 때, 결과 Y = i를 관찰할 확률, 즉 정말 관심있는 것을 추정한다.
  - naiveBayes [naiveBayes](python/pythonData/naiveBayes.py)
  - descriminantAnalysis.py [descriminantAnalysis](python/pythonData/descriminantAnalysis.py)

---

## 2024-06-03 월

---

- 복습
  - 지도학습
    - 회귀(Regression)
    - 분류(Classification): 나이브 베이즈, 판별분석
  - 비지도학습: target이 없음

- 데이터 과학을 위한 통계
  - chapter5 분류
    - 로지스틱 회귀
      - logisticRegression.py [로지스틱 회귀](python/pythonData/logisticRegression.py)
      - assessingModel.py [모델 평가하기](python/pythonData/assessingModel.py)
    - 분류 모델 평가
      - confusionMatrix.py [conf_mat](python/pythonData/confusionMatrix.py)
      - rocCurve.py [rocCurve](python/pythonData/rocCurve.py)
      - aucCurve.py [aucCurve](python/pythonData/aucCurve.py)

  - chapter6 통계적 머신러닝
    - KNN(k-nearest neighbors)
      - 1. 특징들이 가장 유사한 k개의 레코드를 찾는다.
      - 2. 분류: 이 유사한 레코드들 중에 다수가 속한 클래스가 무엇인지 찾은 후에, 새로운 레코드를 그 클래스에 할당한다.
      - 3. 예측(KNN 회귀: KNN regression): 유사한 레코드들의 평균을 찾아서 새로운 레코드에 대한 예측값으로 사용한다.
      - knnTest.py [knnTest](python/pythonData/knnTest.py)
      - knn2Test.py [knn2Test](python/pythonData/knn2Test.py)
      - featureEngineering.py [KNN을 통한 featureEngineering](python/pythonData/featureEngineering.py)
      - datasetTest.py [pytorch폴더 datasetTest](pytorch/datasetTest.py)
      - train_vaild_split.py [train_vaild_split](pytorch/train_valid_split.py)
      - decisionTreeTest.py [decisionTree](pytorch/decisionTreeTest.py)

---

## 2024-06-04 화

---

- 데이터 과학을 위한 통계
  - chapter 6 통계적 머신러닝
    - 6.3 배깅과 랜덤 포레스트
      - 앙상블: 여러 모델의 집합을 이용해서 하나의 예측을 이끌어내는 방식
      - 배깅: 데이터를 부트스트래핑해서 여러 모델을 만드는 일반적인 방법. 배깅은 다양한 모델들을 정확히 같은 데이터에 대해 구하는 대신, 매번 부트스트랩 재표본에 대해 새로운 모델을 만든다.

      - 랜덤 포레스트
        - randomForestTest.py [랜덤 포레스트](python/pythonData/randomForestTest.py)
      - 하이퍼파라미터
        - variableImportance.py [](python/pythonData/variableImportance.py)
        - variableImportance.ipynb [](python/pythonData/variableImportance.ipynb)

      - xgboostTest.py [xgboostTest](python/pythonData/xgboostTest.py)
      - overfitting.ipynb [overfitting](python/pythonData/overfitting.ipynb)

  - chapter 7 비지도 학습
    - 7.1 주성분분석 (PCA)
      - pcaTest.py [pcaTest](python/pythonData/pcaTest.py)
      - pcaTest2.py [pcaTest2](python/pythonData/pcaTest2.py)
      - pcaTest3.py [pca데이터로 범주형도 클러스터링 할 수 있다](python/pythonData/pcaTest3.py)

    - 7.2 k-평균 클러스터링
      - kMeanClustering.py [k-평균 클러스터링](python/pythonData/kMeanClustering.py)

---

## 2024-06-05 수

---

- 데이터 과학을 위한 통계
  - chapter 7 비지도학습
    - 7.2 k-평균 클러스터링
      - kMeanClustering2.py [kMeanClustering2](python/pythonData/kMeanClustering2.py)
      - kMeanClusteringDeterminN.py [kMeanClusteringDeterminN](python/pythonData/kMeanClusteringDeterminN.py)
    - 7.3 계층적 클러스터링
      - hierarchicalClustering.py [계층적 클러스터링](python/pythonData/hierarchicalClustering.py)
    - 7.4 모델 기반 클러스터링
      - normalMixture.py [normalMixture](python/pythonData/normalMixture.py)
    - 7.5 스케일링과 범주형 변수
      - dominantVariable.py [지배 변수](python/pythonData/dominantVariable.py)
      - gowersDistance.py [범주형 데이터와 고워 거리](python/pythonData/gowersDistance.py)
- kaggle에서 titanic_machine learning from disaster 해보기
  - kaggle에서 data 가져와 colab에서 실습

---

## 2024-06-10 월

---

- 머신러닝
  - 데이터 전처리 전략
    - 결측치 처리하기: 드롭과 채우기(drop & fill)
    - 범주형 데이터 처리하기: 원핫인코딩(one-hot encoding)
    - 범주형 데이터로 변환하여 처리하기: 바인딩(binding)
    - 데이터의 크기 맞추기: 피쳐 스케일링(feature scaling)

  - dropProcessing.py [데이터 전처리 드롭](pythonML/dropProcessing.py)
  - fillProcessing.py [데이터 전처리 채우기](pythonML/fillProcessing.py)

  - get_dummiesTest.py [get dummies](pythonML/get_dummiesTest.py)
  - bindingTest.py [binding](pythonML/bindingTest.py)
  - featureScaling.py [feature scaling](pythonML/featureScaling.py)

  - 머신러닝 회귀귀법
    - gradientDescent.py [경사하강법 알고리즘](pythonML/gradientDescent.py)
    - testAndSplit.py [선형회귀 성능측정.훈련/테스트 분할](pythonML/testAndSplit.py)
    - maeRmseR2.py [선형회귀 성능 측정 지표](pythonML/maeRmseR2.py)
    - linearRegressionCustom.py [경사하강법으로 linear regression](pythonML/linearRegressionCustom.py)

---

## 2024-06-11 화

---

- 복습
  - 머신러닝
    - chap6 데이터 전처리
      - 범주 -> 수치형
      - non(결측치) -> pandas의 drop, fill 메소드
      - 이상치 처리를 하면 데이터가 더 정확해진다.
      - 정규화를 해야한다 -> 정규화, z스코어 정규화
    - 회귀이론 ->  y = f(x) f()가 모델, y = w1x + w0 (w1값과 w0값을 구하는게 훈련)

- chap 8 선형회귀의 심화
  - LinearRSGDTest.py [로버스트 확률적 경사 하강법(RSGD)](pythonML/LinearRSGDTest.py)
  - LinearRSGDMain.py [로버스트 확률적 경사 하강법(RSGD)](pythonML/LinearRSGDMain.py)
  - bostonHouseRegression.py [보스턴 하우스 회귀](pythonML/bostonHouseRegression.py)
  - confusionMatrixTest.py [confusion Matrix](pythonML/confusionMatrixTest.py)
  - bindingTest.py [binding Test](pythonML/bindingTest.py)
  - LogisticRegressionTest.py [Logistic Regression](pythonML/LogisticRegressionTest.py)
  - softmaxTest.py [softmax Test](pythonML/softmaxTest.py)
  - mnistClassify.ipynb [mnistClassify](pythonML/mnistClassify.ipynb)

---

## 2024-06-12 수

---

- 복습
  - 선형회귀
    - 1. 방적식 풀기: 최소자승법
      - 빠르다, 중간과정 없음
    - 2. 차근차근 접근: 경사하강법(GD)
      - 국소적으로만 보게되는 단점이 있다 -> 확률적 경사하강법 사용
  - 로지스틱

- chap 11 나이브 베이지안 분류기
  - simpleBayze.py [bayzian](pythonML/simpleBayze.py)
  - sportsNaiveBayze.py [sportsNaiveBayze](pythonML/sportsNaiveBayze.py)

---

## 2024-06-14 금

---

- hanback전자의 XNode 장비 다루기(윈도우 환경에서 작업)
  1. c드라이브 루트에 hanback 폴더 만들어서 장비에 있는 usb 파일 옮김
  2. B타입 컴퓨터에 연결 (B타입은 bluetooth, zigbee 지원 / A타입은 와이파이 있음)
  3. VScode 실행
  4. 복사한 폴더 안의 Software -> Windows64 폴더 안 압축파일 풀고 Soda IDE설치
  5. C드라이브 루트에 Xnode 폴더 생성()
  6. SodaIDE 폴더 안의 VScode 실행 -> Xnode 폴더 열기
  7. app.py 파일 생성(main파일, 파일 이름은 app으로 고정)
  8. 옮겼던 파일 중 lib 파일을 만들어둔 Xnode 폴더에 복사(라이브러리 가져오기)
  9. app.py 작성 및 진행 (해당 파일안에 진행사항 있음)

- Xnode폴더 안 CORE 폴더의 py파일들
