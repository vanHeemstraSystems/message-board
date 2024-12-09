# src/message_board/app.py
from flask import Flask, jsonify

def create_app(config_class=None):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    if config_class is None:
        from .config import get_config
        config_class = get_config()
    
    app.config.from_object(config_class)

    @app.route('/')
    def home():
        return jsonify({
            "message": "Welcome to the Message Board Server!",
            "status": "healthy"
        })

    @app.route('/health')
    def health_check():
        return jsonify({
            "status": "ok",
            "environment": app.config.get('ENV', 'Not Set')
        })

    return app
