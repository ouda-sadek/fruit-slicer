#################################### The logic of the main game (movement of fruits, score...) ##########################

import pygame
from pygame.locals import *
import random
import time
from config import *
from game.entities.fruit import Fruit

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, SCORE_FONT_SIZE)
        self.objects = []
        self.score = 0
        self.last_object_spawn_time = time.time()
        self.game_over = False
        self.remaining_lives = 3
        self.strikes = 0
        self.last_slice_time = 0
        self.combo_count = 0
        self.paused = False
        self.pause_duration = 0

    def handle_events(self, event):
      if event.type == pygame.KEYDOWN:
        if self.paused:
          return
        for obj in list(self.objects):
          if event.unicode.upper() == obj.letter:
            self.slice_object(obj)

    def add_object(self):
        size = random.randint(MIN_FRUIT_SIZE, MAX_FRUIT_SIZE)
        speed = random.randint(FRUIT_MIN_SPEED, FRUIT_MAX_SPEED)
        x = random.randint(size, SCREEN_WIDTH - size)
        y = SCREEN_HEIGHT + size
        object_type = random.choices(["apple", "banana", "orange", "kiwi", "watermelon", "pasteque", "bomb", "ice"], weights=[5, 5, 5, 5, 5, 5, 1, 1])[0]
        self.objects.append(Fruit(x, y, size, speed, object_type))
    
    def slice_object(self, obj):
       if obj.object_type == "bomb":
         self.game_over = True
         return
       elif obj.object_type == "ice":
          self.paused = True
          self.pause_duration = time.time() + random.randint(ICE_MIN_DURATION,ICE_MAX_DURATION)
          self.objects.remove(obj)
          return

       self.objects.remove(obj)
       self.score += 1
       current_time = time.time()
       if current_time - self.last_slice_time < COMBO_TIME_WINDOW :
            self.combo_count += 1
            self.score += self.combo_count
       else:
           self.combo_count = 0
           self.score += 1
       self.last_slice_time = current_time
    
    def update(self):
        if self.game_over:
            return "game_over"
        if self.paused:
             if time.time() >= self.pause_duration:
               self.paused = False
             return

        if time.time() - self.last_object_spawn_time > OBJECT_SPAWN_INTERVAL / 1000:
            self.add_object()
            self.last_object_spawn_time = time.time()

        # Update fruit
        for obj in list(self.objects):
            obj.update()
            if obj.y < -obj.size:
                self.objects.remove(obj)
                self.strikes += 1
                if self.strikes >= MAX_STRIKES:
                  self.game_over = True
        return None
       
    def draw(self):
        self.screen.fill(BLACK)
        for obj in self.objects:
           obj.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, SCORE_POSITION)
        strikes_text = self.font.render(f"Strikes: {self.strikes}", True, SCORE_COLOR)
        self.screen.blit(strikes_text, (10, 50))

    def get_score(self):
        return self.score
       
