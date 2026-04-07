from pathlib import Path

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Test_444'  # Change this to a random secret key for production
    DEBUG = True  # Set to False in production