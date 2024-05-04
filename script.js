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
