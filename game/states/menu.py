####################################### Class for the game menu   ##############################################################
import pygame
from pygame.locals import *
from config import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, MENU_FONT_SIZE)
        self.buttons = self.create_menu_buttons()
        #self.background = pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__), 
       
    def create_menu_buttons(self):
        button_width = MENU_BUTTON_WIDTH
        button_height = MENU_BUTTON_HEIGHT
        play_x = SCREEN_WIDTH // 2 - button_width // 2
        play_y = SCREEN_HEIGHT // 2 - button_height // 2 - button_height
        exit_x = play_x
        exit_y = SCREEN_HEIGHT // 2 + button_height // 2

        play_text, play_rect, play_button = self.create_button("Play", self.font, play_x + button_width // 2, play_y + button_height // 2)       
        exit_text, exit_rect, exit_button = self.create_button("Exit", self.font, exit_x + button_width // 2, exit_y + button_height // 2)

        buttons = {
            "Play": (play_text, play_rect, play_button),
            "Exit": (exit_text, exit_rect, exit_button),
        }
        return buttons
    
    def create_button(self, text, font, x, y):
        text_surface = font.render(text, True, MENU_BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        button_rect = text_rect.inflate(MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
        return text_surface, text_rect, button_rect
    
    def draw_button(self, text_surface, text_rect, button_rect, color):
        pygame.draw.rect(self.screen, color, button_rect)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for name, (_,_, button_rect) in self.buttons.items():
                if button_rect.collidepoint(mouse_pos):
                    self.next_state = name.lower()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for name, (text, rect, button_rect) in self.buttons.items():
            if button_rect.collidepoint(mouse_pos):
                color = MENU_BUTTON_HOVER_COLOR
            else:
                color = MENU_BUTTON_COLOR
            self.draw_button(text, rect, button_rect, color)
        return self.next_state   if hasattr(self, 'next_state') else None
    
    def draw(self):
       pass