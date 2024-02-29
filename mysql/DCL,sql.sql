use madangdb;

-- 3-45 example
insert into Book(bookid, bookname, publisher)
	value (14, '스포츠 의학', '한솔의학서적');
select * from Book;

-- 2-46 example
create table Imported_book(
	bookid integer primary key,
    bookname varchar(20),
    publisher varchar(20),
    price integer);

select * from Imported_book;
insert into Imported_book(bookid, bookname, price, publisher)
	select bookid, bookname, price, publisher
    from Book;

-- 3-47 example
set SQL_SAFE_UPDATES=0;
select * from Customer;
update Customer set address = '대한민국 부산' where custid=5;

-- 3-48 example update
select * from Book;
update 	Book
set 	publisher = (	select publisher
						from Imported_book
                        where bookid=10)
where bookid=14;

-- 3-39 example delete
delete from Book where bookid > 10;
select * from Book;

select * from Customer;
delete from Customer;

alter table Orders drop custid foreign key;