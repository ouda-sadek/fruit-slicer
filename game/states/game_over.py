##################################### Class for the end of game screen.    ####################################################

import pygame
from config import *

class GameOver:
    def __init__(self, screen, score=0):
        self.screen = screen
        self.font = pygame.font.Font(None, GAME_OVER_FONT_SIZE)
        self.score = score
        self.buttons = self.create_buttons()

    def create_buttons(self):
        button_width = GAME_OVER_BUTTON_WIDTH
        button_height = GAME_OVER_BUTTON_HEIGHT
        restart_x = SCREEN_WIDTH // 2 - button_width // 2
        restart_y = SCREEN_HEIGHT // 2 + button_height
        menu_x = SCREEN_WIDTH // 2 - button_width // 2
        menu_y = SCREEN_HEIGHT // 2 + 2*button_height

        restart_text, restart_rect, restart_button = self.create_button("Restart", self.font, restart_x + button_width // 2, restart_y + button_height // 2)
        menu_text, menu_rect, menu_button = self.create_button("Menu", self.font, menu_x + button_width // 2, menu_y + button_height // 2)
        buttons = {
            "Restart": (restart_text, restart_rect, restart_button),
            "Menu": (menu_text, menu_rect, menu_button),
        }
        return buttons
    
    def create_button(self, text, font, x, y):
        text_surface = font.render(text, True, GAME_OVER_BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        button_rect = text_rect.inflate(GAME_OVER_BUTTON_WIDTH, GAME_OVER_BUTTON_HEIGHT)
        return text_surface, text_rect, button_rect
    
    def draw_button(self, text_surface, text_rect, button_rect, color):
        pygame.draw.rect(self.screen, color, button_rect)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        for name, (_, _, button_rect) in self.buttons.items():
         if button_rect.collidepoint(mouse_pos):
           self.next_state = name.lower()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for name, (text, rect, button_rect) in self.buttons.items():
            if button_rect.collidepoint(mouse_pos):
                color = GAME_OVER_BUTTON_HOVER_COLOR
            else:
                color = GAME_OVER_BUTTON_COLOR
            self.draw_button(text, rect, button_rect, color)
        return self.next_state if hasattr(self, 'next_state') else None
    
    def draw(self):
        game_over_text = self.font.render("Game Over", True, GAME_OVER_TEXT_COLOR)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - GAME_OVER_FONT_SIZE))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = self.font.render(f"Score: {self.score}", True, GAME_OVER_TEXT_COLOR)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(score_text, score_rect)




    