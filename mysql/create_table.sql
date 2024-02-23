CREATE TABLE Book (
  bookid		INTEGER PRIMARY KEY,
  bookname	VARCHAR(40),
  publisher	VARCHAR(40),
  price		INTEGER
);

CREATE TABLE  Customer (
  custid		INTEGER PRIMARY KEY,
  name		VARCHAR(40),
  address		VARCHAR(50),
  phone		VARCHAR(20)
);


CREATE TABLE Orders (
  orderid INTEGER PRIMARY KEY,
  custid  INTEGER,
  bookid  INTEGER,
  saleprice INTEGER,
  orderdate DATE,
  FOREIGN KEY (custid) REFERENCES Customer(custid),
  FOREIGN KEY (bookid) REFERENCES Book(bookid)
);