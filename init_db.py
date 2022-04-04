import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

items = [
    {"name": "ASDLK", "price": 1233, "description": "jsadklsaksalkjdasjjk dsasa"},
    {"name": "AdsLK", "price": 532, "description": "jsadklsaksalkjdas32jjk dsasa"},
    {"name": "asdasDLK", "price": 234, "description": "jsadklsaksalk23jdasjjk dsasa"},
    {"name": "ASsdaK", "price": 222, "description": "jsadklsaksalkjasddasjjk dsasa"},
    {"name": "ASDLasdK", "price": 12, "description": "jsadklsaksalkjasddasjjk dsasa"},
]

cur = connection.cursor()

command = "INSERT INTO items (name, price, description) VALUES (?, ?, ?)"

items = [(i["name"], i["price"], i["description"]) for i in items]

for item in items:
    cur.execute(command, item)

connection.commit()
connection.close()