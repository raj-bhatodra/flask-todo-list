from flask import Flask, render_template, request

import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname="mydb", user="postgres",
                        password="postgres", host="0.0.0.0")


@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY id")
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)


@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (description) VALUES (%s)", [description])
    conn.commit()
    return index()


@app.route('/complete/<int:id>')
def complete(id):
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = %s WHERE id = %s", [True, id])
    conn.commit()
    return index()


if __name__ == '__main__':
    app.run(debug=True)
