# import bluetooth

# def find_nintendo_devices():
#     devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
#     nintendo_devices = []
#     for addr, name in devices:
#         if "Joy-Con (R)" in name:  # Filtre par nom pour les Joy-Con droit
#             nintendo_devices.append((addr, name))
#     return nintendo_devices

# nintendo_devices = find_nintendo_devices()
# for addr, name in nintendo_devices:
#     print(f"Nintendo Device Found: {name} with MAC Address: {addr}")

# def connect_and_read(device_address):
#     # UUID pour le profil RFCOMM
#     uuid = "00001101-0000-1000-8000-00805F9B34FB"
#     service_matches = bluetooth.find_service(uuid=uuid, address=device_address)

#     if service_matches:
#         first_match = service_matches[0]
#         port = first_match['port']
#         name = first_match['name']
#         host = first_match['host']

#         sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#         try:
#             sock.connect((host, port))
#             data = sock.recv(1024)
#             print("Received:", data)
#         finally:
#             sock.close()
#     else:
#         print("No services found for this device.")

import bluetooth
import re

def find_nintendo_devices():
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    nintendo_devices = []
    for addr, name in devices:
        if "Joy-Con" in name: 
            nintendo_devices.append((addr, name))
    return nintendo_devices

nintendo_devices = find_nintendo_devices()
for addr, name in nintendo_devices:
    print(f"Nintendo Device Found: {name} with MAC Address: {addr}")

# def connect_and_read(device_address):
#     uuid = "00001101-0000-1000-8000-00805F9B34FB"
#     service_matches = bluetooth.find_service(uuid=uuid, address=device_address)

#     if service_matches:
#         first_match = service_matches[0]
#         port = first_match['port']
#         name = first_match['name']
#         host = first_match['host']

#         sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#         try:
#             sock.connect((host, port))
#             print(f"Connected to {name} on {host}:{port}")
#             try:
#                 while True:  # Continue à lire tant que la connexion est active
#                     data = sock.recv(1024)
#                     if not data:
#                         break  # Arrête la boucle si aucune donnée n'est reçue
#                     print("Received:", data)
#             except KeyboardInterrupt:
#                 print("Reception stopped by user.")
#         finally:
#             sock.close()
#             print("Connection closed.")
#     else:
#         print("No services found for this device.")

# if nintendo_devices:
#     connect_and_read(nintendo_devices[0][0])
