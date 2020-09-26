from flask import Flask, request, send_from_directory, render_template, g
import locales
import sqlite3

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.debug = True

DATABASE = 'db/db.sqlite'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/assets/<path:path>')
def static_handler(path):
    return send_from_directory('assets', path)


@app.route('/route')
def route():
    frm = request.args.get("from", "0", type=int)
    id  = request.args.get("id", "", type=int)

    description = locales.NO_ROUTE_AVAILABLE
    floor = -1

    app.logger.warn("From: {} to: {}".format(frm, id))

    res = query_db("SELECT \"from\",\"to\",floor,route_description FROM ROUTES WHERE \"from\" = ? AND \"to\" = ?", [frm, id])
    if len(res) != 0:
        res = res[0] # select first object from request
        if res[3] and res[3] != "":
            description = res[3]
        floor = res[2]

    return render_template("route.html", description=description, floor=floor)


@app.route('/', methods=['GET'])
def default_route():
    query = request.args.get("q", "")
    has_query = query != ""
    results = []
    if has_query:
        query = '%{}%'.format(query.lower())
        res = query_db("SELECT title,author,some_shit,room_id FROM BOOKS WHERE title like ? OR author like ?", [query, query])
        for r in res:
            d = {}
            d['title'] = r[0].capitalize()
            d['author'] = r[1].capitalize()
            d['zhanr'] = r[2]
            d['room_id'] = r[3]
            results.append(d)
    return render_template('index.html', any_results=has_query, data=results)
