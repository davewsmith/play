from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


@app.route('/css/<path>')
def serve_js(path):
    return send_from_directory('static/css', path)
