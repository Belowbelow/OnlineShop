from flask import Flask, request, render_template, session
import mdbc
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111111111'
app.config['SESSION_PERMANENT'] = False


#主页
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

#登陆页面, 请求数据
@app.route('/signin', methods=['GET'])
def singin_form():
    return render_template('signin.html')

#登陆页面， 发送数据
@app.route('/signin', methods=['POST'])
def singin():
    username = request.form['username']
    password = request.form['password']
    if mdbc.check_signin(username, password):
        session['username'] = username
        return render_template('shopping_basket.html')
    return render_template('signin.html', message="Wrong input", username=username)

#帮助页面
@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template('help.html')

#常见问题页面
@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')

#联系我们页面
@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    return render_template('contactus.html')

#网站使用规则页面
@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('search.html')

#注册页面
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

#注册页面
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phonenumber']
    bankcard = request.form['bankcard']
    if mdbc.check_signup(username, password, confirm, email, address, phone, bankcard):
        return render_template('search.html')  
    msg = 'username already exists or password is not equal to confirm'
    return render_template('signup.html', message=msg, username=username)

#结账页面
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():

    return render_template('checkout.html')

#购物篮页面
@app.route('/basket', methods=['GET', 'POST'])
def basket():
    if 'username' in session:
        return render_template('shopping_basket.html')
    return render_template('signin.html', message='请先登陆')

#搜索页面
@app.route('/search', methods=['GET'])
def search_input():
    return render_template('search.html')

#搜索页面
@app.route('/search', methods=['POST'])
def seacrch():
    searchinfo = request.form['search']
    val = mdbc.search(searchinfo)
    return render_template('searchrs.html', searchinfo=searchinfo, val=val)

#书籍页面
@app.route('/books', methods=['GET'])
def books_form():
    return render_template('books.html')

#书籍购买
@app.route('/books', methods=['POST'])
def books():
    ISBN = request.form['ISBN']
    number = request.form['num']
    print(number, type(number))
    if number == '':
        print('0')
        return render_template('books.html')
    elif 'username' in session:
        mdbc.buy(session['username'], ISBN, number)
        return render_template('books.html')
    else:
        return render_template('signin.html', message="请先登录")

if __name__ == "__main__":
    app.run()