from app import app

def test_api_is_alive():
    """Vérifie que la page d'accueil répond bien (Code 200)"""
    client = app.test_client()
    response = client.get("/")
    
    # Vérification 1 : Le serveur répond OK
    assert response.status_code == 200
    
    # Vérification 2 (Optionnelle mais recommandée) : 
    # On vérifie que la réponse contient bien du texte (ex: du JSON ou du HTML)
    assert response.content_type == "application/json" or "text/html" in response.content_type
