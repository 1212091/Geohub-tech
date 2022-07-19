from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    payload = {
        "code": "LDM",
        "name": "Lightdm",
        "description": "To adjust screen",
        "price": 40000,
        "platform": "Ubuntu"
    }
    response = client.post("localhost:8081/api/v1/products", json=payload)
    assert response.status_code == 201
