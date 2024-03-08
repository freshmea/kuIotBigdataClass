use madangdb;
create table Summer(
	sid int primary key,
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
