import pytest
from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"API Tamagotchi" in response.data

def test_initial_state():
    """Vérifie que l'état initial contient Luna"""
    client = app.test_client()
    response = client.get('/state')
    data = response.get_json()
    assert response.status_code == 200
    assert "name" in data