# tests/test_app.py
import pytest
from flask_application.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns a 200 status and correct message"""
    response = client.get('/')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['message'] == "Welcome to the Message Board Server!"
    assert data['status'] == "healthy"

def test_health_check(client):
    """Test the health check route"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == "ok"
