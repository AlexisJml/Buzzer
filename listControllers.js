const HID = require('node-hid');
const devices = HID.devices();

console.log("Périphériques HID connectés:");
devices.forEach(device => {
    console.log(`Device: ${device.product}, Vendor ID: ${device.vendorId}, Product ID: ${device.productId}`);
});
