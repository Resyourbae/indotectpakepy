import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wutdehelll'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pw@localhost/db_nama' #pakai password postgres sendiri

    SQLALCHEMY_TRACK_MODIFICATIONS = False
