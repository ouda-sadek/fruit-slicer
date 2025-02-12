##################################### Class for the end of game screen.    ####################################################
import pygame
from pygame.locals import *
from config import *
from game.entities.button import Button
import os
class GameOver:
    def __init__(self, screen, score=0):
        self.screen = screen
        self.font = pygame.font.Font(None, GAME_OVER_FONT_SIZE)
        self.score = score
        self.buttons = self.create_buttons()
        self.next_state = None
        self.background = pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/images/background2.webp")))
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def create_buttons(self):
         # Space between buttons
        button_width = GAME_OVER_BUTTON_WIDTH
        button_height = GAME_OVER_BUTTON_HEIGHT

        # Define buttons position
        spacing = 50 
        start_x = SCREEN_WIDTH // 2 - (3 * button_width + 2 * spacing) // 2  
        y = SCREEN_HEIGHT // 2 + 2 * button_height  

        # cCreate 3 buttons 
        replay_button = Button(start_x, y, button_width, button_height, "Replay", self.font, GAME_OVER_BUTTON_COLOR, GAME_OVER_BUTTON_HOVER_COLOR)
        menu_button = Button(start_x + button_width + spacing, y, button_width, button_height, "Menu", self.font, GAME_OVER_BUTTON_COLOR, GAME_OVER_BUTTON_HOVER_COLOR)
        exit_button = Button(start_x + 2 * (button_width + spacing), y, button_width, button_height, "Exit", self.font, GAME_OVER_BUTTON_COLOR, GAME_OVER_BUTTON_HOVER_COLOR)

        return {
            "Replay": replay_button,
            "Menu": menu_button,
            "Exit": exit_button,
        }

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for name, button in self.buttons.items():
                # If the button is pressed
                if button.rect.collidepoint(mouse_pos): 
                    # Define the next_state (button_pressed) 
                    self.next_state = name.lower()  
                    break
    
    def update(self):
        # Update button state 
        mouse_pos = pygame.mouse.get_pos()
        for name, button in self.buttons.items():
            print(f"Button: {name}, {button}")
            if button.rect.collidepoint(mouse_pos):
                color = GAME_OVER_BUTTON_HOVER_COLOR
            else:
                color = GAME_OVER_BUTTON_COLOR
            button.draw(self.screen) 
        return self.next_state if hasattr(self, 'next_state') else None
    def draw(self):
        # Draw the screen final game
        self.screen.blit(self.background, (0, 0))

        # Draw the game over text and score  at the center of the screen
        game_over_text = self.font.render("Game Over", True, GAME_OVER_TEXT_COLOR)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - GAME_OVER_FONT_SIZE))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = self.font.render(f"Score: {self.score}", True, GAME_OVER_TEXT_COLOR)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(score_text, score_rect)

        # Draw the buttons after score
        for button in self.buttons.values():
            button.draw(self.screen)