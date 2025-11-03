from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 👇 Cho phép Flask trả về file mp3 nằm cùng cấp app.py
@app.route('/HonLaBan.mp3')
def serve_music():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'HonLaBan.mp3')

if __name__ == '__main__':
    app.run(debug=True)

