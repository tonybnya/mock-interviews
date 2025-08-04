"""
Script Name : app.py
Description : Create a basic file upload endpoint
Author      : @tonybnya
"""
from flask import Flask, flash, render_template, request

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret-key-here'

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    if 'file' not in request.files:
        flash('No file part')
        return render_template('upload.html'), 400

    file = request.files.get('file')

    if file is None or file.filename == '':
        flash('No file selected')
        return render_template('upload.html'), 400

    if file.content_type == 'text/plain':
        try:
            content = file.read().decode('utf-8')
            flash('File uploaded successfully!')
            return content
        except UnicodeDecodeError:
            flash('Error: Could not decode file as text')
            return render_template('upload.html'), 400
    else:
        flash(f'Unsupported file type: {file.content_type}. Only text files are supported.')
        return render_template('upload.html'), 400
