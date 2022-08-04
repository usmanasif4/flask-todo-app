from flask_migrate import Migrate
import os
from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)


class ToDo(db.Model):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  todo = db.Column(db.Text())
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  
  comments = db.relationship("ToDoComment", backref="todo", lazy='dynamic')

  def __init__(self, todo, created_at, updated_at):
    self.todo = todo
    self.created_at = created_at
    self.updated_at = updated_at

  def __repr__(self):
    return '<id {}>'.format(self.id)
  
  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
      
      
class ToDoComment(db.Model):
  __tablename__ = 'todo_comments'
  
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String())
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  todo_id = db.Column(db.Integer, db.ForeignKey('todos.id'), nullable=False)

  def __init__(self, comment, todo, created_at, updated_at):
    self.comment = comment
    self.todo = todo
    self.created_at = created_at
    self.updated_at = updated_at

  def __repr__(self):
    return '<id {}>'.format(self.id)
  
  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  