"""
Script Name : app.py
Description : Build a simple template rendering with Jinja2
Author      : @tonybnya
"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')
