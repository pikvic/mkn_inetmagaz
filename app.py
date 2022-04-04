import sqlite3
from flask import Flask, render_template


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
items = conn.execute('SELECT * FROM items').fetchall()
conn.close()
print(items)

app = Flask(__name__)


@app.get("/")
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.get("/items/<name>")
def get_item(name: str):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE name=?', (name,)).fetchone()
    conn.close()
    if not item:
        return 404, "Not Found"
    return render_template('item.html', item=item)