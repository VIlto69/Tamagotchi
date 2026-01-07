from flask import Flask, jsonify, request
import time
import json
import os

app = Flask(__name__)

DATA_FILE = "data/pet.json"


def charger_pet():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "Luna",
        "hunger": 50,
        "happiness": 50,
        "energy": 100,
        "last_update": time.time(),
    }


def sauvegarder_pet(data):
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def update_pet(pet):
    now = time.time()
    elapsed = now - pet.get("last_update", now)
    pet["hunger"] = max(0, min(pet["hunger"] + elapsed * 0.1, 100))
    pet["happiness"] = max(0, min(pet["happiness"] - elapsed * 0.05, 100))
    pet["last_update"] = now
    return pet


@app.route("/")
def hello():
    return "API Tamagotchi opérationnelle !"


@app.route("/state", methods=["GET"])
def get_state():
    pet = update_pet(charger_pet())
    sauvegarder_pet(pet)
    return jsonify(pet)


@app.route("/feed", methods=["POST", "GET"])
def feed():
    pet = update_pet(charger_pet())
    pet["hunger"] = max(pet["hunger"] - 20, 0)
    sauvegarder_pet(pet)
    return jsonify({"msg": "Nourri !", "pet": pet})


@app.route("/play", methods=["POST", "GET"])
def play():
    pet = update_pet(charger_pet())
    pet["happiness"] = min(pet["happiness"] + 20, 100)
    sauvegarder_pet(pet)
    return jsonify({"msg": "On joue !", "pet": pet})


@app.route("/pet", methods=["PUT"])
def update_manual():
    data = request.get_json()
    pet = charger_pet()
    if data and "name" in data:
        pet["name"] = data["name"]
    sauvegarder_pet(pet)
    return jsonify(pet), 200


@app.route("/pet", methods=["DELETE"])
def delete_pet():
    default_state = {
        "name": "Luna",
        "hunger": 50,
        "happiness": 50,
        "energy": 100,
        "last_update": time.time(),
    }
    sauvegarder_pet(default_state)
    return jsonify({"msg": "Réinitialisé !", "pet": default_state}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec