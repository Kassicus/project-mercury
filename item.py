import pygame

import lib

class Item(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, name: str, image: str):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.display_surface = pygame.display.get_surface()

        self.name = name

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.pickup_text = lib.promt_font.render("[E] Pickup " + name, True, lib.color.WHITE, lib.color.BLACK)

    def update(self):
        pass

    def pickup(self):
        if lib.world_reference.hotbar.add_item(self):
            lib.world_reference.ground_items.remove(self)
            lib.world_reference.world_camera.remove(self)
        else:
            pass

    def interact_player(self, player: pygame.sprite.Sprite):
        pickup_offset = 40

        keys = pygame.key.get_pressed()

        if self.pos.x - pickup_offset < player.pos.x < self.pos.x + self.rect.width + pickup_offset:
            if self.pos.y - pickup_offset < player.pos.y < self.pos.y + self.rect.height + pickup_offset:
                self.display_surface.blit(self.pickup_text, ((self.rect.centerx - lib.global_offset.x) - self.pickup_text.get_width() / 2, (self.pos.y - 20) - lib.global_offset.y))
                if keys[pygame.K_e]:
                    self.pickup()