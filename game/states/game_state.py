#################################### The logic of the main game (movement of fruits, score...) ##########################
"""import pygame
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
        self.pause_button_rect = pygame.Rect(PAUSE_BUTTON_POSITION, (PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT))
        self.pause_text = self.font.render("Pause", True, PAUSE_BUTTON_TEXT_COLOR)
        self.pause_text_rect = self.pause_text.get_rect(center=self.pause_button_rect.center)

    def handle_events(self, event):
      if event.type == pygame.KEYDOWN:
        if self.paused:
          return
        for obj in list(self.objects):
          if event.unicode.upper() == obj.letter:
            self.slice_object(obj)
      if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_pos = pygame.mouse.get_pos()
           if self.pause_button_rect.collidepoint(mouse_pos):
              self.paused = not self.paused

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
            if time.time() >= self.pause_duration and self.pause_duration != 0:
                self.paused = False
                self.pause_duration = 0
            return
            
        if not self.paused:
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
        
        # Draw pause button
        mouse_pos = pygame.mouse.get_pos()
        if self.pause_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, PAUSE_BUTTON_HOVER_COLOR, self.pause_button_rect)
        else:
            pygame.draw.rect(self.screen, PAUSE_BUTTON_COLOR, self.pause_button_rect)
        self.screen.blit(self.pause_text, self.pause_text_rect)

    def get_score(self):
        return self.score"""
       
##########################################################
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
        
        # Charger l'image pour le bouton pause
        self.pause_image = pygame.image.load(IMAGE_FOLDER + "pause.png").convert_alpha()  # Remplace par le chemin de ton image
        self.pause_image = pygame.transform.scale(self.pause_image, (PAUSE_IMAGE_WIDTH, PAUSE_IMAGE_HEIGHT))  # Redimensionner l'image
        
        # Créer un rect pour positionner l'image
        self.pause_image_rect = self.pause_image.get_rect(topleft=PAUSE_IMAGE_POSITION)
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if self.paused:
                return
            for obj in list(self.objects):
                if event.unicode.upper() == obj.letter:
                    self.slice_object(obj)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Vérifie si la souris clique sur l'image du bouton pause
            if self.pause_image_rect.collidepoint(mouse_pos):
                self.paused = not self.paused  # Changer l'état de la pause

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
            self.pause_duration = time.time() + random.randint(ICE_MIN_DURATION, ICE_MAX_DURATION)
            self.objects.remove(obj)
            return

        self.objects.remove(obj)
        self.score += 1
        current_time = time.time()
        if current_time - self.last_slice_time < COMBO_TIME_WINDOW:
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
            if time.time() >= self.pause_duration and self.pause_duration != 0:
                self.paused = False
                self.pause_duration = 0
            return
            
        if not self.paused:
            if time.time() - self.last_object_spawn_time > OBJECT_SPAWN_INTERVAL / 1000:
                self.add_object()
                self.last_object_spawn_time = time.time()

            # Update fruit
            for obj in self.objects[:]:
                obj.update()
                if obj.y < -obj.size:
                #if obj.y >= SCREEN_HEIGHT + obj.size: 
                    self.objects.remove(obj)
                    self.strikes += 1
                    if self.strikes >= MAX_STRIKES:
                        self.game_over = True
        return None
       
    def draw(self):
        self.screen.fill(BLACK)
        for obj in self.objects:
            obj.draw(self.screen)
        
        
        # Dessiner le score et les vies restantes
        score_text = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, SCORE_POSITION)
        strikes_text = self.font.render(f"Strikes: {self.strikes}", True, SCORE_COLOR)
        self.screen.blit(strikes_text, (10, 50))
        
        # Dessiner l'image du bouton pause
        mouse_pos = pygame.mouse.get_pos()
        if self.pause_image_rect.collidepoint(mouse_pos):
            # Optionnel : si tu veux changer l'apparence de l'image lorsqu'on survole
            pygame.draw.rect(self.screen, PAUSE_IMAGE_HOVER_COLOR, self.pause_image_rect, 5)  # Dessiner un contour survolé
        self.screen.blit(self.pause_image, self.pause_image_rect)  # Afficher l'image

    def get_score(self):
        return self.score
