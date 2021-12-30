from flask import Flask, send_from_directory
from flask_restful import Api

from api import Ticker


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('static/css', path)


@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static/js/', path)


api.add_resource(Ticker, '/api/tick')
