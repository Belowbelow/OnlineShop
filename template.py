from flask import Flask, request, render_template
import mdbc

app = Flask(__name__)

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
    if mdbc.check_signup(username, password, confirm):
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
    return render_template('shopping_basket.html')

#搜索页面
@app.route('/search', methods=['GET', 'POST'])
def seacrch():
    return render_template('search.html')

if __name__ == "__main__":
    app.run()