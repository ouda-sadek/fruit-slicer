########################### The Fruit class and the logic for drawing, moving and detecting collisions ###############################

import pygame
import sys
import os
import random
import string
from os import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from config import *

class Fruit:
    def __init__(self, x, y, size, speed, fruit_type):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.letter = random.choice(string.ascii_uppercase)
        self.fruit_type = fruit_type
        self.image = None                            
        self.rect = None
        self.is_sliced = False  
        self.load_image(fruit_type)
        if self.image is None:
            print(f"Error: Could not load image for {fruit_type}. Object not created.")
            return
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def load_image(self, fruit_type):
        fruit_image_files = [
            f"{fruit_type}.png",  # Extension PNG
            f"{fruit_type}.jpg",  # Extension JPG
            f"{fruit_type}.jpeg", # Extension JPEG
            f"{fruit_type}.bmp",  # Extension BMP
            f"{fruit_type}.gif",  # Extension GIF
            f"{fruit_type}.webp", # Extension WEBP
        ]
        # Check if image exists in assets folder
        image_path = None
        for filename in fruit_image_files:
            image_path = os.path.join(IMAGE_FOLDER, filename)
            if os.path.exists(image_path):
                break
        else:
            # If no images were found
            print(f"Error: Image file for {fruit_type} not found in any expected formats.")
            self.image = None
            return
        
        # If the image is found, load it
        try:
            print(f"Loading image from: {image_path}")
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (self.size, self.size))
            self.image = image
            print(f"Image loaded for {fruit_type} with size : {self.image.get_size()}")
        except Exception as e:
            print(f"An error occurred while loading image for fruit type '{fruit_type}': {e}")
            self.image = None
        
    def update(self):
        if self.rect:
            self.y -= self.speed
            self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if self.rect:
            screen.blit(self.image, self.rect)
            self.font = pygame.font.Font(None, 36)
            letter_text = self.font.render(self.letter, True, WHITE)  
            letter_rect = letter_text.get_rect(center=(self.rect.centerx, self.rect.centery - self.size // 2 - 10))  
            screen.blit(letter_text, letter_rect)

            #pygame.display.update()
        
    def is_sliced(self, knife):
        if knife.is_cutting:
            return self.rect.colliderect(knife.rect)
        else:
            return False    
        
