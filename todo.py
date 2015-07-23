import sqlite3
from bottle import route, run, debug, template, request, error
from Task import Task

todo = Task()

@route('/todo')
def display_todo():
    return todo.todo_list()

@route('/new', method='GET')
def new_item():
    return todo.new_item()

@route('/edit/<no:int>', method='GET')
def edit_item(no):
    return todo.edit_item(no)

@route('/delete/<no:int>', method='GET')
def delete_item(no):
    return todo.delete_item(no)

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

debug(True)
run(reloader=True)