from flask import Flask, jsonify
import time
import json
import os

app = Flask(__name__)

# --- CONFIGURATION DE LA PERSISTANCE ---
# Ce fichier sera stocké dans le volume Docker
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
        "last_update": time.time()
    }

def sauvegarder_pet(data):
    """Enregistre l'état actuel sur le disque dur (Volume)."""
    # On s'assure que le dossier data existe
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def update_pet(pet):
    """Calcule l'évolution du Tamagotchi selon le temps écoulé."""
    now = time.time()
    elapsed = now - pet["last_update"]

    pet["hunger"] += elapsed * 0.1
    pet["happiness"] -= elapsed * 0.05

    # Limites de sécurité (0 à 100)
    pet["hunger"] = min(pet["hunger"], 100)
    pet["happiness"] = max(pet["happiness"], 0)
    pet["last_update"] = now
    return pet

@app.route("/state")
def get_state():
    pet = charger_pet()
    pet = update_pet(pet)
    sauvegarder_pet(pet)
    return jsonify(pet)

@app.route("/feed")
def feed():
    pet = charger_pet()
    pet = update_pet(pet)
    pet["hunger"] = max(pet["hunger"] - 20, 0)
    sauvegarder_pet(pet)
    return jsonify({"msg": "Nourri !", "pet": pet})

@app.route("/play")
def play():
    pet = charger_pet()
    pet = update_pet(pet)
    pet["happiness"] = min(pet["happiness"] + 20, 100)
    sauvegarder_pet(pet)
    return jsonify({"msg": "On joue !", "pet": pet})

@app.route("/")
def hello():
    return "API Tamagochi opérationnelle avec Persistance !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
