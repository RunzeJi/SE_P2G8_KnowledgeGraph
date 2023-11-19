import sys
from flask import Flask, request, render_template, redirect, url_for

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

@app.route('/graph')
def sendGraph():
    graphDataPy = {
        "nodes": [
            {"cNumber": 120, "category": 0, "name": "A1"},
            {"cNumber": 120, "category": 0, "name": "A2"},
            {"cNumber": 100, "category": 1, "name": "B1"},
            {"cNumber": 100, "category": 1, "name": "B2"},
            {"cNumber": 80, "category": 2, "name": "C1"},
            {"cNumber": 80, "category": 2, "name": "D1"},
            {"cNumber": 80, "category": 3, "name": "E1"},
            {"cNumber": 80, "category": 3, "name": "F1"},
            {"cNumber": 80, "category": 2, "name": "C2"},
            {"cNumber": 80, "category": 2, "name": "D2"},
            {"cNumber": 80, "category": 3, "name": "E2"},
            {"cNumber": 80, "category": 3, "name": "F2"},
        ],
        "links": [
            {"name": "TO", "source": "B1", "target": "A1"},
            {"name": "TO", "source": "C1", "target": "B1"},
            {"name": "TO", "source": "D1", "target": "B1"},
            {"name": "TO", "source": "E1", "target": "D1"},
            {"name": "TO", "source": "F1", "target": "D1"},
            {"name": "TO", "source": "B2", "target": "A2"},
            {"name": "TO", "source": "C2", "target": "B2"},
            {"name": "TO", "source": "D2", "target": "B2"},
            {"name": "TO", "source": "E2", "target": "D2"},
            {"name": "TO", "source": "F2", "target": "D2"},
            {"name": "TO", "source": "F2", "target": "D1"},
        ]
    }
    return render_template('graph_external.html', gdata = graphDataPy)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)