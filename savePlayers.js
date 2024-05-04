const fs = require('fs');

// Récupérer les données envoyées depuis le formulaire HTML
const formData = JSON.parse(process.argv[2]);

// Convertir les données en format texte
const dataToWrite = JSON.stringify(formData, null, 2);

// Écrire les données dans un fichier texte
fs.writeFile('./joueurs.txt', dataToWrite, (err) => {
  if (err) throw err;
  console.log('Les données des joueurs ont été enregistrées dans joueurs.txt');
});
