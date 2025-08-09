import pytest 
from app import create_app

@pytest.fixture()
def app():
    app = create_app()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_login(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_home(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Home' in response.data

def test_profile(client):
    response = client.get('/profile')
    assert response.status_code == 200
    assert b'Walter White' in response.data