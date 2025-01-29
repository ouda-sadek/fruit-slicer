 ##################################  The main file that launches the game and manages the main loop  ######################################

import sys
import pygame
from pygame.locals import *
from os import *
from config import *
from game.states.menu import Menu
from game.states.game_state import GameState
from game.states.game_over import GameOver

# Load assets
def main():
    # Initialize pygame
    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fruit Slicer Game")
    # Create the Clock object to control game speed
    clock = pygame.time.Clock()

    # The game starts with the menu
    current_state = Menu(screen)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Event handling current state
            current_state.handle_events(event)

        # Update current state
        next_state = current_state.update()

        # If state changed
        if next_state:
            if next_state == "menu":
                current_state = Menu(screen)
            elif next_state == "play":
                current_state = GameState(screen)
            elif next_state == "game_over":
                current_state = GameOver(screen)
            elif next_state == "exit":
                running = False
            else:
                raise ValueError(f"Invalid next state: {next_state}")
                    
            
        current_state.update()    
        # Draw current state
        current_state.draw()
        pygame.display.flip()

        # Limit the game speed
        clock.tick(FPS)
    
    # Exit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() 

"""import pygame
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))  # Créer une fenêtre
    pygame.display.set_caption("Test Pygame")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Remplir l'écran de noir
        screen.fill((0, 0, 0))

        # Dessiner un cercle rouge au centre de l'écran
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

        # Actualiser l'écran
        pygame.display.flip()

        clock.tick(60)  # Limiter à 60 FPS

    pygame.quit()  # Terminer Pygame proprement
    sys.exit()

if __name__ == "__main__":
    main()   """

"""import pygame
import sys
import os

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))  # Créer une fenêtre
    pygame.display.set_caption("Test Fruits")

    # Charger une image de fruit (par exemple, une pomme)
    try:
        

# Utilisation du chemin relatif depuis le répertoire courant
        image_path = "assets/images/apple.png"
        print(f"Tentative de chargement de l'image : {image_path}")

# Charge l'image directement sans utiliser os.getcwd()
        fruit_image = pygame.image.load(image_path).convert_alpha()

        #image_path = "assets/images/apple.PNG"
        #print(f"Tentative de chargement de l'image : {image_path}")

# Charge l'image directement sans utiliser os.getcwd()
        #fruit_image = pygame.image.load(image_path).convert_alpha()
        # Affiche le chemin absolu du fichier avant de le charger
        #image_path = os.path.join(os.getcwd(), "assets/images/apple.PNG")
        #print(f"Tentative de chargement de l'image : {image_path}")

        #fruit_image = pygame.image.load(image_path).convert_alpha()
        #fruit_image = pygame.image.load("assets/images/apple.PNG").convert_alpha()
        #fruit_image = pygame.image.load("/Users/rs_5/Desktop/laplateforme/IA/Fruit-slicer/assets/images/apple.PNG").convert_alpha()

    except pygame.error as e:
        print(f"Erreur de chargement de l'image : {e}")
        pygame.quit()
        sys.exit()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Remplir l'écran de noir
        screen.fill((0, 0, 0))

        # Afficher l'image du fruit à une position donnée (exemple : au centre de l'écran)
        screen.blit(fruit_image, (350, 250))

        # Actualiser l'écran
        pygame.display.flip()

        clock.tick(60)  # Limiter à 60 FPS

    pygame.quit()  # Terminer Pygame proprement
    sys.exit()

if __name__ == "__main__":
    main()
"""    """
import pygame
from game.states.game_state import GameState

def main():
    # Initialisation de Pygame
    pygame.init()

    # Configuration de la fenêtre
    SCREEN_WIDTH = 800  # Largeur de la fenêtre
    SCREEN_HEIGHT = 600  # Hauteur de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Créer la fenêtre
    pygame.display.set_caption("Fruit Slicer")  # Ajouter un titre à la fenêtre

    # Création de l'état du jeu
    game_state = GameState(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_state.handle_events(event)

        # Mise à jour de l'état du jeu
        game_state.update()

        # Dessiner l'écran
        game_state.draw()

        # Actualiser l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()

if __name__ == "__main__":
    main()"""
