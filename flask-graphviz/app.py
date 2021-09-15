import subprocess

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    with open('test.svg', 'r') as f:
        svg = f.read()
    return render_template('index.html', svg=svg, msg='From file')

@app.route('/popen')
def with_popen():
    cmd = ['dot', '-Tsvg']
    input = 'digraph { a->b }'.encode()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate(input)
    svg = out.decode('utf-8')
    return render_template('index.html', svg=svg, msg='From Popen')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
