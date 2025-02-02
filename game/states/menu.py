####################################### Class for the game menu   ##############################################################

import pygame
import os
from pygame.locals import *
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from config import * 


class SubMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, MENU_FONT_SIZE)
        self.buttons = self.create_submenu_buttons()
        self.background = pygame.image.load(os.path.join(os.path.dirname(__file__), "../../assets/images/background1.png"))
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.theme_selected = None  # To store the chosen theme
        self.theme_options = ["theme1", "theme2", "theme3"]  # List of available themes
        self.theme_buttons = self.create_theme_buttons()  # Buttons to choose a theme
        self.show_theme_options = False  # To show or hide theme options
        self.next_state = None  # Initialize next_state to None
        

    def create_submenu_buttons(self):
        button_width = MENU_BUTTON_WIDTH
        button_height = MENU_BUTTON_HEIGHT
        theme_x = 420
        theme_y = 60
        language_x = 110
        language_y = 190
        sounds_x = theme_x + 300
        sounds_y = 180

        theme_text, theme_rect, theme_button = self.create_button("Theme", self.font, theme_x + button_width // 2, theme_y + button_height // 2)
        language_text, language_rect, language_button = self.create_button("Language", self.font, language_x + button_width // 2, language_y + button_height // 2)
        sounds_text, sounds_rect, sounds_button = self.create_button("Sounds", self.font, sounds_x + button_width // 2, sounds_y + button_height // 2)

        buttons = {
            "Theme": (theme_text, theme_rect, theme_button),
            "Language": (language_text, language_rect, language_button),
            "Sounds": (sounds_text, sounds_rect, sounds_button),
        }
        return buttons

    def create_theme_buttons(self):
        button_width = MENU_BUTTON_WIDTH
        button_height = MENU_BUTTON_HEIGHT
        theme1_x = 420
        theme1_y = 60
        theme2_x = 110
        theme2_y = 190
        theme3_x = theme1_x + 300
        theme3_y = 180

        theme1_text, theme1_rect, theme1_button = self.create_button("Theme1", self.font, theme1_x + button_width // 2, theme1_y + button_height // 2)
        theme2_text, theme2_rect, theme2_button = self.create_button("Theme2", self.font, theme2_x + button_width // 2, theme2_y + button_height // 2)
        theme3_text, theme3_rect, theme3_button = self.create_button("Theme3", self.font, theme3_x + button_width // 2, theme3_y + button_height // 2)

        buttons = {
            "theme1": (theme1_text, theme1_rect, theme1_button),
            "theme2": (theme2_text, theme2_rect, theme2_button),
            "theme3": (theme3_text, theme3_rect, theme3_button),
        }
        return buttons

    def create_button(self, text, font, x, y):
        text_surface = font.render(text, True, MENU_BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        button_rect = text_rect.inflate(MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
        return text_surface, text_rect, button_rect

    def draw_button(self, text_surface, text_rect, button_rect, color):
        pygame.draw.rect(self.screen, color, button_rect, border_radius=100)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.show_theme_options:
                # Handling clicks on theme buttons
                for theme_name, (_, _, button_rect) in self.theme_buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        self.theme_selected = theme_name
                        print(f"Thème sélectionné dans SubMenu : {self.theme_selected}")
                        self.show_theme_options = False  # Hide theme options after selection
                        self.next_state = "menu"  # Indicate that we should return to the main menu
            else:
                # Managing clicks on submenu buttons
                for name, (_, _, button_rect) in self.buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        if name == "Theme":
                            self.show_theme_options = True  # Show theme options
                        elif name == "Language":
                            print("Language clicked")
                        elif name == "Sounds":
                            print("Sounds clicked")
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.show_theme_options:
            # Update theme buttons
            for theme_name, (text, rect, button_rect) in self.theme_buttons.items():
                if button_rect.collidepoint(mouse_pos):
                    color = MENU_BUTTON_HOVER_COLOR
                else:
                    color = MENU_BUTTON_COLOR
                self.draw_button(text, rect, button_rect, color)
        else:
            # Update submenu buttons
            for name, (text, rect, button_rect) in self.buttons.items():
                if button_rect.collidepoint(mouse_pos):
                    color = MENU_BUTTON_HOVER_COLOR
                else:
                    color = MENU_BUTTON_COLOR
                self.draw_button(text, rect, button_rect, color)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.show_theme_options:
            # Draw the theme buttons
            for text_surface, text_rect, button_rect in self.theme_buttons.values():
                self.draw_button(text_surface, text_rect, button_rect, MENU_BUTTON_COLOR)
        else:
            # Draw the submenu buttons
            for text_surface, text_rect, button_rect in self.buttons.values():
                self.draw_button(text_surface, text_rect, button_rect, MENU_BUTTON_COLOR)



class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, MENU_FONT_SIZE)
        self.buttons = self.create_menu_buttons()
        self.background = pygame.image.load(os.path.join(os.path.dirname(__file__), "../../assets/images/background1.png"))
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.submenu = None
        self.next_state = None

    def create_menu_buttons(self):
        button_width = MENU_BUTTON_WIDTH
        button_height = MENU_BUTTON_HEIGHT
        play_x = 420
        play_y = 60
        setting_x = 110
        setting_y = 190
        exit_x = play_x + 300
        exit_y = setting_y

        play_text, play_rect, play_button = self.create_button("Play", self.font, play_x + button_width // 2, play_y + button_height // 2)
        setting_text, setting_rect, setting_button = self.create_button("Setting", self.font, setting_x + button_width // 2, setting_y + button_height // 2)
        exit_text, exit_rect, exit_button = self.create_button("Exit", self.font, exit_x + button_width // 2, exit_y + button_height // 2)

        buttons = {
            "Play": (play_text, play_rect, play_button),
            "Setting": (setting_text, setting_rect, setting_button),
            "Exit": (exit_text, exit_rect, exit_button),
        }
        return buttons

    def create_button(self, text, font, x, y):
        text_surface = font.render(text, True, MENU_BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        button_rect = text_rect.inflate(MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
        return text_surface, text_rect, button_rect

    def draw_button(self, text_surface, text_rect, button_rect, color):
        pygame.draw.rect(self.screen, color, button_rect, border_radius=100)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self, event):
        if self.submenu:
            self.submenu.handle_events(event)  
        else:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, (_, _, button_rect) in self.buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        if name == "Setting":
                            self.submenu = SubMenu(self.screen)  
                        elif name == "Exit":
                            self.next_state = "exit"
                        elif name == "Play":
                        # Récupérer le thème sélectionné dans le sous-menu
                         if hasattr(self, 'submenu') and hasattr(self.submenu, 'theme_selected'):
                            theme = self.submenu.theme_selected or "theme1"  # Thème par défaut si aucun n'est sélectionné
                         else:
                            theme = "theme1"  # Thème par défaut
                         print(f"Thème sélectionné : {theme}")  # Vérification
                         self.next_state = "play"
                         # Stocker le thème pour le transmettre à GameState
                         self.selected_theme = theme

                        else:
                            self.next_state = name.lower()

    def update(self):
        if self.submenu:
            self.submenu.update()
            # Si le sous-menu a terminé son travail (par exemple, un bouton "Retour" est cliqué)
            if self.submenu.next_state == "menu":
                self.submenu = None  # Revenir au menu principal
        else:
            mouse_pos = pygame.mouse.get_pos()
            for name, (text, rect, button_rect) in self.buttons.items():
                if button_rect.collidepoint(mouse_pos):
                    color = MENU_BUTTON_HOVER_COLOR
                else:
                    color = MENU_BUTTON_COLOR
                self.draw_button(text, rect, button_rect, color)
        return self.next_state if hasattr(self, 'next_state') else None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.submenu:
            self.submenu.draw()
        else:
            for text_surface, text_rect, button_rect in self.buttons.values():
                self.draw_button(text_surface, text_rect, button_rect, MENU_BUTTON_COLOR)


