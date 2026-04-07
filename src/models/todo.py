from .. import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.title}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Todo.query.all()

    @staticmethod
    def get_by_id(todo_id):
        return Todo.query.get(todo_id)