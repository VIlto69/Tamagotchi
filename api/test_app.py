from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien et que les données sont correctes"""
    client = app.test_client()
    response = client.get("/")

    # Vérifie le code HTTP
    assert response.status_code == 200

    # Vérifie que le type de contenu est JSON
    assert response.content_type == "application/json"

    # Vérifie que la réponse contient les champs attendus
    data = response.get_json()
    assert "name" in data
    assert "hunger" in data
    assert "happiness" in data

    # Vérifie que les valeurs sont dans la plage attendue
    assert 0 <= data["hunger"] <= 100
    assert 0 <= data["happiness"] <= 100
