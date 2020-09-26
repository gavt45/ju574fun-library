from flask import Flask, request, send_from_directory,render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('assets', path)

@app.route('/', methods=['GET', 'POST'])
def default_route():
    query = request.args.get("q", "")
    any_results = query != ""
    return render_template('index.html', any_results=any_results, data=[[query]])
