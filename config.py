import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wutdehelll'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:170727@localhost/lagibelajar' #pakai password postgres sendiri

    SQLALCHEMY_TRACK_MODIFICATIONS = False
