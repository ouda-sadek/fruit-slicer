#################################### The logic of the main game (movement of fruits, score...) ##########################

import pygame
from pygame.locals import *
import random
import time
from config import *
from game.entities.fruit import Fruit
from game.entities.knife import Knife

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, SCORE_FONT_SIZE)
        self.fruits = []
        self.knife = Knife(KNIFE_COLOR, KNIFE_WIDTH)
        self.score = 0
        self.last_fruit_spawn_time = time.time()
        self.game_over = False
        self.mouse_down = False

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
        fruit_type = random.choice(["apple", "banana", "orange", "kiwi", "watermelon","pasteque"])
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
                #self.score += 1

        # Check if fruit collides with knife
        for fruit in self.fruits:
            if self.knife.cut_fruit(fruit):
                self.fruits.remove(fruit)
                #self.score += 1

         # Check for collisions between knife and fruits
        if self.mouse_down:
            for fruit in self.fruits:
                if self.knife.cut_fruit(fruit):
                    self.fruits.remove(fruit)
                    self.score +=1
        #return None
       
    def draw(self):
        self.screen.fill(BLACK)
        for fruit in self.fruits:
           fruit.draw(self.screen)
        self.knife.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, SCORE_POSITION)  
    
    #pygame.display.flip()
    

    
