"""
Example cribbed mostly from https://pythonhosted.org/latex/
"""

from flask import Flask
from jinja2 import FileSystemLoader
from latex import build_pdf
from latex.jinja2 import make_env


app = Flask(__name__)

env = make_env(loader=FileSystemLoader('.'))

@app.route('/')
def home():
    template = env.get_template('ex2.latex')
    pdf = build_pdf(template.render(name='Alice'))
    return bytes(pdf), 200, {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'inline; filename="report.pdf"'}

