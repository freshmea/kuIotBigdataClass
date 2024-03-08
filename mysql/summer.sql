use madangdb;
create table Summer(
	sid int,
    class varchar(40),
    price int);
    
insert into Summer values (100, 'JAVA', 20000);
insert into Summer values (150, 'PYTHON', 15000);
insert into Summer values (200, 'C', 10000);
insert into Summer values (250, 'JAVA', 20000);

select * from Summer;

-- 7-1 example 
-- c class 의가격
select price as 'C class 의 가격' 
from Summer
where class like 'C';

-- 200번 학생의 수강 취소
delete from Summer where sid=200;

-- 7-2 example
-- C++ 강좌 개설
insert into Summer values (NULL, 'C++', 25000);

-- 수강인원 
select count(*) from Summer;

-- 7-3 example
set sql_safe_updates=0;
update Summer set price=20000 where class like 'JAVA' and sid = 250;
select * from Summer;


create table SummerPrice(
	class varchar(20),
    price integer);
create table SummerEnroll(
	sid integer,
    class varchar(20));
    
insert into SummerPrice values ('JAVA', 20000);
insert into SummerPrice values ('PYTHON', 25000);
insert into SummerPrice values ('C', 10000);

insert into SummerEnroll values (100, 'JAVA');
insert into SummerEnroll values (150, 'PYTHON');
insert into SummerEnroll values (200, 'C');
insert into SummerEnroll values (250, 'JAVA');

select * from SummerPrice;
select * from SummerEnroll;

-- 7-4 example 삭제 이상 발생 안되는 예제.
select price as 'C class 의 가격' 
from SummerPrice
where class like 'C';

delete from SummerEnroll where sid=200;
select * from SummerEnroll;

-- 7-5 example 삽입 이상 발생 안되는 예제
insert into SummerPrice values ('C++', 25000);

select count(*) from SummerEnroll;

-- 7-6 example 수정 이상
update SummerPrice set price=15000 where class like 'JAVA';

select price as 'JAVA class 의 가격' 
from SummerPrice
where class like 'JAVA';
