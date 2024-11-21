from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
    "message": "Hello Tested App"
}

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == data
