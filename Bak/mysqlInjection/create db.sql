create database mysqlInjection;
use mysqlInjection;
create table Users(
user varchar(255) not null,
pw varchar(255) not null
);

insert into Users(user,pw)
values ('Test','69');
insert into Users(user,pw)
values ('Test1','187');
insert into Users(user,pw)
values ('Test2','420');

select * from Users;