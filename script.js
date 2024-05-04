//index.html
document.addEventListener('keydown', function(event) {
    // Vérifie si la touche pressée est la touche "E" (vous pouvez utiliser une autre touche selon vos préférences)
    if (event.key === 'e' || event.key === 'E') {
        // Afficher l'image
        document.getElementById('imageContainer').innerHTML = '<img src="assets/669177.png" alt="Image">';
        document.getElementById('imageContainer').style.display = 'block';

        // Temps en millisecondes pendant lequel l'image reste affichée (par exemple 5 secondes)
        var tempsAffichage = 5000;

        // Cacher l'image après le temps spécifié
        setTimeout(function() {
            document.getElementById('imageContainer').style.display = 'none';
        }, tempsAffichage);
    }
});

//params.html
let playerCount = 1;

function addPlayer() {
  playerCount++;
  const playersContainer = document.getElementById('playersContainer');
  const playerDiv = document.createElement('div');
  playerDiv.classList.add('player');
  playerDiv.innerHTML = `
    <label for="player${playerCount}">Joueur ${playerCount}</label>
    <input type="text" id="player${playerCount}" name="player${playerCount}" placeholder="Pseudo du joueur ${playerCount}">
    <label for="key${playerCount}">Touche du clavier</label>
    <input type="text" id="key${playerCount}" name="key${playerCount}" placeholder="Touche du clavier pour le joueur ${playerCount}">
    <label for="image${playerCount}">Image</label>
    <input type="file" id="image${playerCount}" name="image${playerCount}">
  `;
  playersContainer.appendChild(playerDiv);
}

