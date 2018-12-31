import mysql.connector

#登陆功能， 检测数据库中是否存在该用户， 存在则返回True， 否则False
def check_signin(name, psw):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'select * from users where (username=%s and password=%s)'
    cur.execute(cmd, [str(name), str(psw)])
    values = cur.fetchall()
    print(values)
    if values:
        conn.close()
        return True
    else:
        conn.close()
        return False

#检测用户是否存在
def check_user(name):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'select * from users where username=%s'
    cur.execute(cmd, [str(name)])
    values = cur.fetchall()
    print(values)
    if values:
        conn.close()
        return True
    else:
        conn.close()
        return False


#注册功能， 若用户名不存在，则注册， 并返回True，否则返回False
def check_signup(name, psw, confirm, email, address, phone, bankcard):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = '''insert into users (username, password, email, phonenumber, address, bankcard)
            values (%s, %s, %s, %s, %s, %s)'''
    if not check_user(name):
        if psw==confirm:
            cur.execute(cmd, [str(name), str(psw), str(email), str(phone), str(address), str(bankcard)])
            conn.commit()
            cur.close()
            conn.close()
            return True
    cur.close()
    conn.close()
    return False

#搜索功能， 输入ISBN号， 书名， 作者， 类型， 搜索书籍， 返回所有结果
def search(info):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'select * from books where ISBN=%s or bookname=%s or type=%s or author=%s'
    info1 = str(info)
    cur.execute(cmd, [info1, info1, info1, info1])
    values = cur.fetchall()
    print(values)
    return(values)
    conn.close()

#购物车功能， 将购物信息添加到数据库
def buy(username, ISBN, num):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'insert into orders (customer, ISBN, number, state) values(%s, %s, %s, %s)'
    cur.execute(cmd, [str(username), str(ISBN), str(num), str(0)])
    conn.commit()
    conn.close()

#获取用户订单
def get_orders(username):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'select * from orders where customer=%s'
    cur.execute(cmd, [str(username)])
    val = cur.fetchall()
    return val
    conn.close()

#处理订单
def deal_orders(username):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'update orders set state=%s where customer=%s'
    cur.execute(cmd, [str(1), str(username)])
    conn.commit()
    conn.close()