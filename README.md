# kuIotBigdataClass
C/C++ database arduino raspberrypi Iot clas.....

---
## 2024-02-22
---

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
    https://www.heropy.dev/p/B74sNE
  - 영상 시청 git: 
    https://www.youtube.com/watch?v=YFNQwo7iTNc
    https://www.youtube.com/watch?v=1I3hMwQU6GU&t=5618s

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
	3문제 풀기.
프로그래머스 SQL 언어:
         0 문제 풀기.
영상 과제:
     https://www.youtube.com/watch?v=K9L9YZhEjC0
     https://www.youtube.com/watch?v=Xp1IKwJfDAA


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
	3문제 풀기.
프로그래머스 SQL 언어:
 ‘인기 있는 아이스크림’
	‘3월에 태어난 여성 회원 목록’
	‘조건에 맞는 도서 리스트’
	‘흉부 외과 또는 일반외과’
영상 과제:
포스팅 과제:
               https://www.tuwlab.com/ece/27193


---
## 2024-02-29
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
    - 다수의 행, 다수의 열 ( in, not in, exists, not exists)[집합, 존재]
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