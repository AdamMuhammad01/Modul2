Microsoft Windows [Version 10.0.18363.476]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>cd C:\Program Files\MySQL\MySQL Server 8.0\bin

C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql -u root -p
Enter password: ******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.0.18 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.08 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> create database mydatabase;
Query OK, 1 row affected (0.18 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydatabase         |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use mydatabase
Database changed
mysql> select database()
    -> ;
+------------+
| database() |
+------------+
| mydatabase |
+------------+
1 row in set (0.00 sec)

mysql> create table kota
    -> ;
ERROR 1113 (42000): A table must have at least 1 column
mysql> create table kota
    -> no int,
    -> nama varchar(5)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'no int,
nama varchar(5)
)' at line 2
mysql> create table kota(
    -> no int,
    -> create table kota
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create table kota
)' at line 3
mysql> create table kota(
    -> no int,
    -> nama varchar(5)
    -> );
Query OK, 0 rows affected (2.13 sec)

mysql> show tables,
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',' at line 1
mysql> show tables;
+----------------------+
| Tables_in_mydatabase |
+----------------------+
| kota                 |
+----------------------+
1 row in set (0.14 sec)

mysql> describe kota;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| no    | int(11)    | YES  |     | NULL    |       |
| nama  | varchar(5) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
2 rows in set (0.03 sec)

mysql> drop table mydatabase;
ERROR 1051 (42S02): Unknown table 'mydatabase.mydatabase'
mysql> select * from kota;
Empty set (0.04 sec)

mysql> insert into kota
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> insert into kota values(2,'adam')
    -> ;
Query OK, 1 row affected (0.15 sec)

mysql> select * from kota
    -> ;
+------+------+
| no   | nama |
+------+------+
|    2 | adam |
+------+------+
1 row in set (0.00 sec)

mysql> insert into kota values(3,'bambang');
ERROR 1406 (22001): Data too long for column 'nama' at row 1
mysql> insert into kota (nama) values('bambang');
ERROR 1406 (22001): Data too long for column 'nama' at row 1
mysql> inser into kota (nama) values ('budi');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'inser into kota (nama) values ('budi')' at line 1
mysql> insert into kota (nama) values ('bambang')
    -> ;
ERROR 1406 (22001): Data too long for column 'nama' at row 1
mysql> insert into kota (nama) values ('budi')
    -> ;
Query OK, 1 row affected (0.17 sec)

mysql> select * from kota;
+------+------+
| no   | nama |
+------+------+
|    2 | adam |
| NULL | budi |
+------+------+
2 rows in set (0.00 sec)

mysql> insert into kota (nama) values ('budi',25);
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> insert into kota (nama) values ('budi',25)
    -> ;
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> insert into kota (nama,no) values ('caca', 25);
Query OK, 1 row affected (0.12 sec)

mysql> select * from kota;
+------+------+
| no   | nama |
+------+------+
|    2 | adam |
| NULL | budi |
|   25 | caca |
+------+------+
3 rows in set (0.00 sec)

mysql> insert into kota values
    -> (3, 'koko'),
    -> (6,'ronaldo'),
    -> (89,'zambrota');
ERROR 1406 (22001): Data too long for column 'nama' at row 2
mysql> (3, 'koko');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '3, 'koko')' at line 1
mysql> insert into kota values
    -> (3,'ronaldo')
    -> ;
ERROR 1406 (22001): Data too long for column 'nama' at row 1
mysql> insert into kota values
    -> (6,'rona'),
    -> (9,'vera'),
    -> (88,'zamb');
