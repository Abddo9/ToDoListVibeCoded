from src import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes.todo_routes import todo_bp

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from src import db
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8080)