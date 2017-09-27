from io import BytesIO
import random

from flask import Flask, send_file

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# styling. enable only one.
plt.style.use('seaborn')
# plt.style.use('fivethirtyeight')
# plt.xkcd()

app = Flask(__name__)


@app.route('/')
def frontpage():
    return """
<!doctype html>
<head><title>matplotlib</title></head>
<body>
<img style="border: 1px dotted red" src="/example1.png" />
</body>
</html>
"""

@app.route('/example1.png')
def example1():
    fig, ax = plt.subplots()
    draw(ax)
    return nocache(fig_response(fig))

def draw(ax):
    """Draw a random scatterplot"""
    x = [random.random() for i in range(100)]
    y = [random.random() for i in range(100)]
    ax.scatter(x, y)
    ax.set_title("Random scatterplot")

def fig_response(fig):
    """Turn a matplotlib Figure into Flask response"""
    img_bytes = BytesIO()
    fig.savefig(img_bytes)
    img_bytes.seek(0)
    return send_file(img_bytes, mimetype='image/png')

def nocache(response):
    """Add Cache-Control headers to disable caching a response"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response
