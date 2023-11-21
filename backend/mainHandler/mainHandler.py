import sys
from flask import Flask, request, render_template, redirect, url_for, jsonify

sys.path.append('../SE_P2G8_KnowledgeGraph/backend/')

from graphData import gd
from loginHandler import authHelper

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('root.html')

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
    login_success = authHelper.detectLogin(userCredential[0], userCredential[1])
    if login_success == True:
        return jsonify({'redirect_url': url_for('nav')})
        #return redirect(url_for('home'), code=302)
    elif login_success == False:
        #return redirect(url_for('login'), code=302)
        return jsonify({'redirect_url': url_for('login_failed')})

@app.route('/login_failed')
def login_failed():
    return render_template('loginFail.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_clicked', methods=['POST'])
def signup_clicked():
    sign_up_username = request.form.get('username_input')
    sign_up_password = request.form.get('password_input')
    print(f'signup_username={sign_up_username}')
    print(f'signup_password={sign_up_password}')
    authHelper.addUser(sign_up_username, sign_up_password)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/graph')
def sendGraph():
    graphDataPy = gd.readGD()
    return render_template('graph_extern.html', gdata = graphDataPy)

@app.route('/send_echarts_js')
def send_echarts_js():
    return app.send_static_file('echarts_working.js')

@app.route('/send_login_stat')
def send_login_status():
    return app.send_static_file('loginSuccess.js')

@app.route('/send_graph_raw_data')
def send_graph_raw_data():
    return app.send_static_file('graphRawData.js')

@app.route('/nav')
def nav():
    return render_template('nav.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)