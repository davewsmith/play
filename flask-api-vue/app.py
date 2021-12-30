from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('static/css', path)


@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static/js/', path)

ticker = 0

@app.route('/api/tick')
def tick():
    global ticker
    ticker = ticker + 1
    return {'tick': ticker}
