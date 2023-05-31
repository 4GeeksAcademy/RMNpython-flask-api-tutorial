from flask import Flask, jsonify, request
# from flask import jsonify

app = Flask(__name__)

todos = [{"label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods = ['DELETE'])
def delete_todo(position):
    if postion < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return "No hay nada que borrar"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3245, debug=True)