import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), int(lib.SCREEN_HEIGHT / 2))
        self.velo = pygame.math.Vector2()
        self.speed = 250

        self.image = pygame.Surface([40, 60])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.velo * lib.delta_time
        self.rect.center = self.pos

        self.move()

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velo.x = -self.speed
        elif keys[pygame.K_d]:
            self.velo.x = self.speed
        else:
            self.velo.x = 0

        if keys[pygame.K_w]:
            self.velo.y = -self.speed
        elif keys[pygame.K_s]:
            self.velo.y = self.speed
        else:
            self.velo.y = 0