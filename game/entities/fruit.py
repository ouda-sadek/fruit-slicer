########################### The Fruit class and the logic for drawing, moving and detecting collisions ###############################

import pygame
from sys import *
from os import *
from config import *

class Fruit:
    def __init__(self, x, y, size, speed, fruit_type):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.fruit_type = fruit_type
        self.image = self.load_image(fruit_type)
        # Vérification du chemin de l'image
        image_path = f"./fruit-slicer/assets/images/{self.fruit_type}.png"
        print(f"Loading image from: {image_path}")
        self.image = pygame.image.load(image_path ).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
        if self.image:
             print(f"Image loaded for {fruit_type} with size : {self.image.get_size()}")
        else:
             print(f"Error: Image for {fruit_type} is None!")
             self.rect = pygame.Rect(0,0,0,0)
             return
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
        
        

    def load_image(self, fruit_type):
        try:
            if fruit_type == "melon":
                image = pygame.image.load(IMAGE_FOLDER + "melon.png").convert_alpha()
            elif fruit_type == "pomegranate":
                image = pygame.image.load(IMAGE_FOLDER + "pomegranate.png").convert_alpha()
            elif fruit_type == "orange":
                image = pygame.image.load(IMAGE_FOLDER + "orange.png").convert_alpha()
            elif fruit_type == "guava":
                image = pygame.image.load(IMAGE_FOLDER + "guava.png").convert_alpha()
            else:
                raise ValueError(f"Invalid fruit type: {fruit_type}")
            image = pygame.transform.scale(image, (self.size, self.size))
            return image
        except FileNotFoundError:
            print(f"Error : File not found at {IMAGE_FOLDER + fruit_type + ".png"}.Please check the image path.")
            return None
        except Exception as e:
            print(f"An error occurred while loading image for fruit type '{fruit_type}': {e}")
            return None
        
    def update(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_sliced(self, knife):
        if knife.is_cutting:
            return self.rect.colliderect(knife.rect)
        else:
            return False

    

