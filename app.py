from flask import Flask, request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import ToDo, ToDoComment

@app.route('/todo/<int:id>', methods=['PUT', 'DELETE', 'GET'])
def todo(id):
  if request.method == 'PUT':
    todo_object = ToDo.query.get(id)
    if todo_object is not None:
      todo_object.todo = request.form['todo-content']
      db.session.commit()
      return todo_object.as_dict(), 200
  elif request.method == 'GET':
    todo_object = ToDo.query.get(id)
    return todo_object.as_dict(), 200
  elif request.method == 'DELETE':
    todo_object = ToDo.query.get(id)
    db.session.delete(todo_object)
    db.session.commit()
    return { 'Status': 'Object deleted with id: %s' % todo_object.id, 'object': todo_object.as_dict() }



@app.route('/todo/', methods=['POST','GET'])
def index():
	if request.method == 'GET':
		todos_list = ToDo.query.all()
		return [item.as_dict() for item in todos_list], 200
	elif request.method == 'POST':
		todo_content = request.form['todo-content']
		if todo_content:
			todo_object = ToDo(todo=todo_content, created_at=datetime.now(), updated_at=datetime.now())
			db.session.add(todo_object)
			db.session.commit()
			return todo_object.as_dict(), 200
	return ''

app.debug = True

if __name__ == '__main__':
  app.run()