Query OK, 3 rows affected (0.16 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from kota
    -> ;
+------+------+
| no   | nama |
+------+------+
|    2 | adam |
| NULL | budi |
|   25 | caca |
|    6 | rona |
|    9 | vera |
|   88 | zamb |
+------+------+
6 rows in set (0.00 sec)

mysql> create table warga(
    -> no int not null auto_increment,
    -> nama varchar(100) not null default 'anonymous'
    -> usia inyint,
    -> berat float(3,1),
    -> sex enum('pria', 'wanita'),
    -> bod date,
    -> primary key (no)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'usia inyint,
berat float(3,1),
sex enum('pria', 'wanita'),
bod date,
primary k' at line 4
mysql> create table warga(
    -> no int not null auto_increment,
    -> nama varchar(100) not null default 'anonymous'
    -> usia tinyint,
    -> berat float(3,1),
    -> sex enum('pria', 'wanita'),
    -> bod date,
    -> primary key (no),
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'usia tinyint,
berat float(3,1),
sex enum('pria', 'wanita'),
bod date,
primary ' at line 4
mysql> create table warga(
    -> no int not null auto_increment,
    -> nama varchar(100) not null default 'anonymous',
    -> usia tinyint,
    -> berat float(3,1),
    -> sex enum('pria','wanita'),
    -> bod date,
    -> created_at timestamp default current_timestamp,
    -> primary key(no)
    -> );
Query OK, 0 rows affected, 1 warning (0.94 sec)

mysql> select * from warga
    -> ;
Empty set (0.00 sec)

mysql> describe warga;
+------------+-----------------------+------+-----+-------------------+-------------------+
| Field      | Type                  | Null | Key | Default           | Extra             |
+------------+-----------------------+------+-----+-------------------+-------------------+
| no         | int(11)               | NO   | PRI | NULL              | auto_increment    |
| nama       | varchar(100)          | NO   |     | anonymous         |                   |
| usia       | tinyint(4)            | YES  |     | NULL              |                   |
| berat      | float(3,1)            | YES  |     | NULL              |                   |
| sex        | enum('pria','wanita') | YES  |     | NULL              |                   |
| bod        | date                  | YES  |     | NULL              |                   |
| created_at | timestamp             | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+-----------------------+------+-----+-------------------+-------------------+
7 rows in set (0.00 sec)

mysql> insert into warga (nama, usia, berat, sex, bod) values
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> insert into warga (nama, usia, berat, sex, bod) values
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> insert into warga (nama, usia, berat, sex, bod) values
    -> ('andi',22,77.8,'PRIA','1996-01-01')
    -> ('anuar',23,36.8,'PRIA','1995-01-01');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '('anuar',23,36.8,'PRIA','1995-01-01')' at line 3
mysql> insert into warga (nama, usia, berat, sex, bod) values,
    -> ('andi',22,77.8,'PRIA','1996-01-01'),
    -> ('anuar',23,36.8,'PRIA','1995-01-01');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',
('andi',22,77.8,'PRIA','1996-01-01'),
('anuar',23,36.8,'PRIA','1995-01-01')' at line 1
mysql> insert into warga (nama, usia, berat, sex, bod) values
    -> ('andi',22,77.8,'PRIA','1996-01-01'),
    -> ('anuar',23,36.8,'PRIA','1995-01-01');
Query OK, 2 rows affected (0.20 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from warga;
+----+-------+------+-------+------+------------+---------------------+
| no | nama  | usia | berat | sex  | bod        | created_at          |
+----+-------+------+-------+------+------------+---------------------+
|  1 | andi  |   22 |  77.8 | pria | 1996-01-01 | 2019-11-20 11:58:28 |
|  2 | anuar |   23 |  36.8 | pria | 1995-01-01 | 2019-11-20 11:58:28 |
+----+-------+------+-------+------+------------+---------------------+
2 rows in set (0.00 sec)

mysql> insert into warga (berat) values (45.3);
Query OK, 1 row affected (0.10 sec)

mysql> select * from warga;
+----+-----------+------+-------+------+------------+---------------------+
| no | nama      | usia | berat | sex  | bod        | created_at          |
+----+-----------+------+-------+------+------------+---------------------+
|  1 | andi      |   22 |  77.8 | pria | 1996-01-01 | 2019-11-20 11:58:28 |
|  2 | anuar     |   23 |  36.8 | pria | 1995-01-01 | 2019-11-20 11:58:28 |
|  3 | anonymous | NULL |  45.3 | NULL | NULL       | 2019-11-20 12:01:38 |
+----+-----------+------+-------+------+------------+---------------------+
3 rows in set (0.00 sec)
