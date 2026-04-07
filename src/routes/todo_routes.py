from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.todo import Todo
from .. import db

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@todo_bp.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            new_todo = Todo(title=title, is_completed=False)
            db.session.add(new_todo)
            db.session.commit()
            flash('Todo item added successfully!', 'success')
            return redirect(url_for('todo.index'))
    return render_template('add_todo.html')

@todo_bp.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.title = request.form.get('title')
        todo.is_completed = 'is_completed' in request.form
        db.session.commit()
        flash('Todo item updated successfully!', 'success')
        return redirect(url_for('todo.index'))
    return render_template('edit_todo.html', todo=todo)

@todo_bp.route('/delete/<int:todo_id>', methods=['GET', 'POST'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        db.session.delete(todo)
        db.session.commit()
        flash('Todo item deleted successfully!', 'success')
        return redirect(url_for('todo.index'))
    return render_template('delete_todo.html', todo=todo)