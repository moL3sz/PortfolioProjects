import re
from flask import Flask,request,jsonify
from flask_restful import Api,Resource,abort
app = Flask(__name__)
api = Api(app)

TODOS = {
    "todo0": {"task":"Create a API for this service"},
    "todo1": {"task":"Create UI for this"}
}
def check_if_todoid_exists(todoid):
    if  todoid not in TODOS:
        abort("404")
class Todo(Resource):
    def get(self,todoid):
        check_if_todoid_exists(todoid)
        return TODOS[todoid]
    def put(self,todoid):
        task = request.form["task"]
        check_if_todoid_exists(todoid)
        TODOS[todoid] = {"task",task}
        return {todoid: TODOS[todoid]},200
    def delete(self,todoid):
        check_if_todoid_exists(todoid)
        temp = TODOS[todoid]
        del TODOS[todoid]
        return temp #return the deleted one
class TodoList(Resource):
    def get(self):
        return TODOS
    def post(self):
        latest_todoid = int(max(TODOS.keys()).lstrip("todo"))
        next_todoid = "todo%i" % (latest_todoid+1)
        TODOS[next_todoid] = {"task":request.form["task"]}
        return TODOS[next_todoid] 
api.add_resource(Todo,"/todos/<todoid>")
api.add_resource(TodoList,"/todos")

if __name__ == "__main__":
    app.run(debug=True)








