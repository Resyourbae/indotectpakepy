# Import modul-modul yang dibutuhkan
from flask import Flask                          # Modul utama Flask
from flask_sqlalchemy import SQLAlchemy          # Untuk ORM (Object Relational Mapper)
from flask_login import LoginManager             # Untuk manajemen login (autentikasi pengguna)
from config import Config                        # Konfigurasi aplikasi dari file config.py
import os                                        # Modul os digunakan untuk operasi sistem (tidak digunakan langsung di sini)

# Inisialisasi aplikasi Flask
app = Flask(__name__)                            # Membuat instance dari aplikasi Flask
app.config.from_object(Config)                   # Menggunakan konfigurasi dari objek Config

# Inisialisasi SQLAlchemy untuk menangani database
db = SQLAlchemy(app)                             # Membuat instance SQLAlchemy dengan aplikasi Flask

# Inisialisasi LoginManager untuk mengatur autentikasi
login_manager = LoginManager(app)                # Membuat instance LoginManager dan hubungkan dengan aplikasi Flask
login_manager.login_view = 'login'               # Nama endpoint view untuk login, akan digunakan saat redirect otomatis saat belum login
login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'  # Pesan yang ditampilkan jika pengguna belum login
login_manager.login_message_category = 'danger'  # Kategori pesan (bisa digunakan untuk styling seperti Bootstrap alert)

# Fungsi untuk memuat pengguna berdasarkan ID (diperlukan oleh Flask-Login)
@login_manager.user_loader
def load_user(users_id):                         # Fungsi ini akan dipanggil oleh Flask-Login untuk mengambil user dari database
    from app.models import User                  # Import model User (dalam file models.py)
    return User.query.get(int(users_id))         # Mengambil user berdasarkan ID dari database

# Inisialisasi Flask-Migrate untuk manajemen migrasi database
from flask_migrate import Migrate                # Import Flask-Migrate
migrate = Migrate(app, db)                       # Hubungkan Migrate dengan app dan db

# Import routes dan models setelah semua konfigurasi dan ekstensi siap
from app import routes, models                   # Ini penting agar tidak terjadi circular import
