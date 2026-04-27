from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "title is required"}), 400
    todo = {"id": len(todos) + 1, "title": data['title'], "done": False}
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "not found"}), 404
    todo['done'] = request.get_json().get('done', todo['done'])
    return jsonify(todo), 200
