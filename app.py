from flask import Flask, render_template

app = Flask(__name__)

items = [
    {"name": "ASDLK", "price": 1233, "description": "jsadklsaksalkjdasjjk dsasa"},
    {"name": "AdsLK", "price": 532, "description": "jsadklsaksalkjdas32jjk dsasa"},
    {"name": "asdasDLK", "price": 234, "description": "jsadklsaksalk23jdasjjk dsasa"},
    {"name": "ASsdaK", "price": 222, "description": "jsadklsaksalkjasddasjjk dsasa"},
    {"name": "ASDLasdK", "price": 12, "description": "jsadklsaksalkjasddasjjk dsasa"},
]

@app.get("/")
def index():
    return render_template('index.html', items=items)

@app.get("/items/<name>")
def get_item(name: str):
    item = [item for item in items if item["name"] == name]
    if not item:
        return 404, "Not Found"
    return render_template('item.html', item=item[0])