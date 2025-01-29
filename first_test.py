import pygame
import os
from PIL import Image
import numpy as np

# Paramètres d'opacité (0 = transparent, 100 = opaque)
opacity_percent = 50  # Change cette valeur pour ajuster l'opacité

# Charger et modifier l'image avec Pillow (PIL)
image_path = "background3.webp"  # Chemin de ton image
image = Image.open(image_path).convert("RGBA")  # Assure le mode RGBA

# Convertir en tableau NumPy
array = np.array(image)

# Modifier l'opacité
alpha_value = int(255 * (opacity_percent / 100))  # Convertit le % en alpha (0-255)
array[:, :, 3] = alpha_value  # Applique l'opacité sur tout l'image

# Reconvertir en image et sauvegarder temporairement
new_image = Image.fromarray(array)
modified_image_path = "background_opacity.png"  # Sauvegarde temporaire
new_image.save(modified_image_path)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((750, 650))
clock = pygame.time.Clock()
running = True

# Charger l'image modifiée avec Pygame
background_image = pygame.image.load(modified_image_path)
background_image = pygame.transform.scale(background_image, (750, 650))

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran et afficher l'image de fond
    screen.fill("black")
    screen.blit(background_image, (0, 0))

    # Affichage de l'image modifiée
    pygame.display.flip()
    clock.tick(60)  # Limite à 60 FPS

pygame.quit()
