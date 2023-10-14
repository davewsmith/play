from flask import Flask
from flask import render_template
from flask import Response

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


@app.route('/example2-start', methods=['POST'])
def example2_start():
    resp = Response("""
<h3>Started</h3>
<span class="loader"></span>
""")
   return resp



if __name__ == '__main__':
    app.run(debug=True)
