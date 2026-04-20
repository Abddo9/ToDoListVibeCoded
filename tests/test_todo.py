"""
Unit tests for the ToDo List Flask application.

This module contains pytest test cases for testing the core functionality
of the ToDo List application, including:
- Creating new todo items
- Editing existing todo items
- Deleting todo items
- Listing all todo items

All tests use fixtures defined in conftest.py to provide an isolated
test environment with an in-memory SQLite database.

Test Fixtures:
    - client: Flask test client for making HTTP requests
    - app: Flask application instance with test configuration

Test Coverage:
    These tests cover the CRUD (Create, Read, Update, Delete) operations
    for the ToDo model and the corresponding routes using the new REST API.
"""

from src import create_app, db
from src.models.todo import Todo
import json


def test_add_todo(client):
    """Test creating a new todo item via POST request to /api/todos endpoint."""
    response = client.post('/api/todos', 
                          data=json.dumps({'title': 'Test Todo'}),
                          content_type='application/json')
    assert response.status_code == 201  # Created
    data = response.get_json()
    assert data['title'] == 'Test Todo'
    assert data['is_completed'] is False
    
    # Verify in database
    todo = Todo.query.filter_by(title='Test Todo').first()
    assert todo is not None

def test_edit_todo(client):
    """Test editing an existing todo item via PUT request to /api/todos/<id> endpoint."""
    # Create a todo first
    todo = Todo(title='Edit Test Todo', is_completed=False)
    db.session.add(todo)
    db.session.commit()
    
    # Update it
    response = client.put(f'/api/todos/{todo.id}',
                         data=json.dumps({'title': 'Updated Todo', 'is_completed': True}),
                         content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Updated Todo'
    assert data['is_completed'] is True
    
    # Verify in database
    updated_todo = db.session.get(Todo, todo.id)
    assert updated_todo.title == 'Updated Todo'
    assert updated_todo.is_completed is True

def test_delete_todo(client):
    """Test deleting a todo item via DELETE request to /api/todos/<id> endpoint."""
    # Create a todo first
    todo = Todo(title='Delete Test Todo', is_completed=False)
    db.session.add(todo)
    db.session.commit()
    todo_id = todo.id
    
    # Delete it
    response = client.delete(f'/api/todos/{todo_id}')
    assert response.status_code == 200
    
    # Verify it's deleted from database
    deleted_todo = db.session.get(Todo, todo_id)
    assert deleted_todo is None

def test_list_todos(client):
    """Test retrieving the list of todos via GET request to /api/todos endpoint."""
    # Create some test todos
    todo1 = Todo(title='Todo 1', is_completed=False)
    todo2 = Todo(title='Todo 2', is_completed=True)
    db.session.add_all([todo1, todo2])
    db.session.commit()
    
    # Get the API response
    response = client.get('/api/todos')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2
    
    titles = [todo['title'] for todo in data]
    assert 'Todo 1' in titles
    assert 'Todo 2' in titles