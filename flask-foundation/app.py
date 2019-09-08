from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def starthere():
    return """
<!doctype html>
<head>
<style>body { font-family: sans-serif; }</style>
</head>
<html>
<a href="/static/index.html">Foundation demo (unmodified)</a><br />
</html>
"""

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')
