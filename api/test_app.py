from app import app


def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
