from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/REBEL HEART.mp3')
def serve_music():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'REBEL HEART.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
