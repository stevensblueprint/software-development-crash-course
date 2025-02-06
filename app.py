from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Read a book", "completed": False},
]


@app.route("/")
def hello():
    return "Welcome to the Blueprint Software Dev Crash Course!"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)
