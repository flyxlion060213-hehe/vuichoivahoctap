from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
from flask import send_from_directory

@app.route('/HonLaBan.mp3')
def serve_music():
    return send_from_directory('vuichoivahoctap', 'HonLaBan.mp3')


