from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_homepage_loads():
    response = client.get('/')
    assert response.status_code == 200
    assert 'EduGenie' in response.text

def test_health_endpoint():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'

def test_empty_input_is_rejected():
    response = client.post('/api/task', json={'task': 'qa', 'text': ''})
    assert response.status_code == 422
