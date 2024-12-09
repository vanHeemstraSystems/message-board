# server/src/message_board/utils/app_utils.py
from flask import Flask, jsonify
from config import DevelopmentConfig as Config # DevelopmentConfig | ProductionConfig

def create_app(config=Config):
    """Create and configure the Flask application"""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Message Board Server!", "status": "healthy"})

    @app.route('/health')
    def health_check():
        return jsonify({
            "status": "ok",
            "environment": app.config.get('ENV', 'Not Set')
        })

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)

    return app
