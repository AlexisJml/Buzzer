const HID = require('node-hid');
const nintendoVID = 0x057E;

//recherche tout les devices Nintendo
const devices = HID.devices();
const nintendoDevices = devices.filter(device => device.vendorId === nintendoVID);

console.log("Périphériques Nintendo connectés:");
nintendoDevices.forEach(device => {
    console.log(`Device: ${device.product}, Vendor ID: ${device.vendorId}, Product ID: ${device.productId}`);
});
