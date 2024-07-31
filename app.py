# import pygame

# # Initialiser Pygame et le joystick
# pygame.init()
# pygame.joystick.init()

# # Assurer qu'au moins un joystick est connecté
# if pygame.joystick.get_count() > 1:
#     print("Aucun joystick détecté !")
#     pygame.quit()
#     exit()

# # Créer un objet Joystick pour le premier joystick connecté
# joycon = pygame.joystick.Joystick(0)
# joycon.init()

# try:
#     while True:
#         for event in pygame.event.get():
#             # Détecter les appuis sur les boutons
#             if event.type == pygame.JOYBUTTONDOWN:
#                 print(f"Bouton {event.button} appuyé")
#             if event.type == pygame.JOYBUTTONUP:
#                 print(f"Bouton {event.button} relâché")

# finally:
#     # Désinitialiser Pygame à la fermeture du programme
#     pygame.quit()

# import pygame

# # Initialiser Pygame et le module joystick
# pygame.init()
# pygame.joystick.init()

# # Vérifier le nombre de joysticks connectés
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("Aucun joystick détecté !")
#     pygame.quit()
#     exit()

# # Créer des objets Joystick pour chaque joystick connecté
# joysticks = [pygame.joystick.Joystick(i) for i in range(joystick_count)]
# for joystick in joysticks:
#     joystick.init()
#     print(f"Joystick {joystick.get_name()} initialisé.")

# try:
#     while True:
#         for event in pygame.event.get():
#             # Gérer les événements de boutons pour tous les joysticks
#             if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
#                 # Vérifier que l'indice du joystick est valide
#                 if event.joy < joystick_count:
#                     action = "appuyé" if event.type == pygame.JOYBUTTONDOWN else "relâché"
#                     print(f"Joystick {event.joy} : Bouton {event.button} {action}")
#                 else:
#                     print(f"Événement reçu pour un joystick non reconnu : {event.joy}")
# finally:
#     # Désinitialiser Pygame à la fermeture du programme
#     pygame.quit()


import pygame

# Initialiser Pygame et le module joystick
pygame.init()
pygame.joystick.init()

# Vérifier le nombre de joysticks connectés
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Aucun joystick détecté !")
    pygame.quit()
    exit()

# Créer des objets Joystick pour chaque joystick connecté
joysticks = [pygame.joystick.Joystick(i) for i in range(joystick_count)]
for joystick in joysticks:
    joystick.init()
    print(f"Joystick {joystick.get_name()} initialisé.")

try:
    while True:
        for event in pygame.event.get():
            if event.type in [pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP]:
                if event.joy < len(joysticks):
                    action = "appuyé" if event.type == pygame.JOYBUTTONDOWN else "relâché"
                    print(f"Joystick {event.joy} : Bouton {event.button} {action}")
                else:
                    print(f"Erreur: Événement reçu pour joystick non initialisé (index {event.joy})")
finally:
    pygame.quit()

