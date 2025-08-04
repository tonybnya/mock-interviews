"""
Script Name : url_params.py
Description : Create routes with URL parameters
Author      : @tonybnya
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return 'index'


@app.route('/<username>')
def hello(username: str) -> str:
    return f'Hello, {username.capitalize()}'


@app.route('/<int:num>')
def process_num(num: int):
    text: str = f'{num} is '
    return text + 'even' if num % 2 == 0 else text + 'odd'
