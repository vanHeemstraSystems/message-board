# src/message_board/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'development_secret_key')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig
    return DevelopmentConfig
