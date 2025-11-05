from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Cho phép trả file mp3
@app.route('/<filename>.mp3')
def serve_music(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), f"{filename}.mp3")

if __name__ == '__main__':
    app.run(debug=True)
