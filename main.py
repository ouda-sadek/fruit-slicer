 ##################################  The main file that launches the game and manages the main loop  ######################################
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


# The main function that runs the game
def main():
    # Initialize pygame
    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   #, pygame.HWSURFACE | pygame.DOUBLEBUF) 
    pygame.display.set_caption("Fruit Slicer Game")
    # Create the Clock object to control game speed
    clock = pygame.time.Clock()
    # The game starts with the menu
    current_state = Menu(screen)
    print("Starting with Menu state")

    # Main loop
    running = True
    while running:
        print(f"Current state: {current_state.__class__.__name__}")
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit event detected")
                running = False 

            # Event handling current state
            current_state.handle_events(event)

        # Update current state
        next_state = current_state.update()
        print(f"Next state: {next_state}")

        # If state changed
        if next_state:
            if next_state == "menu":
                print("Changing to Menu")
                current_state = Menu(screen)
            elif next_state == "play":
                print("Changing to GameState")
                current_state = GameState(screen)
            elif next_state == "game_over":
                print("Changing to GameOver")
                game_score = current_state.get_score()
                current_state = GameOver(screen, game_score)
            elif next_state == "replay":
                print("Changing to GameState (Replay)")  
                current_state = GameState(screen) 
            elif next_state == "exit":
                print("Exiting game")
                running = False
            else:
                raise ValueError(f"Invalid next state: {next_state}")

        screen.fill(BLACK)
        current_state.update()            
         # Draw current state
        current_state.draw()
        #current_state.update()   
        pygame.display.flip()
        # Limit the game speed
        clock.tick(FPS)
    
    # Exit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() 
