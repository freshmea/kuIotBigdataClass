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
  - 3자 내용 추가
    - 셀렉트 쓰는 방법
