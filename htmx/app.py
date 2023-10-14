from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/example1')
def example1():
    return render_template('example1.html')


@app.route('/clicked', methods=['POST'])
def clicked():
    return render_template('example1-clicked.html')


@app.route('/example2')
def example2():
    return render_template('example2.html')


if __name__ == '__main__':
    app.run(debug=True)
