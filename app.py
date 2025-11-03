from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# phục vụ file nhạc ở cùng cấp app.py
@app.route('/HonLaBan.mp3')
def music():
    return send_from_directory('.', 'HonLaBan.mp3')  # dấu '.' nghĩa là thư mục hiện tại

if __name__ == '__main__':
    app.run(debug=True)



