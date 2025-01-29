############################# The Knife class for knife movement logic, collision detection #######################

import pygame
from config import KNIFE_COLOR, KNIFE_WIDTH
from game.utils import point_in_circle, distance


class Knife:
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.pos = (0, 0) 
        self.is_cutting = False 
        self.rect = pygame.Rect(0, 0, 1,1) 
        self.rect.center = self.pos
        self.radius = 20 
        self.last_pos = None 

    def update(self, mouse_pos, mouse_down):
        self.pos = mouse_pos
        self.is_cutting = mouse_down
        self.rect.center = self.pos
        if self.last_pos:
            self.direction = (self.pos[0] - self.last_pos[0] , self.pos[1] - self.last_pos[1]) 
        self.last_pos = self.pos 

    def draw(self, screen):
       if self.last_pos and self.is_cutting :
        pygame.draw.line(screen, self.color, self.last_pos,self.pos, self.width)
    
    def cut_fruit(self,fruit):
       if self.is_cutting:
           # check if the knife is inside the fruit circle
           return point_in_circle(self.pos,(fruit.x, fruit.y), fruit.size/2) or (self.last_pos and point_in_circle(self.last_pos,(fruit.x, fruit.y), fruit.size/2))
       return False