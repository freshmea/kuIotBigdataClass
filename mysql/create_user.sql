create database madangdb;
create user madang@localhost identified with mysql_native_password by 'madang';
grant all privileges on madangdb.* to madang@localhost;
commit;