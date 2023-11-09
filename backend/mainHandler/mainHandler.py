import sys
from flask import Flask, request, render_template, redirect, url_for
from neo4j import GraphDatabase

sys.path.append('../backend/loginHandler/')

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_clicked', methods=['POST'])
def login_clicked():
    login_username = request.form.get('username_input')
    login_password = request.form.get('password_input')
    print(f'login_username={login_username}')
    print(f'login_password={login_password}')

    userCredential = [login_username, login_password]
    login_success = True
    if login_success:
        return redirect('http://localhost:8000/home', code=302)
    else:
        return redirect(url_for('login'), code=302)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_clicked', methods=['POST'])
def signup_clicked():
    sign_up_username = request.form.get('username_input')
    sign_up_password = request.form.get('password_input')
    print(f'signup_username={sign_up_username}')
    print(f'signup_password={sign_up_password}')
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/root')
def root():
    return render_template('root.html')

@app.route('/fetchData')
def fetchData():
    return app.send_static_file('graphData.json')

@app.route('/echarts.html')
def sendECharts():
    return app.send_static_file('echarts.html')

@app.route('/sendechartsjs')
def sendecjs():
    return app.send_static_file('echarts.js')

@app.route('/nav')
def nav():
    return render_template('nav.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)