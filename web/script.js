const apiUrl = "/api";

async function updateState() {
  const res = await fetch(`${apiUrl}/state`);
  const pet = await res.json();

  document.getElementById("name").innerText = pet.name;

  const hungerBar = document.getElementById("hunger-bar");
  hungerBar.style.width = `${pet.hunger}%`;
  hungerBar.style.background = pet.hunger > 70 ? "#ff4d4d" : "#4caf50";

  const happinessBar = document.getElementById("happiness-bar");
  happinessBar.style.width = `${pet.happiness}%`;
  happinessBar.style.background = pet.happiness < 30 ? "#ff4d4d" : "#4caf50";

  const petImg = document.getElementById("pet-img");
  if (pet.hunger > 70) {
    petImg.src = "images/hungry.png";
    petImg.className = "sad";
  } else if (pet.happiness < 30) {
    petImg.src = "images/sad.png";
    petImg.className = "sad";
  } else {
    petImg.src = "images/happy.png";
    petImg.className = "happy";
  }
}

// Actions
async function feed() {
  await fetch(`${apiUrl}/feed`);
  updateState();
}

async function play() {
  await fetch(`${apiUrl}/play`);
  updateState();
}

// Update automatique toutes les 2 secondes
setInterval(updateState, 2000);
updateState();
