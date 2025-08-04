"""
Script Name : app.py
Description : Build a simple form handling endpoint
Author      : @tonybnya
"""
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'tonybnya' and password == 'test1234':
            return 'Login successfully!'

        return 'Invalid credentials'
