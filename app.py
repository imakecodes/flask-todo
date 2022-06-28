from flask import Flask, jsonify, request 
import json
from uuid import uuid4

app = Flask(__name__)


# http://localhost:5000/
@app.route('/')
def hello():
    return 'Hello World!'


# http://localhost:5000/todos
@app.route('/todos', methods=['POST'])
def todos():
    """
    POST: 
    Receber a requisição do cliente e adicionar a tarefa a lista de tarefas

    GET: 
    Retornar a lista de tarefas contida no arquivo
    """

    # abrir o arquivo taferas.json em modo somente leitura "r"
    # e disponibilizar um ponteiro de leitura chamado f
    with open("tarefas.json", "r") as f:
        content = f.read()
        todos = json.loads(content)

    # receber o conteúdo do corpo da requisição
    data_request = request.get_json()
    todos[str(uuid4())] = data_request["task"]
    
    # abrir o arquivo taferas.json em modo somente escrita "w"
    # e disponibilizar um ponteiro de escrita chamado f
    with open("tarefas.json", "w") as f:
        f.write(json.dumps(todos, indent=4))
    
    return jsonify(todos)

# http://localhost:5000/todos/:id
@app.route('/todos/<id>', methods=['GET'])
def todos_single(id):
    """
    GET: 
    Retornar a tarefa com o id especificado
    """

    # abrir o arquivo taferas.json em modo somente leitura "r"
    # e disponibilizar um ponteiro de leitura chamado f
    with open("tarefas.json", "r") as f:
        content = f.read()
        todos = json.loads(content)

    # retornar a tarefa com o id especificado
    return jsonify({"task": todos[id]})