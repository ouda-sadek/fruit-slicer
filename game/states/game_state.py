#################################### The logic of the main game (movement of fruits, score...) ##########################

import pygame
import os
from pygame.locals import *
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import random
import time
from config import *
from game.entities.fruit import Fruit
from game.entities.knife import Knife

class GameState:
    def __init__(self, screen, theme="theme1"):
        self.screen = screen
        self.font = pygame.font.Font(None, SCORE_FONT_SIZE)
        self.theme = theme
        self.background = self.load_background()
        self.fruits = []
        self.knife = Knife(KNIFE_COLOR, KNIFE_WIDTH)
        self.score = 0
        self.last_fruit_spawn_time = time.time()
        self.game_over = False
        self.mouse_down = False
        
        

    def load_background(self):
        """Charge l'image de fond en fonction du thème sélectionné."""
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            if self.theme == "theme1":
              image_path = os.path.join(base_dir, "assets", "images", "background3.png")
            elif self.theme == "theme2":
              image_path = os.path.join(base_dir, "assets", "images", "background4.png")
            elif self.theme == "theme3":
              image_path = os.path.join(base_dir, "assets", "images", "background5.png")
            else:
              image_path = os.path.join(base_dir, "assets", "images", "background6.png")

            background = pygame.image.load(image_path)
            background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
            return background
        except FileNotFoundError:
            print(f"Erreur : Fichier d'image manquant pour le thème {self.theme}. Utilisation du thème par défaut.")
            return pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image : {e}")
            return pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            self.mouse_down = False

    def add_fruit(self):
        size = random.randint(MIN_FRUIT_SIZE, MAX_FRUIT_SIZE)
        speed = random.randint(FRUIT_MIN_SPEED, FRUIT_MAX_SPEED)
        x = random.randint(size, SCREEN_WIDTH - size)
        y = -size
        fruit_type = random.choice(["melon", "pomegranate", "orange", "guava"])
        self.fruits.append(Fruit(x, y, size, speed, fruit_type))

    def update(self):
        if self.game_over:
            return "game_over"
        self.knife.update(pygame.mouse.get_pos(), self.mouse_down)
        if time.time() - self.last_fruit_spawn_time > FRUIT_SPAWN_INTERVAL / 1000:
            self.add_fruit()
            self.last_fruit_spawn_time = time.time()

        # Update fruit
        for fruit in self.fruits:
            fruit.update()
            if fruit.y > SCREEN_HEIGHT + fruit.size:
                self.fruits.remove(fruit)

        # Check for collisions between knife and fruits
        if self.mouse_down:
            for fruit in self.fruits:
                if self.knife.cut_fruit(fruit):
                    self.fruits.remove(fruit)
                    self.score += 1

    def draw(self):
        # Afficher le fond d'écran
        self.screen.blit(self.background, (0, 0))
        
        # Afficher les fruits
        for fruit in self.fruits:
            fruit.draw(self.screen)
        
        # Afficher le couteau
        self.knife.draw(self.screen)
        
        # Afficher le score
        score_text = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, SCORE_POSITION)
    

    
