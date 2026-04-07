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
    for the ToDo model and the corresponding routes.
"""

from src import create_app, db
from src.models.todo import Todo


def test_add_todo(client):
    """Test creating a new todo item via POST request to /add endpoint."""
    response = client.post('/add', data={'title': 'Test Todo', 'is_completed': False})
    assert response.status_code == 302  # Redirect after adding
    todo = Todo.query.filter_by(title='Test Todo').first()
    assert todo is not None
    assert todo.is_completed is False

def test_edit_todo(client):
    """Test editing an existing todo item via POST request to /edit/<id> endpoint."""
    todo = Todo(title='Edit Test Todo', is_completed=False)
    db.session.add(todo)
    db.session.commit()
    
    response = client.post(f'/edit/{todo.id}', data={'title': 'Updated Todo', 'is_completed': True})
    assert response.status_code == 302  # Redirect after editing
    updated_todo = Todo.query.get(todo.id)
    assert updated_todo.title == 'Updated Todo'
    assert updated_todo.is_completed is True

def test_delete_todo(client):
    """Test deleting a todo item via POST request to /delete/<id> endpoint."""
    todo = Todo(title='Delete Test Todo', is_completed=False)
    db.session.add(todo)
    db.session.commit()
    
    response = client.post(f'/delete/{todo.id}')
    assert response.status_code == 302  # Redirect after deleting
    deleted_todo = Todo.query.get(todo.id)
    assert deleted_todo is None

def test_list_todos(client):
    """Test retrieving the list of todos via GET request to / endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'ToDo List' in response.data  # Check if the title is in the response
    assert b'Add New Todo' in response.data  # Check if the add button is in the response