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
    html = """
<div hx-target="this" hx-swap="outerHTML">
    <h3>Work</h3>
    <button hx-post="/example2-start">
        Start
    </button>
</div>
"""
    return render_template('example2.html', html=html)


@app.route('/example2-start', methods=['POST'])
def example2_start():
    resp = Response("""
<div hx-trigger="done" hx-get="/example2-done" hx-swap="outerHTML" hx-target="this">
  <h3>Working...</h3>
  <span id="loader" class="loader"></span>
  <div hx-get="/example2-progress" hx-trigger="every 1s" hx-target="this" hx-swap="innerHTML"></div>
</div>
""")
    return resp


counter = 0  # hack to track progress

@app.route("/example2-progress")
def example2_progress():
    resp = Response("")
    global counter
    counter = counter + 1
    if counter % 5 == 0:
        resp.headers['HX-Trigger'] = 'done'
    return resp


@app.route("/example2-done")
def example2_done():
    resp = Response("""
<div hx-target="this" hx-swap="outerHTML">
    <h3>Work Finished</h3>
    <button hx-post="/example2-start">
        Restart
    </button>
</div>
""")
    return resp

if __name__ == '__main__':
    app.run(debug=True)
