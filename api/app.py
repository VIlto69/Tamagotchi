from flask import Flask, jsonify
import time
import json  
import os

app = Flask(__name__)

pet = {
    "name": "Luna",
    "hunger": 50,
    "happiness": 50,
    "last_update": time.time()
}

def update_pet():
    now = time.time()
    elapsed = now - pet["last_update"]

    pet["hunger"] += elapsed * 0.1     # devenir plus faim
    pet["happiness"] -= elapsed * 0.05 # devenir plus triste

    pet["hunger"]  = min(pet["hunger"], 100)
    pet["happiness"] = max(pet["happiness"], 0)

    pet["last_update"] = now

@app.route("/state")
def get_state():
    update_pet()
    return jsonify(pet)

@app.route("/feed")
def feed():
    update_pet()
    pet["hunger"] -= 20
    pet["hunger"] = max(pet["hunger"], 0)
    return jsonify({"msg": "Nourri !", "pet": pet})

@app.route("/play")
def play():
    update_pet()
    pet["happiness"] += 20
    pet["happiness"] = min(pet["happiness"], 100)
    return jsonify({"msg": "On joue !", "pet": pet})

@app.route("/")
def hello():
    return "API Tamagochi opérationnelle !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
