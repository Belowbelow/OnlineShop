import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()

#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id, name) values (%s, %s)', ['001', 'Alice'])
print(cursor.rowcount)
cursor.execute('select * from user')
print(cursor.execute('select * from user'))


cursor.close()
conn.commit()
conn.close()