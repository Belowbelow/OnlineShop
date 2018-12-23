from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def singin_form():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def singin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123':
        return render_template('shopping_basket.html')
    return render_template('signin.html', message="Wrong input", username=username)

@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template('help.html')

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    return render_template('contactus.html')

@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('rules.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    return render_template('checkout.html')

@app.route('/basket', methods=['GET', 'POST'])
def basket():
    return render_template('shopping_basket')

if __name__ == "__main__":
    app.run()