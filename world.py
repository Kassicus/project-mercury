import pygame

import lib
import camera
import player
import wall
import ui
import item

class World():
    def __init__(self, background_path: str) -> None:
        lib.world_reference = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()

        self.world_camera = camera.PlayerCenterCamera(self.display_surface, self.world_background)
        self.walls = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()
        self.ui_elements = pygame.sprite.Group()
        self.ground_items = pygame.sprite.Group()

        self.hotbar = ui.HotBar()

        self.ui_elements.add(self.hotbar)

        self.test_item = item.Tool(300, 300, "wrench", "assets/items/wrench.png", 100, 100)
        self.other_item = item.Tool(400, 600, "hammer", "assets/items/hammer.png", 80, 200)

        self.wall_points = [
            [0, 0, 15, 1], [0, 1, 1, 21], [15, 1, 1, 8], [15, 11, 1, 3], [15, 16, 1, 6], [1, 21, 14, 1], [16, 7, 11, 1], [16, 12, 11, 1], [16, 17, 16, 1], [20, 13, 1, 4],
            [27, 0, 1, 9], [28, 0, 4, 1], [32, 0, 1, 18], [27, 11, 1, 3], [27, 16, 1, 1]
        ]

        self.create_walls(self.wall_points)
        self.player = player.Player()
        self.world_camera.add(self.player)
        self.world_camera.add(self.test_item, self.other_item)

        self.ground_items.add(self.test_item, self.other_item)

    def create_walls(self, wall_array: list):
        for point_array in range(len(wall_array)):
            w = wall.Wall(wall_array[point_array][0], wall_array[point_array][1], wall_array[point_array][2], wall_array[point_array][3])
            self.walls.add(w)
            self.collidables.add(w)

    def check_collisions(self):
        collision_tollerance = 15

        for c in self.collidables:
            if self.player.rect.colliderect(c.rect):
                if abs(self.player.rect.left - c.rect.right) < collision_tollerance:
                    self.player.velo.x = 0
                    self.player.pos.x = c.rect.right + self.player.rect.width / 2
                if abs(self.player.rect.right - c.rect.left) < collision_tollerance:
                    self.player.velo.x = 0
                    self.player.pos.x = c.rect.left - self.player.rect.width / 2

                if abs(self.player.rect.top - c.rect.bottom) < collision_tollerance:
                    self.player.velo.y = 0
                    self.player.pos.y = c.rect.bottom + self.player.rect.height / 2
                if abs(self.player.rect.bottom - c.rect.top) < collision_tollerance:
                    self.player.velo.y = 0
                    self.player.pos.y = c.rect.top - self.player.rect.height / 2

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)
        self.ui_elements.draw(self.display_surface)

    def update(self) -> None:
        self.world_camera.update()
        self.check_collisions()
        self.ui_elements.update()

        for item in self.ground_items:
            item.interact_player(self.player)