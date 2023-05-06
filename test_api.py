import json
from app import app
from db import users

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'message': 'Welcome to my API!'}

def test_get_all_users():
    response = app.test_client().get('/users')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'users': users}

def test_get_user():
    response = app.test_client().get('/users/1')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'user': {"id": 1, "name": "John Doe"}}

def test_update_user():
    data = {'id': 1, 'name': 'Maria Gonzalez'}
    response = app.test_client().put('/users/1', json=data)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'message': 'User updated successfully!'}

def test_delete_user():
    response = app.test_client().delete('/users/1')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'message': 'User deleted successfully!'}
