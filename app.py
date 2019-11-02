from flask import Flask, render_template, request, url_for
import psycopg2 as sql
from psycopg2.extras import DictCursor
from os import environ

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        con = sql.connect(environ['DATABASE_URL'])
        cur = con.cursor(cursor_factory=DictCursor)
        val = cur.execute('SELECT * FROM data')
        con.commit()
        vals = cur.fetchall()
        print(vals)
        return render_template('index.html', value=vals)
    elif request.method == 'POST':
        newval = request.form['newval']
        con = sql.connect(environ['DATABASE_URL'])
        cur = con.cursor(cursor_factory=DictCursor)
        cur.execute(
            "INSERT INTO data (key, value) VALUES ('value', %s)", (newval,))
        con.commit()
        return render_template('result.html', result="Success!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ['PORT'])
