const express = require('express');
const HID = require('node-hid');
const app = express();
const port = 3000;

//Constante pour l'ID de vendeur de Nintendo
const nintendoVID = 0x057E;

app.use(express.static('public'));

app.get('/', (req, res) => {
    //Recherche tous les périphériques HID
    const devices = HID.devices();
    //Filtre pour obtenir uniquement les périphériques Nintendo
    const nintendoDevices = devices.filter(device => device.vendorId === nintendoVID);

    let htmlContent = `
        <html>
        <head><title>Périphériques Nintendo Connectés</title></head>
        <body>
            <h1>Périphériques Nintendo Connectés</h1>
            <ul>`;

    //Générer une liste HTML des périphériques Nintendo connectés
    nintendoDevices.forEach(device => {
        htmlContent += `<li>${device.product} - Vendor ID: ${device.vendorId}, Product ID: ${device.productId}</li>`;
    });

    htmlContent += `</ul></body></html>`;

    res.send(htmlContent);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
