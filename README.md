# Interview Assesment -> TODO List App

## Description

> A sample TODO list app built in python alongwith the following mentioned technologies:

- Python3
- Pip
- Virtualenv
- Flask
- PostgreSQL
- SQLAlchemy

## Environment variables

1. Create a .env file in root directory of the project.
2. Insert db url and config settings in .env file:
  - DATABASE_URL="postgresql:///todos_dev"
  - APP_SETTINGS="config.DevelopmentConfig"


## App setup

  * Clone the app: `git clone https://github.com/usmanasif4/flask-todo-app.git`
  * Activate Virtualenv
    1. `python -m venv venv`
    2. `source venv/bin/activate`
  * Install the dependencies: `pip install -r requirements.txt`
  * Run migrations: `flask db migrate`
  * Then run `flask run` command to start the server


## Api endpoints

* GET: To fetch all todo: `/todo/`
* POST: To create a todo: `/todo/` with post parameters => `todo_content`(string)
* GET: To fetch a single todo: `/todo/<todo-id>/`
* PUT: To update a todo: `/todo/<todo-id>/` with post parameters => `todo_content`(string)
* DELETE: To delete a todo: `/todo/<todo-id>/`


* GET: To fetch all comments: `/todo/<todo-id>/comments`
* POST: To create a comment: `/todo/<todo-id>/comments` with post parameters => `todo_comment`(string)
* GET: To fetch a single comment: `/todo/<todo-id>/comments/<comment-id>`
* PUT: To update a comment: `/todo/<todo-id>/comments/<comment-id>` with post parameters => `todo_comment`(string)
* DELETE: To delete a comment: `/todo/<todo-id>/comments/<comment-id>/`

