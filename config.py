import os
from datetime import timedelta

class Config:
    # --------------------------
    # Basic Flask Configuration
    # --------------------------
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')

    # --------------------------
    # Database Configuration
    # --------------------------
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///realestate.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------
    # Upload Configuration
    # --------------------------
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB max upload
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'ogg', 'pdf', 'doc', 'docx'}

    # --------------------------
    # Session Configuration
    # --------------------------
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    # --------------------------
    # Pagination
    # --------------------------
    PROPERTIES_PER_PAGE = int(os.getenv('PROPERTIES_PER_PAGE', 9))
    ADMIN_PAGE_SIZE = int(os.getenv('ADMIN_PAGE_SIZE', 20))
    USER_PAGE_SIZE = int(os.getenv('USER_PAGE_SIZE', 12))

    # --------------------------
    # Admin Credentials
    # --------------------------
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')  # Change this in production!

    # --------------------------
    # Email Configuration (Flask-Mail)
    # --------------------------
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'false').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'mandavkaratharva@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', MAIL_USERNAME)
