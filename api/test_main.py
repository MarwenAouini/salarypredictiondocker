import pytest
from fastapi.testclient import TestClient

from main import app

# Exemple (fixture) pour le client de test
@pytest.fixture
def client():
    return TestClient(app)

# Exemple (fixture) pour des données d'entrée
@pytest.fixture
def input_data():
    return {
        "experience": 5.0
    }

def test_predict_salary2():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello, I am an API!"}

# Test utilisant les exemples (fixtures)
def test_predict_salary(client, input_data):
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    assert response.json() == {"estimated_salary": 72440.66}

