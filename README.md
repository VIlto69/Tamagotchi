# 🐣 Tamagochi Dockerisé (API Python + Interface Web)

Ce projet est un **Tamagochi simple** développé avec :
- 🐍 **Python / Flask** pour l'API
- 🌐 **HTML / CSS / JavaScript** pour l'interface graphique
- 🐳 **Docker & Docker Compose** pour l'orchestration

L'interface permet d'interagir avec le Tamagochi (nourrir, jouer) et d'observer son état en temps réel.

---

## 📦 Architecture du projet

```
tamagochi/
│
├── api/                 # API Python Flask
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── web/                 # Interface graphique
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── nginx.conf
│   ├── images/
│   │   ├── happy.png
│   │   ├── sad.png
│   │   └── hungry.png
│   └── Dockerfile
│
└── docker-compose.yml
```

---

## ⚙️ Fonctionnement

- Le navigateur accède uniquement à **Nginx**
- Nginx sert l'interface graphique
- Nginx agit aussi comme **reverse proxy** vers l'API Flask (`/api/*`)
- L'API gère l'état du Tamagochi (faim, bonheur, temps)

➡️ **Aucun problème CORS**
➡️ **Architecture propre type production**

---

## 🚀 Lancement du projet

### Prérequis
- Docker
- Docker Compose

### Démarrage
Depuis le dossier racine :

```bash
docker compose down -v
docker compose build --no-cache
docker compose up -d
```

### Vérification
```bash
docker ps
```
Tu dois voir :
- `tamagochi-api`
- `tamagochi-web`

---

## 🌐 Accès

- Interface graphique :
  👉 http://localhost

- API (test direct) :
  👉 http://localhost/api/state

---

## 🎮 Fonctionnalités

- 🐣 Tamagochi avec état interne
- 🍎 Bouton **Nourrir** → réduit la faim
- 🎾 Bouton **Jouer** → augmente le bonheur
- 📊 Barres de progression animées
- 🖼 Image du Tamagochi qui change selon son état
- ⏱ Mise à jour automatique toutes les 2 secondes

---

## 🧠 Logique du jeu

- La **faim augmente** avec le temps
- Le **bonheur diminue** avec le temps
- Les valeurs sont bornées entre 0 et 100
- L'image change selon :
  - faim élevée → affamé
  - bonheur bas → triste
  - sinon → heureux

---

## 🛠 Technologies utilisées

| Élément | Technologie |
|-------|------------|
API | Python 3.11 + Flask |
Web | HTML / CSS / JavaScript |
Serveur Web | Nginx |
Conteneurisation | Docker |
Orchestration | Docker Compose |

---

## 🔮 Améliorations possibles

- 💾 Sauvegarde persistante (SQLite / PostgreSQL)
- 🧬 Évolution du Tamagochi (niveaux)
- 😴 Nouvelles actions (dormir, laver, soigner)
- 🎵 Sons et animations
- 👥 Plusieurs Tamagochis
- 🔐 Authentification utilisateur

---

## 📸 Aperçu

> Interface graphique avec boutons, barres animées et Tamagochi dynamique
<img width="1266" height="614" alt="image" src="https://github.com/user-attachments/assets/8f41b7ce-0e6a-4e30-b588-b1603d59103d" />

---

## 👤 Auteur

Projet réalisé à des fins d'apprentissage Docker / API / Web.

---

🐣 Amuse-toi bien avec ton Tamagochi !

