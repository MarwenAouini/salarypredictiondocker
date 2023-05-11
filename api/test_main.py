import pytest
from fastapi.testclient import TestClient
import pytest
import requests
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

# Test d'intégration pour l'API
def test_integration():
    # Faites une requête POST pour prédire le salaire avec une valeur d'expérience donnée
    url = 'http://localhost:8000/predict'
    data = {
        'experience': 5.0
    }
    response = requests.post(url, json=data)
    
    # Vérifiez que la réponse est un succès (code HTTP 200)
    assert response.status_code == 200
    
    # Vérifiez la valeur de la réponse
    json_response = response.json()
    assert 'estimated_salary' in json_response
    assert isinstance(json_response['estimated_salary'], float)