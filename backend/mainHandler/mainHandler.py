import sys, platform
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_clicked', methods=['POST'])
def login_clicked():
    username = request.form.get('username_input')
    password = request.form.get('password_input')
    print(username)
    print(password)
    return render_template('signupHandler.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/root')
def root():
    return render_template('root.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)