use mysql;
select host, user from user;

create user 'root'@'%' identified by '0000';
grant all privileges on *.* to 'root'@'%';
flush privileges;