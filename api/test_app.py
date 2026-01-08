from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien et que les données sont correctes"""
    with app.test_client() as client:
        with app.app_context():
            response = client.get("/")

            # Vérifie le code HTTP
            assert response.status_code == 200

            # Récupère le JSON
            data = response.get_json()
            assert data is not None, "La réponse JSON ne doit pas être None"

            # Vérifie les champs
            assert "name" in data
            assert "hunger" in data
            assert "happiness" in data

            # Vérifie les valeurs
            assert 0 <= data["hunger"] <= 100
            assert 0 <= data["happiness"] <= 100
