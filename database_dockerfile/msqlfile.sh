#!/bin/bash
mysql -u root -psumit2606 <<EOF 
create database facebook;
use facebook;
create table user(id int not null primary key auto_increment, name varchar(100), address varchar(100));
insert into user values(1,"sumit","pune");
insert into user values("patil", "mumbai");
EOF
