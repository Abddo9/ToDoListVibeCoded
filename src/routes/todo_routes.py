from flask import Blueprint, render_template, request, jsonify
from ..models.todo import Todo
from .. import db

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    return render_template('index.html')

# API endpoint to get all todos
@todo_bp.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'is_completed': todo.is_completed
    } for todo in todos])

# API endpoint to add a new todo
@todo_bp.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    title = data.get('title', '').strip()
    if title:
        new_todo = Todo(title=title, is_completed=False)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({
            'id': new_todo.id,
            'title': new_todo.title,
            'is_completed': new_todo.is_completed
        }), 201
    return jsonify({'error': 'Title is required'}), 400

# API endpoint to update a todo
@todo_bp.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    if 'title' in data:
        todo.title = data['title'].strip()
    if 'is_completed' in data:
        todo.is_completed = data['is_completed']
    db.session.commit()
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'is_completed': todo.is_completed
    })

# API endpoint to delete a todo
@todo_bp.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'}), 200