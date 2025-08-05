import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wutdehelll'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:G-Chanmybeloved@localhost/db_auth'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
