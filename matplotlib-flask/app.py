from io import BytesIO
import random

import numpy as np
import seaborn as sns

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

<div>
<img style="border: 1px dotted red" src="/example1.png" />
</div>

<div>
<img style="border: 1px dotted red" src="/example2.png" />
</div>

</body>
</html>
"""

@app.route('/example1.png')
def example1():
    fig, ax = plt.subplots()
    draw1(ax)
    return nocache(fig_response(fig))

def draw1(ax):
    """Draw a random scatterplot"""
    x = [random.random() for i in range(100)]
    y = [random.random() for i in range(100)]
    ax.scatter(x, y)
    ax.set_title("Random scatterplot")

@app.route('/example2.png')
def example2():
    """Draw a hexbin with marginals

    From https://seaborn.pydata.org/examples/hexbin_marginals.html
    """
    sns.set(style='ticks')
    rs = np.random.RandomState(11)
    x = rs.gamma(2, size=1000)
    y = -.5 * x + rs.normal(size=1000)
    plot = sns.jointplot(x, y, kind='hex', color='#4CB391')
    # fig = plot.get_figure()
    fig = plot.fig
    return nocache(fig_response(fig))

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
