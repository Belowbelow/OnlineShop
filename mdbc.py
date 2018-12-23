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
def check_signup(name, psw, confirm):
    conn = mysql.connector.connect(user='root', password='123456', database='bookshop')
    cur = conn.cursor()
    cmd = 'insert into users values (%s, %s)'
    if not check_user(name):
        if psw==confirm:
            cur.execute(cmd, [str(name), str(psw)])
            conn.commit()
            cur.close()
            conn.close()
            return True
    cur.close()
    conn.close()
    return False

print(check_signup('test', '123', '123'))