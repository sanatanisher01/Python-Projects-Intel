import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-quicknotes'
    
    # SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///quicknotes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
