import pygame

import lib
import animation

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), int(lib.SCREEN_HEIGHT / 2))
        self.velo = pygame.math.Vector2()
        self.speed = 250

        self.display_surface = pygame.display.get_surface()

        self.image = pygame.Surface([40, 60])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.idle_animation = animation.Animation([
            pygame.image.load("assets/animations/player/idle/idle_1.png").convert_alpha(),
            pygame.image.load("assets/animations/player/idle/idle_2.png").convert_alpha()
        ])
        
        self.walking_animation = animation.Animation([
            pygame.image.load("assets/animations/player/walking/walking_1.png").convert_alpha(),
            pygame.image.load("assets/animations/player/walking/walking_2.png").convert_alpha(),
            pygame.image.load("assets/animations/player/walking/walking_3.png").convert_alpha(),
            pygame.image.load("assets/animations/player/walking/walking_4.png").convert_alpha()
        ], animation_speed=8)

    def update(self) -> None:
        self.pos += self.velo * lib.delta_time
        self.rect.center = self.pos

        self.move()

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velo.x = -self.speed
            self.image = self.walking_animation.animate(mirrored=True)
        elif keys[pygame.K_d]:
            self.velo.x = self.speed
            self.image = self.walking_animation.animate()
        else:
            self.velo.x = 0
            self.image = self.idle_animation.animate()

        if keys[pygame.K_w]:
            self.velo.y = -self.speed
        elif keys[pygame.K_s]:
            self.velo.y = self.speed
        else:
            self.velo.y = 0