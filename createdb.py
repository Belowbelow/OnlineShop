import mysql.connector

def create_user(cur):
    cur.execute('''CREATE TABLE user (id varchar(20) NOT NULL,
                                    username varchar(20) NOT NULL,
                                    password varchar(20) NOT NULL,
                                    PRIMARY KEY (id, username, password))''')

def create_book(cur):
    cur.execute('''CREATE TABLE book (ISBN varchar(20) NOT NULL,
                                    bookname varchar(20) NOT NULL,
                                    price varchar(20) NOT NULL,
                                    type varchar(20) NOT NULL,
                                    storehouse varchar(20) NOT NULL,
                                    soldout varchar(20) NOT NULL,
                                    author varchar(20) NOT NULL,
                                    introduce varchar(255) NOT NULL,
                                    PRIMARY KEY (ISBN, bookname))''')

def create_order(cur):
    cur.execute('''CREATE TABLE order (customer varchar(20) NOT NULL,
                                    ISBN varchar(20) NOT NULL,
                                    number varchar(20) NOT NULL,
                                    address varchar(20) NOT NULL,
                                    bankcard varchar(20) NOT NULL,
                                    PRIMARY KEY(customer,))''')

def create():
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cursor = conn.cursor()

    try:
        create_book(cursor)
        create_order(cursor)
        create_user(cursor)
    except BaseException as e:
        print(e)

    conn.commit()
    cursor.close()
    conn.close()

create()