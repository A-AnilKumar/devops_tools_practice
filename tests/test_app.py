import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'healthy'

def test_create_todo(client):
    res = client.post('/todos', json={'title': 'Learn Jenkins'})
    assert res.status_code == 201
    assert res.get_json()['title'] == 'Learn Jenkins'

def test_create_todo_missing_title(client):
    res = client.post('/todos', json={})
    assert res.status_code == 400

def test_get_todos(client):
    client.post('/todos', json={'title': 'Learn pipelines'})
    res = client.get('/todos')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)
