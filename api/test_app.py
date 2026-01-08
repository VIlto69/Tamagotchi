from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien et que les données sont correctes"""
    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 200
        data = response.get_json()
        assert data is not None

        assert "name" in data
        assert "hunger" in data
        assert "happiness" in data
        assert 0 <= data["hunger"] <= 100
        assert 0 <= data["happiness"] <= 100
