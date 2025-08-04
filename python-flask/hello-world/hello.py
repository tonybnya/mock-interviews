"""
Script Name : hello.py
Description : Simple Hello World Flask application
Author      : @tonybnya
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello, World!"
