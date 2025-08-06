
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

# Inisialisasi Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi database
db = SQLAlchemy(app)

# Inisialisasi login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(users_id):
    from app.models import User
    return User.query.get(int(users_id))

# Inisialisasi Flask-Migrate
from flask_migrate import Migrate
migrate = Migrate(app, db)

# Import routes setelah semua konfigurasi
from app import routes, models

