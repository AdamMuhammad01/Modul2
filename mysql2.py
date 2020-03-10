'''

sql -u root -p              > masuk ke mysql atau pake .\mysql klo di terminal vscode
create database tokoOnlineku; > bikin database
show databases;               > cek database

create database if not exist tokoOnlineku;  > bikin database klo filenya ga ada
use tokoonlineku;                           > mau kerja di database tokoonlineku
select database();                          > cek lg kerja di database apa
show tables;                                > cek ada tabel apa aja

create table pedagang (     > bikin table nama pedagang
    no int,                 > kolom no isi int
    nama varchar(5)         > kolom nama isi string max 5 karakter
    );                      

describe pedagang;                                  > cek isi database pedagang
drop table pedagang;                                > hapus tabel
select * from pedagang;                             > pilih semua data di tabel pedagang
insert into pedagang values (2,'Andi');             > masukin nilai ke pedagang
insert into pedagang (nama) values ('Budi');        > masukin nama doang
insert into pedagang (nama,no) values ('Caca',3);   > masukin nilai ke no dan nama
select no from pedagang;                            > tampilkan kolom no aja
select nama from pedagang;                          > tampilkan kolom nama aja

insert into pedagang values     > masukin beberapa data sekaligus
(4,'Dedi'),
(5,'Euis'),
(6,'Fafa');

create table pembeli(
    no int not null auto increment,                         > int ga boleh kosong, auto_increment otomatis isi naik nomor
    nama varchar(100) not null default 'Anonim Buyer',      > string ga boleh kosong, klo kosong 'Anonim Buyer'
    usia tinyint,
    berat float(3,1),                                       > (3,1) artinya 3 digit, pembulatan 1 digit belakang koma
    sex enum('Pria','Wanita'),                              > hanya bisa diisi 'Pria' atau 'Wanita'
    bod date,                                               > tanggal lahir format yy-mm-dd
    created_at timestamp default current_timestamp,         > waktu sekarang
    primary key (no)                                        > key unik milik msg2 pembeli
    );

insert into pembeli (nama,usia,berat,sex,bod) values
('Andi',22,77.8,'PRIA','1996-12-29'),
('Budi',22,79.8,'WANITA','1995-12-29');

delete from pembeli;     > hapus data di tabel pembeli
drop table pembeli;      > hapus tabel pembeli

mysql> create table karyawan(
    -> id_kar bigint not null auto_increment,
    -> nama varchar(5) default 'nonim',
    -> sex set('pria','wanita'),                        > hanya bisa diisi 'pria' dan 'wanita', bisa juga pria,wanita, beda sama enum
    -> gaji int default 5000000,
    -> created_at timestamp default current_timestamp,
    -> primary key(id_kar)
    -> );

klo insert data tapi gagal, id nya udah kepake, jd lanjut ke id selanjutnya
id yg gagal, bisa dipake dengan data baru, pake insert, dan id_kar values nya diinput id yg gagal tadi
id yg udah kepake, udah ada isi datanya, ga bisa dipake lagi utk data lain, krn id_kar nya primary

mysql> select nama,gaji from karyawan;
+------+---------+
| nama | gaji    |
+------+---------+
| Anna | 5000000 |
| Boni | 5000000 |
| Elsa | 5000000 |
| Olaf | 5000000 |
+------+---------+
4 rows in set (0.00 sec)

mysql> select gaji,nama from karyawan;
+---------+------+
| gaji    | nama |
+---------+------+
| 5000000 | Anna |
| 5000000 | Boni |
| 5000000 | Elsa |
| 5000000 | Olaf |
+---------+------+
4 rows in set (0.00 sec)

mysql> select nama from karyawan limit 2;
+------+
| nama |
+------+
| Anna |
| Boni |
+------+

mysql> select * from karyawan limit 2,1;                > ngambil 1 data, setelah 2 data, jadi ambil data ke 3
+--------+------+--------+---------+---------------------+
| id_kar | nama | sex    | gaji    | created_at          |
+--------+------+--------+---------+---------------------+
|      4 | Elsa | wanita | 5000000 | 2019-11-21 09:38:02 |
+--------+------+--------+---------+---------------------+

mysql> select nama,gaji,0.03*gaji from karyawan;
+------+---------+-----------+
| nama | gaji    | 0.03*gaji |
+------+---------+-----------+
| Anna | 5000000 | 150000.00 |
| Boni | 5000000 | 150000.00 |
| Elsa | 5000000 | 150000.00 |
| Olaf | 5000000 | 150000.00 |
+------+---------+-----------+

mysql> select nama,gaji,0.03*gaji as pot_bpjs from karyawan;
+------+---------+-----------+
| nama | gaji    | pot_bpjs  |  > gaji*0.03 nya pake nama pot_bpjs
+------+---------+-----------+
| Anna | 5000000 | 150000.00 |
| Boni | 5000000 | 150000.00 |
| Elsa | 5000000 | 150000.00 |
| Olaf | 5000000 | 150000.00 |
+------+---------+-----------+

mysql> select * from karyawan order by nama;    > sort pake kolom nama
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
+--------+------+-------------+---------+---------------------+

mysql> select * from karyawan order by nama desc;   > sort pake kolom nama dibalik
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
+--------+------+-------------+---------+---------------------+

mysql> select * from karyawan order by nama desc,created_at; > sort pake 2 kolom, bisa juga 3 dst
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
+--------+------+-------------+---------+---------------------+

mysql> select * from karyawan order by nama desc,gaji;  > sort nama desc, gaji asc
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      5 | Olaf | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      4 | Elsa | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      2 | Boni | wanita      |  5000000 | 2019-11-21 09:39:28 |
|      1 | Anna | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      7 | Anna | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+

mysql> select * from karyawan where nama='Anna';    > tampilkan data dengan nama 'Anna'
+--------+------+--------+----------+---------------------+
| id_kar | nama | sex    | gaji     | created_at          |
+--------+------+--------+----------+---------------------+
|      1 | Anna | wanita |  5000000 | 2019-11-21 09:34:37 |
|      7 | Anna | NULL   | 12000000 | 2019-11-21 09:57:10 |
+--------+------+--------+----------+---------------------+

mysql> select * from karyawan where gaji>8000000;
+--------+------+------+----------+---------------------+
| id_kar | nama | sex  | gaji     | created_at          |
+--------+------+------+----------+---------------------+
|      7 | Anna | NULL | 12000000 | 2019-11-21 09:57:10 |
+--------+------+------+----------+---------------------+

mysql> select * from karyawan where gaji between 4000000 and 8000000;
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select * from karyawan where gaji > 4000000 and gaji < 8000000;
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select * from karyawan where gaji between 5000000 and 8000000;
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select * from karyawan where gaji > 5000000 and gaji < 8000000;
Empty set (0.00 sec)

mysql> select * from karyawan where nama like 'a%';
+--------+------+--------+----------+---------------------+
| id_kar | nama | sex    | gaji     | created_at          |
+--------+------+--------+----------+---------------------+
|      1 | Anna | wanita |  5000000 | 2019-11-21 09:34:37 |
|      7 | Anna | NULL   | 12000000 | 2019-11-21 09:57:10 |
+--------+------+--------+----------+---------------------+
2 rows in set (0.00 sec)

mysql> select * from karyawan where nama like '%i';
+--------+------+--------+---------+---------------------+
| id_kar | nama | sex    | gaji    | created_at          |
+--------+------+--------+---------+---------------------+
|      2 | Boni | wanita | 5000000 | 2019-11-21 09:39:28 |
+--------+------+--------+---------+---------------------+
1 row in set (0.00 sec)

mysql> select * from karyawan where nama like '%ls';
Empty set (0.00 sec)

mysql> select * from karyawan where nama like '%ls%';
+--------+------+--------+---------+---------------------+
| id_kar | nama | sex    | gaji    | created_at          |
+--------+------+--------+---------+---------------------+
|      4 | Elsa | wanita | 5000000 | 2019-11-21 09:38:02 |
+--------+------+--------+---------+---------------------+
1 row in set (0.00 sec)

mysql> select * from karyawan where nama!='Anna';
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
4 rows in set (0.00 sec)

mysql> select count(*) from karyawan;   > hitung jumlah data di karyawan
+----------+
| count(*) |
+----------+
|        6 |
+----------+
1 row in set (0.01 sec)

mysql> select count(*) from karyawan where nama='Anna';
+----------+
| count(*) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)

mysql> select count(nama) from karyawan where nama='Anna';
+-------------+
| count(nama) |
+-------------+
|           2 |
+-------------+
1 row in set (0.00 sec)

mysql> select count(sex) from karyawan;
+------------+
| count(sex) |
+------------+
|          5 |
+------------+
1 row in set (0.00 sec)

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Anna | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      |  5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Anna | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
6 rows in set (0.00 sec)
mysql> select max(gaji) from karyawan;
+-----------+
| max(gaji) |
+-----------+
|  12000000 |
+-----------+
1 row in set (0.00 sec)

mysql> select max(gaji) as gaji_tertinggi from karyawan;
+----------------+
| gaji_tertinggi |
+----------------+
|       12000000 |
+----------------+
1 row in set (0.00 sec)

mysql> select min(gaji) from karyawan;
+-----------+
| min(gaji) |
+-----------+
|   5000000 |
+-----------+
1 row in set (0.00 sec)

mysql> select min(gaji) as gaji_terendah from karyawan;
+---------------+
| gaji_terendah |
+---------------+
|       5000000 |
+---------------+
1 row in set (0.00 sec)

mysql> select sum(gaji) from karyawan;
+-----------+
| sum(gaji) |
+-----------+
|  37000000 |
+-----------+
1 row in set (0.00 sec)

mysql> select avg(gaji) from karyawan;
+--------------+
| avg(gaji)    |
+--------------+
| 6166666.6667 |
+--------------+
1 row in set (0.00 sec)

mysql> select avg(gaji) from karyawan where gaji < (select avg(gaji) from karyawan);
+--------------+
| avg(gaji)    |
+--------------+
| 5000000.0000 |    > mencari rata2 gaji karyawan yg gajinya di bawah rata2 gaji karyawan semua
+--------------+
1 row in set (0.00 sec)

mysql> select nama from karyawan where gaji < (select avg(gaji) from karyawan);
+------+
| nama |
+------+
| Anna |
| Boni |
| Elsa |
| Olaf |
| Nina |
+------+
5 rows in set (0.00 sec)

mysql> select * from karyawan where gaji < (select avg(gaji) from karyawan);
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select * from karyawan where gaji < (        > ini namanya subquery
    -> select avg(gaji) from karyawan
    -> );
+--------+------+-------------+---------+---------------------+
| id_kar | nama | sex         | gaji    | created_at          |
+--------+------+-------------+---------+---------------------+
|      1 | Anna | wanita      | 5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      | 5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      | 5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita | 5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      | 5000000 | 2019-11-21 09:50:34 |
+--------+------+-------------+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select avg(gaji) from karyawan where gaji < (
    -> select avg(gaji) from karyawan
    -> );
+--------------+
| avg(gaji)    |
+--------------+
| 5000000.0000 |
+--------------+
1 row in set (0.00 sec)

mysql> select avg(gaji) from (
    -> select * from karyawan where gaji < (
    -> select avg(gaji) from karyawan
    -> )) as myquery;
+--------------+
| avg(gaji)    |
+--------------+
| 5000000.0000 |
+--------------+
1 row in set (0.00 sec)

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Anna | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      2 | Boni | wanita      |  5000000 | 2019-11-21 09:39:28 |
|      4 | Elsa | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Anna | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
6 rows in set (0.00 sec)

mysql> delete from karyawan where id_kar=2;
Query OK, 1 row affected (0.01 sec)

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Anna | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      4 | Elsa | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      5 | Olaf | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Nina | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Anna | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> update karyawan set nama='Budi';     > update semua nama jadi 'Budi'
Query OK, 5 rows affected (0.00 sec)
Rows matched: 5  Changed: 5  Warnings: 0

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Budi | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      4 | Budi | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      5 | Budi | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Budi | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Budi | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> update karyawan set nama='Andi' where sex='wanita';  > update semua nama jadi 'Andi' hanya yg 'wanita'
Query OK, 3 rows affected (0.01 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Andi | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      4 | Andi | wanita      |  5000000 | 2019-11-21 09:38:02 |
|      5 | Budi | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Andi | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Budi | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> update karyawan set      > update i data dengan bbrp atribut
    -> nama='Dina',gaji=7500000
    -> where id_kar=4;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Andi | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      4 | Dina | wanita      |  7500000 | 2019-11-21 09:38:02 |
|      5 | Budi | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Andi | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Budi | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> add column
    -> alamat text;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe karyawan;
+------------+----------------------+------+-----+-------------------+-------------------+
| Field      | Type                 | Null | Key | Default           | Extra             |
+------------+----------------------+------+-----+-------------------+-------------------+
| id_kar     | bigint(20)           | NO   | PRI | NULL              | auto_increment    |
| nama       | varchar(5)           | YES  |     | nonim             |                   |
| sex        | set('pria','wanita') | YES  |     | NULL              |                   |
| gaji       | int(11)              | YES  |     | 5000000           |                   |
| created_at | timestamp            | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| alamat     | text                 | YES  |     | NULL              |                   |
+------------+----------------------+------+-----+-------------------+-------------------+
6 rows in set (0.00 sec)

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+--------+
| id_kar | nama | sex         | gaji     | created_at          | alamat |
+--------+------+-------------+----------+---------------------+--------+
|      1 | Andi | wanita      |  5000000 | 2019-11-21 09:34:37 | NULL   |
|      4 | Dina | wanita      |  7500000 | 2019-11-21 09:38:02 | NULL   |
|      5 | Budi | pria,wanita |  5000000 | 2019-11-21 09:38:02 | NULL   |
|      6 | Andi | wanita      |  5000000 | 2019-11-21 09:50:34 | NULL   |
|      7 | Budi | NULL        | 12000000 | 2019-11-21 09:57:10 | NULL   |
+--------+------+-------------+----------+---------------------+--------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> drop column alamat;
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+-------------+----------+---------------------+
| id_kar | nama | sex         | gaji     | created_at          |
+--------+------+-------------+----------+---------------------+
|      1 | Andi | wanita      |  5000000 | 2019-11-21 09:34:37 |
|      4 | Dina | wanita      |  7500000 | 2019-11-21 09:38:02 |
|      5 | Budi | pria,wanita |  5000000 | 2019-11-21 09:38:02 |
|      6 | Andi | wanita      |  5000000 | 2019-11-21 09:50:34 |
|      7 | Budi | NULL        | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> add column
    -> alamat text
    -> after sex;
Query OK, 0 rows affected (0.18 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+-------------+--------+----------+---------------------+
| id_kar | nama | sex         | alamat | gaji     | created_at          |
+--------+------+-------------+--------+----------+---------------------+
|      1 | Andi | wanita      | NULL   |  5000000 | 2019-11-21 09:34:37 |
|      4 | Dina | wanita      | NULL   |  7500000 | 2019-11-21 09:38:02 |
|      5 | Budi | pria,wanita | NULL   |  5000000 | 2019-11-21 09:38:02 |
|      6 | Andi | wanita      | NULL   |  5000000 | 2019-11-21 09:50:34 |
|      7 | Budi | NULL        | NULL   | 12000000 | 2019-11-21 09:57:10 |
+--------+------+-------------+--------+----------+---------------------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> modify column
    -> sex set('pria','wanita')
    -> after gaji;
Query OK, 0 rows affected (0.18 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+--------+----------+-------------+---------------------+
| id_kar | nama | alamat | gaji     | sex         | created_at          |
+--------+------+--------+----------+-------------+---------------------+
|      1 | Andi | NULL   |  5000000 | wanita      | 2019-11-21 09:34:37 |
|      4 | Dina | NULL   |  7500000 | wanita      | 2019-11-21 09:38:02 |
|      5 | Budi | NULL   |  5000000 | pria,wanita | 2019-11-21 09:38:02 |
|      6 | Andi | NULL   |  5000000 | wanita      | 2019-11-21 09:50:34 |
|      7 | Budi | NULL   | 12000000 | NULL        | 2019-11-21 09:57:10 |
+--------+------+--------+----------+-------------+---------------------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> modify column
    -> nama varchar(50) default 'Anonim 50'
    -> after gaji;
Query OK, 0 rows affected (0.18 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+--------+----------+------+-------------+---------------------+
| id_kar | alamat | gaji     | nama | sex         | created_at          |
+--------+--------+----------+------+-------------+---------------------+
|      1 | NULL   |  5000000 | Andi | wanita      | 2019-11-21 09:34:37 |
|      4 | NULL   |  7500000 | Dina | wanita      | 2019-11-21 09:38:02 |
|      5 | NULL   |  5000000 | Budi | pria,wanita | 2019-11-21 09:38:02 |
|      6 | NULL   |  5000000 | Andi | wanita      | 2019-11-21 09:50:34 |
|      7 | NULL   | 12000000 | Budi | NULL        | 2019-11-21 09:57:10 |
+--------+--------+----------+------+-------------+---------------------+
5 rows in set (0.00 sec)

mysql> alter table karyawan
    -> rename column
    -> sex to gender;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+--------+----------+------+-------------+---------------------+
| id_kar | alamat | gaji     | nama | gender      | created_at          |
+--------+--------+----------+------+-------------+---------------------+
|      1 | NULL   |  5000000 | Andi | wanita      | 2019-11-21 09:34:37 |
|      4 | NULL   |  7500000 | Dina | wanita      | 2019-11-21 09:38:02 |
|      5 | NULL   |  5000000 | Budi | pria,wanita | 2019-11-21 09:38:02 |
|      6 | NULL   |  5000000 | Andi | wanita      | 2019-11-21 09:50:34 |
|      7 | NULL   | 12000000 | Budi | NULL        | 2019-11-21 09:57:10 |
+--------+--------+----------+------+-------------+---------------------+
5 rows in set (0.00 sec)

py -m pip install MySQL-connector-python
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6
PS C:\Program Files\MySQL\MySQL Server 8.0\bin> my sql
my : The term 'my' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the        
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ my sql
+ ~~
    + CategoryInfo          : ObjectNotFound: (my:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Program Files\MySQL\MySQL Server 8.0\bin> .\ mysql -u root -p
.\ : The term '.\' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the        
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ .\ mysql -u root -p
+ ~~
    + CategoryInfo          : ObjectNotFound: (.\:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Program Files\MySQL\MySQL Server 8.0\bin> .\mysql -u root -p
Enter password: ******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 23
Server version: 8.0.18 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> select * from karyawan;
ERROR 1046 (3D000): No database selected
mysql> describe karyawan;
ERROR 1046 (3D000): No database selected
mysql> show datbase;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'datbase' at line 1
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

mysql> use mydatabase;
Database changed
mysql> describe karyawan;
+-----------+----------------------+------+-----+-------------------+-------------------+
| Field     | Type                 | Null | Key | Default           | Extra             |
+-----------+----------------------+------+-----+-------------------+-------------------+
| id_kar    | bigint(20)           | NO   | PRI | NULL              | auto_increment    |
| nama      | varchar(5)           | YES  |     | nonim             |                   |
| sex       | set('Pria','Wanita') | YES  |     | NULL              |                   |
| gaji      | int(11)              | YES  |     | 5000000           |                   |
| create_at | timestamp            | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+-----------+----------------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)

mysql> select * from karyawan;
+--------+------+--------+---------+---------------------+
| id_kar | nama | sex    | gaji    | create_at           |
+--------+------+--------+---------+---------------------+
|      2 | Adam | Pria   | 5000000 | 2019-11-21 09:35:29 |
|      3 | Anna | Wanita | 6500000 | 2019-11-21 09:36:06 |
|      4 | bams | Wanita | 7000000 | 2019-11-21 09:59:44 |
|      5 | reni | Pria   | 5500000 | 2019-11-21 10:00:18 |
+--------+------+--------+---------+---------------------+
4 rows in set (0.00 sec)

mysql> alter table karyawan drop column alamat;
ERROR 1091 (42000): Can't DROP 'alamat'; check that column/key exists
mysql> alter table karyawan drop column alamat; 
ERROR 1091 (42000): Can't DROP 'alamat'; check that column/key exists
mysql> alter table karyawan                    
    -> add column  ka 
    -> add column     
    -> alamat text
    -> after sex;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'add column
alamat text
after sex' at line 3
mysql> alter table karyawan
    -> add column
    -> alamat text
    -> after sex;
Query OK, 0 rows affected (2.10 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+--------+--------+---------+---------------------+
| id_kar | nama | sex    | alamat | gaji    | create_at           |
+--------+------+--------+--------+---------+---------------------+
|      2 | Adam | Pria   | NULL   | 5000000 | 2019-11-21 09:35:29 |
|      3 | Anna | Wanita | NULL   | 6500000 | 2019-11-21 09:36:06 |
|      4 | bams | Wanita | NULL   | 7000000 | 2019-11-21 09:59:44 |
|      5 | reni | Pria   | NULL   | 5500000 | 2019-11-21 10:00:18 |
+--------+------+--------+--------+---------+---------------------+
4 rows in set (0.00 sec)

mysql> alter table karyawan
    -> modify column
    -> sex set ('Pria','Wanita')
    -> after gaji;
Query OK, 0 rows affected (2.79 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+--------+---------+--------+---------------------+
| id_kar | nama | alamat | gaji    | sex    | create_at           |
+--------+------+--------+---------+--------+---------------------+
|      2 | Adam | NULL   | 5000000 | Pria   | 2019-11-21 09:35:29 |
|      3 | Anna | NULL   | 6500000 | Wanita | 2019-11-21 09:36:06 |
|      4 | bams | NULL   | 7000000 | Wanita | 2019-11-21 09:59:44 |
|      5 | reni | NULL   | 5500000 | Pria   | 2019-11-21 10:00:18 |
+--------+------+--------+---------+--------+---------------------+
4 rows in set (0.00 sec)

mysql> alter table karyawan
    -> modify column
    -> 
    -> sex set ('Pria','Wanita')
    -> after nama;
Query OK, 0 rows affected (1.68 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from karyawan;
+--------+------+--------+--------+---------+---------------------+
| id_kar | nama | sex    | alamat | gaji    | create_at           |
+--------+------+--------+--------+---------+---------------------+
|      2 | Adam | Pria   | NULL   | 5000000 | 2019-11-21 09:35:29 |
|      3 | Anna | Wanita | NULL   | 6500000 | 2019-11-21 09:36:06 |
|      4 | bams | Wanita | NULL   | 7000000 | 2019-11-21 09:59:44 |
|      5 | reni | Pria   | NULL   | 5500000 | 2019-11-21 10:00:18 |
+--------+------+--------+--------+---------+---------------------+
4 rows in set (0.00 sec)

mysql> alter table karyawan 
    -> modify column
    -> nama varchar(50) default 'Anonim50'
    -> after gaji;
Query OK, 0 rows affected (1.44 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe karyawan;
+-----------+----------------------+------+-----+-------------------+-------------------+
| Field     | Type                 | Null | Key | Default           | Extra             |
+-----------+----------------------+------+-----+-------------------+-------------------+
| id_kar    | bigint(20)           | NO   | PRI | NULL              | auto_increment    |
| sex       | set('Pria','Wanita') | YES  |     | NULL              |                   |
| alamat    | text                 | YES  |     | NULL              |                   |
| gaji      | int(11)              | YES  |     | 5000000           |                   |
| nama      | varchar(50)          | YES  |     | Anonim50          |                   |
| create_at | timestamp            | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+-----------+----------------------+------+-----+-------------------+-------------------+
6 rows in set (0.05 sec)

mysql> alter table karyawan
    -> rename column
    -> sex to gender;
Query OK, 0 rows affected (0.15 sec)
Records: 0  Duplicates: 0  Warnings: 0


'''






import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '363636',
    # auth_plugin = 'mysql_native_password',
    # database = 'mydatabase' 
    # database = 'mydatabase'
)
c = db.cursor()
sql = 'create database'
# c.execute('describe karyawan')
# print (db)
# print(c.fetchall())
# print(x)
c.execute(sql)
# sql =

# for i in x:
#     print(i)