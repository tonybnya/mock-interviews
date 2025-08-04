"""
Script Name : app.py
Description : Create a basic GET and POST API endpoints
Author      : @tonybnya
"""
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret-key-here'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')

    if not username or not password:
        flash('Provide both username and password')
        return render_template('login.html'), 400

    if username == 'tonybnya' and password == 'test':
        flash('Login successful!')
        return redirect(url_for('dashboard'))

    flash('Invalid credentials')
    return render_template('login.html'), 401
