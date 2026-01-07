# Branche de développement - Projet Tamagotchi DevSecOps
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# --- CONFIGURATION DE LA PERSISTANCE ---
# Ce fichier sera stocké dans le volume Docker pour ne pas perdre les données
DATA_FILE = "data/pet.json"

def charger_pet():
    """Charge les données depuis le fichier JSON ou crée Luna par défaut."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "Luna",
        "hunger": 50,
        "happiness": 50,
        "energy": 100,
        "last_update": time.time()
    }

def sauvegarder_pet(data):
    """Enregistre l'état actuel sur le disque dur (Volume)."""
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def update_pet(pet):
    """Calcule l'évolution du Tamagotchi selon le temps écoulé."""
    now = time.time()
    elapsed = now - pet.get("last_update", now)

    # L'animal a faim et perd du bonheur avec le temps
    pet["hunger"] += elapsed * 0.1
    pet["happiness"] -= elapsed * 0.05

    # Limites de sécurité (0 à 100)
    pet["hunger"] = max(0, min(pet["hunger"], 100))
    pet["happiness"] = max(0, min(pet["happiness"], 100))
    pet["last_update"] = now
    return pet

# --- ROUTES API (CRUD) ---

@app.route("/")
def hello():
    return "API Tamagotchi opérationnelle avec Persistance !"

@app.route("/state", methods=['GET'])
def get_state():
    """READ : Voir l'état de l'animal"""
    pet = charger_pet()
    pet = update_pet(pet)
    sauvegarder_pet(pet)
    return jsonify(pet)

@app.route("/feed", methods=['POST', 'GET'])
def feed():
    """UPDATE : Action de nourrir"""
    pet = charger_pet()
    pet = update_pet(pet)
    pet["hunger"] = max(pet["hunger"] - 20, 0)
    sauvegarder_pet(pet)
    return jsonify({"msg": "Nourri !", "pet": pet})

@app.route("/play", methods=['POST', 'GET'])
def play():
    """UPDATE : Action de jouer"""
    pet = charger_pet()
    pet = update_pet(pet)
    pet["happiness"] = min(pet["happiness"] + 20, 100)
    sauvegarder_pet(pet)
    return jsonify({"msg": "On joue !", "pet": pet})

@app.route("/pet", methods=['PUT'])
def update_manual():
    """UPDATE (Manuel) : Modifier le nom ou les stats"""
    data = request.get_json()
    pet = charger_pet()
    if not data:
        return jsonify({"error": "Pas de données reçues"}), 400
    if 'name' in data:
        pet['name'] = data['name']
    sauvegarder_pet(pet)
    return jsonify(pet), 200

@app.route("/pet", methods=['DELETE']) 
def delete_pet():
    """DELETE : Réinitialiser le jeu (Exigence du sujet)"""
    default_state = {
        "name": "Luna",
        "hunger": 50,
        "happiness": 50,
        "energy": 100,
        "last_update": time.time()
    }
    sauvegarder_pet(default_state)
    return jsonify({"msg": "Animal réinitialisé !", "pet": default_state}), 200

if __name__ == "__main__":
if __name__ == "__main__":
    # Le '# nosec' dit à Bandit d'ignorer l'alerte sur l'IP 0.0.0.0
    app.run(host="0.0.0.0", port=5000)  # nosec
