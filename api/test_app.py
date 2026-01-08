from app import app


def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien"""
    with app.test_client() as client:
        response = client.get("/")

        # Vérifie le code HTTP
        assert response.status_code == 200