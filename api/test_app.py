from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien et que les données sont correctes"""
    client = app.test_client()
    response = client.get("/")

    # Vérifie le code HTTP
    assert response.status_code == 200,(
         "La réponse HTTP doit être 200"
    )

    # Vérifie que le type de contenu est JSON
    assert response.content_type == "application/json",(
         "Le content-type doit être JSON"
    )

    # Vérifie que la réponse contient les champs attendus
    data = response.get_json()
    assert "name" in data,(
         "La réponse doit contenir 'name'"
    )
    assert "hunger" in data,(
         "La réponse doit contenir 'hunger'"
         )
    assert "happiness" in data,(
         "La réponse doit contenir 'happiness'"
    )

    # Vérifie que les valeurs sont dans la plage attendue
    assert 0 <= data["hunger"] <= 100,(
         "La faim doit être entre 0 et 100"
    )
    assert 0 <= data["happiness"] <= 100,(
         "Le bonheur doit être entre 0 et 100"
    )
