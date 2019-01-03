import mysql.connector

def create_user(cur):
    cmd = '''
    CREATE TABLE IF NOT EXISTS users 
    (id INT NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    password varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    phonenumber varchar(50) NOT NULL,
    address varchar(50) NOT NULL,
    bankcard varchar(50) NOT NULL,
    PRIMARY KEY (id));
    '''
    cur.execute(cmd)

def create_book(cur):
    cmd = '''
    CREATE TABLE IF NOT EXISTS books 
    (bookid INT NOT NULL AUTO_INCREMENT,
    ISBN varchar(50) NOT NULL,
    bookname varchar(50) NOT NULL,
    price varchar(50) NOT NULL,
    type varchar(50) NOT NULL,
    storehouse varchar(50) NOT NULL,
    soldout varchar(50) NOT NULL,
    author varchar(50) NOT NULL,
    introduce varchar(255) NOT NULL,
    bookpicture varchar(50) NOT NULL,
    PRIMARY KEY (bookid))
    '''
    cur.execute(cmd)

def create_order(cur):
    cmd = '''
    CREATE TABLE IF NOT EXISTS orders 
    (orderid INT NOT NULL AUTO_INCREMENT,
    customer varchar(50) NOT NULL,
    ISBN varchar(50) NOT NULL,
    number varchar(50) NOT NULL,
    state varchar(50) NOT NULL,
    PRIMARY KEY(orderid))
    '''
    cur.execute(cmd)

def insert_books(cur):
    cmd = '''
    INSERT INTO books
    (ISBN, bookname, price, type, storehouse, soldout, author, introduce, bookpicture)
    VALUES
    '''
    fPath = './book.txt'
    with open(fPath, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print('(' + str(line).replace('\r', '').replace('\n', '') +');')
            cur.execute(cmd + '(' + str(line).replace('\r', '').replace('\n', '') +');')

def create():
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cursor = conn.cursor()

    try:
        create_user(cursor)
        create_book(cursor)
        create_order(cursor)
        insert_books(cursor)

    except BaseException as e:
        print(e)

    conn.commit()
    cursor.close()
    conn.close()

create()