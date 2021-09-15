import subprocess

from flask import Flask, render_template
import graphviz

app = Flask(__name__)

@app.route('/')
def home():
    """
    The simple case: Read from a file on disk
    """
    with open('test.svg', 'r') as f:
        svg = f.read()
    return render_template('index.html', svg=svg, msg='SVG from file')

@app.route('/popen')
def using_popen():
    """
    Invoke `dot` via subprocess.Popen, passing hand-constructed input
    """
    cmd = ['dot', '-Tsvg']
    input = 'digraph { a->b }'.encode()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate(input)
    # error checking goes here
    svg = out.decode('utf-8')
    return render_template('index.html', svg=svg, msg='Using suprocess.Popen')

@app.route('/graphviz')
def using_graphviz():
    """
    Use graphviz to construct the graph
    """
    dot = graphviz.Digraph(format='svg')
    dot.node('a')
    dot.node('b')
    dot.edge('a', 'b')
    svg = dot.pipe().decode('utf-8')
    return render_template('index.html', svg=svg, msg='Using graphviz')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
