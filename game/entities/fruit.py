########################### The Fruit class and the logic for drawing, moving and detecting collisions ###############################
import pygame
import sys
import os
from os import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from config import *

class Fruit:
    def __init__(self, x, y, size, speed, fruit_type):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
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
        fruit_images = {
            "apple": "apple.png",
            "banana": "banana.png",
            "orange": "orange.png",
            "kiwi": "kiwi.png",
        }
        try:
            if fruit_type in fruit_images:
                image_path = IMAGE_FOLDER + fruit_images[fruit_type]
                if not os.path.exists(image_path):
                    print(f"Error: Image file not found: {image_path}")
                    return None
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (self.size, self.size))
                self.image = image
                print(f"Image loaded for {fruit_type} with size : {self.image.get_size()}")
                #return image
            else:
                raise ValueError(f"Invalid fruit type: {fruit_type}")
        except Exception as e:
            print(f"An error occurred while loading image for fruit type '{fruit_type}': {e}")
            self.image = None
        
    def update(self):
        if self.rect:
            self.y += self.speed
            self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if self.rect:
            screen.blit(self.image, self.rect)
        
    def is_sliced(self, knife):
        if knife.is_cutting:
            return self.rect.colliderect(knife.rect)
        else:
            return False