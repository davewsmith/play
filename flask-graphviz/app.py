from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    with open('test.svg', 'r') as f:
        svg = f.read()
    return render_template('index.html', svg=svg)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
