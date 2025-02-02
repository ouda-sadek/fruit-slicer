 ##################################  The main file that launches the game and manages the main loop  ######################################
"""import sys
import pygame
from pygame.locals import *
import os
from os import *
from config import *
from game.states.menu import Menu
from game.states.game_state import GameState
from game.states.game_over import GameOver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

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

        screen.fill(BLACK)
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
    main()    """

import sys
import pygame
from pygame.locals import *
import os
from os import *
from config import *
from game.states.menu import Menu
from game.states.game_state import GameState
from game.states.game_over import GameOver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

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
                 # Get the score from the game state
                if isinstance(current_state, GameState):
                    game_score = current_state.get_score()
                else:
                   game_score = 0
                current_state = GameOver(screen, game_score)
            elif next_state == "restart":
                current_state = GameState(screen)
            elif next_state == "back to menu":
                current_state = Menu(screen)
            elif next_state == "exit":
                running = False
            else:
                raise ValueError(f"Invalid next state: {next_state}")

        #screen.fill(BLACK) #On supprime ce fill
        current_state.draw() # On inverse draw et update
        #current_state.update() # On supprime cet update
        pygame.display.flip()
        # Limit the game speed
        clock.tick(FPS)

    # Exit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() 