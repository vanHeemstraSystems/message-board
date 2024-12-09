# server/src/message_board/utils/app_utils.py
from flask import Flask, jsonify
from config import DevelopmentConfig as Config # DevelopmentConfig | ProductionConfig

def create_app(config=Config):
    """Create and configure the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Message Board Server!", "status": "healthy"})

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)

    return app
