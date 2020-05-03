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
<br />
<a href="/base">Base page</a><br />
<a href="/dashboard1">Dashboard 1</a><br />
<a href="/login">Login</a><br />
</html>
"""

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route("/dashboard1")
def dashboard():
    return render_template('dashboard1.html')

@app.route('/login')
def login():
    return render_template('login.html')

