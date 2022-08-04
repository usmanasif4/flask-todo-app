from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import ToDo, ToDoComment

########################################################################
### ToDo CRUD operations
########################################################################

@app.route('/todo/<int:id>/', methods=['PUT', 'DELETE', 'GET'])
def todo(id):
  if request.method == 'PUT':
    todo_object = ToDo.query.get(id)
    if todo_object is not None:
      todo_object.todo = request.form['todo_content']
      todo_object.updated_at=datetime.now()
      db.session.commit()
      return todo_object.as_dict(), 200
  elif request.method == 'GET':
    todo_object = ToDo.query.get(id)
    return todo_object.as_dict(), 200
  elif request.method == 'DELETE':
    todo_object = ToDo.query.get(id)
    db.session.delete(todo_object)
    db.session.commit()
    return { 'Status': 'ToDo item deleted with id: %s' % todo_object.id, 'object': todo_object.as_dict() }



@app.route('/todo/', methods=['POST','GET'])
def todos_index():
	if request.method == 'GET':
		todos_list = ToDo.query.all()
		return [item.as_dict() for item in todos_list], 200
	elif request.method == 'POST':
		todo_content = request.form['todo_content']
		if todo_content:
			todo_object = ToDo(todo=todo_content, created_at=datetime.now(), updated_at=datetime.now())
			db.session.add(todo_object)
			db.session.commit()
			return todo_object.as_dict(), 200


########################################################################
### Comments CRUD operations
########################################################################

@app.route('/todo/<int:id>/comments/', methods=['POST','GET'])
def comments_index(id):
	if request.method == 'GET':
		todo_object = ToDo.query.get(id)
		return [item.as_dict() for item in todo_object.comments.all()], 200

	elif request.method == 'POST':
		comment_content = request.form['todo_comment']
		todo_object = ToDo.query.get(id)
		if (todo_object and comment_content):
			todo_comment = ToDoComment(comment=comment_content, todo=todo_object, created_at=datetime.now(), updated_at=datetime.now())
			db.session.add(todo_comment)
			db.session.commit()
			return todo_comment.as_dict(), 200


@app.route('/todo/<int:todo_id>/comments/<int:id>/', methods=['PUT', 'DELETE', 'GET'])
def comment(todo_id, id):
  if request.method == 'PUT':
    todo_comment = ToDoComment.query.get(id)
    if todo_comment is not None:
      todo_comment.comment = request.form['todo_comment']
      todo_comment.updated_at=datetime.now()
      db.session.commit()
      return todo_comment.as_dict(), 200
  elif request.method == 'GET':
    todo_comment = ToDoComment.query.get(id)
    return todo_comment.as_dict(), 200
  elif request.method == 'DELETE':
    todo_comment = ToDoComment.query.get(id)
    db.session.delete(todo_comment)
    db.session.commit()
    return { 'Status': 'Comment item deleted with id: %s' % todo_comment.id, 'object': todo_comment.as_dict() }



#################################
### Application Startup
#################################

if __name__ == '__main__':
  app.run()