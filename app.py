from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@app.route("/items/<int:item_id>")
def get_item(item_id):
    return jsonify({"item_id": item_id, "message": "This is an item."})

if __name__ == "__main__":
    app.run()
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@app.route("/items/<int:item_id>")
def get_item(item_id):
    return jsonify({"item_id": item_id, "message": "This is an item."})

if __name__ == "__main__":
    app.run()
