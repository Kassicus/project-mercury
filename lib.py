import pygame
from random import randint

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1050
SCREEN_TITLE = "Project Mercury"

class Colors:
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.RED = pygame.Color(255, 0, 0, 255)

    def random(self) -> pygame.Color:
        color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255), 255)

        return color
    
    def random_gray(self) -> pygame.Color:
        scale = randint(0, 255)

        color = pygame.Color(scale, scale, scale, 255)

        return color
    
    def random_custom(self, channels: str) -> pygame.Color:
        red_channel = 0
        green_channel = 0
        blue_channel = 0
        
        if 'r' in channels:
            red_channel = randint(0, 255)
        if 'g' in channels:
            green_channel = randint(0, 255)
        if 'b' in channels:
            blue_channel = randint(0, 255)

        color = pygame.Color(red_channel, green_channel, blue_channel, 255)

        return color
        

color = Colors()

global_offset = pygame.math.Vector2()
world_reference = None

delta_time = 0
events = None
framerate = 120