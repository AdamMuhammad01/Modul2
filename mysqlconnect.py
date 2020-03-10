import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '363636'
    auth_plugin = 'mysql_native_password',
    database = 'mydatabase' 
    )
c = db.cursor(dictionary=True)
query='delete from '
sql = 'create database'
c.execute('describe karyawan')
print (db)
print(c.fetchall())
print(x)
c.execute(sql)
sql =

for i in x:
    print(i)