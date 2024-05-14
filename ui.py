import pygame

import lib

class Node(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.display_surface = pygame.display.get_surface()

        self.selected = False
        self.hovered = False

        self.image = pygame.Surface([48, 48])
        self.image.fill(lib.color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.render()
        self.interact()

    def render(self):
        pygame.draw.rect(self.display_surface, lib.color.RED, (self.pos.x, self.pos.y, self.rect.width, self.rect.height), 4)

        if self.selected:
            pygame.draw.rect(self.display_surface, lib.color.WHITE, (self.pos.x, self.pos.y, self.rect.width, self.rect.height), 1)

    def interact(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.pos.x < mouse_pos[0] < self.pos.x + self.rect.width:
            if self.pos.y < mouse_pos[1] < self.pos.y + self.rect.height:
                self.image.fill(lib.color.RED)
                self.hovered = True
            else:
                self.image.fill(lib.color.BLACK)
                self.hovered = False
        else:
            self.image.fill(lib.color.BLACK)
            self.hovered = False

        if pygame.mouse.get_pressed()[0]:
            if self.hovered:
                self.selected = True
            else:
                self.selected = False
            