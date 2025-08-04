"""
Script Name : url_building.py
Description : URL Building
Author      : @tonybnya
"""
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return "index"


@app.route('/login')
def login() -> str:
    return 'login'


@app.route('/user/<username>')
def profile(username: str) -> str:
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='tonybnya'))

