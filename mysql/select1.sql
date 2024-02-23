-- example 3-1
select bookname, price from Book;

-- example 2
select price, bookname from Book;

-- example 3-2 
select bookid, bookname, publisher, price from Book;

select * from Book;

-- example 3-3
select publisher from Book;
select distinct publisher from Book;

-- example 3-4
select * from Book;
select * from Book where price < 20000;

-- example 3-5
select * from Book where price between 10000 and 20000;
select * from Book where price >= 10000 and price <= 20000;

-- example 3-6
select * from Book where publisher in ('대한미디어', '굿스포츠');
select * from Book where publisher not in ('대한미디어', '굿스포츠');

-- example 3-7 3-8
select bookname 책이름, publisher "발행 자" from Book where bookname like '축구의 역사';
select bookname, publisher from Book where bookname like '축구%';

-- example 3-9
select * from Book where bookname like '_구%';

-- example 3-10 3-11
select * from Book where (bookname like '%축구%') and (price >= 20000);
select * from Book where (publisher = '굿스포츠') or (publisher = '대한미디어');
select * from Book where (publisher = '굿스포츠') or (price >= 10000);

-- example 3-12 
select * from Book order by bookname;
select * from Book order by bookname desc;

-- example 3-14
select * from Book order by price desc, publisher asc;