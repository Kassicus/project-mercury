import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        pygame.sprite.Sprite.__init__(self)

        self.scale = 60

        self.pos = pygame.math.Vector2(x * self.scale, y * self.scale)
        self.image = pygame.Surface([width * self.scale, height * self.scale])
        self.image.fill(lib.color.WHITE)
        self.image.set_colorkey(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos