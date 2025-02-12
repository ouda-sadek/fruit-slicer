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
    def __init__(self, x, y, size, speed, object_type):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.letter = random.choice(string.ascii_uppercase)
        self.object_type = object_type
        self.image = None                            
        self.rect = None
        self.is_sliced = False  
        self.load_image(object_type)
        if self.image is None:
            print(f"Error: Could not load image for {object_type}. Object not created.")
            return
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def load_image(self, object_type):
        image_files = [
            f"{object_type}.png",  # Extension PNG
            f"{object_type}.jpg",  # Extension JPG
            f"{object_type}.jpeg", # Extension JPEG
            f"{object_type}.bmp",  # Extension BMP
            f"{object_type}.gif",  # Extension GIF
            f"{object_type}.webp", # Extension WEBP
        ]
        # Check if image exist in the folder specified  :   assets/images
        image_path = None
        for filename in image_files:
            image_path = os.path.join(IMAGE_FOLDER, filename)
            if os.path.exists(image_path):
                break
        else:
            # If not found
            print(f"Error: Image file for {object_type} not found in any expected formats.")
            self.image = None
            return
        
        # If image found , load it
        try:
            print(f"Loading image from: {image_path}")
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (self.size, self.size))
            self.image = image
            print(f"Image loaded for {object_type} with size : {self.image.get_size()}")
        except Exception as e:
            print(f"An error occurred while loading image for object type '{object_type}': {e}")
            self.image = None
        
    def update(self):
        if self.rect:
            self.y -= self.speed
            self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if self.rect:
            screen.blit(self.image, self.rect)
            self.font = pygame.font.Font(None, 36)
            letter_text = self.font.render(self.letter, True, RED)  
            letter_rect = letter_text.get_rect(center=(self.rect.centerx, self.rect.centery - self.size // 2 - 10))  
            screen.blit(letter_text, letter_rect)

#####################################
