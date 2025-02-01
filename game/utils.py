##################################### File for utility functions (collision detection, generation of random objects...) ###########

import pygame
from pygame.locals import *

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def point_in_circle(point, circle_center, circle_radius):
    x, y = point
    circle_x, circle_y = circle_center
    return distance(point, (circle_x, circle_y)) <= circle_radius
