import sys, platform
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 

@app.route('/signup')
def signup():
    return

@app.home('/home')
def home():
    return 

@app.route('/root')
def root():
    return