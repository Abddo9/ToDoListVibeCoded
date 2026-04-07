from .todo_routes import todo_bp

def init_app(app):
    app.register_blueprint(todo_bp)