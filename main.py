import pygame

pygame.init()

import lib
import debug
import world

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()
        self.world = world.World("assets/ship.png")

    def run(self):
        while self.running:
            self.single_events()
            self.multi_events()
            self.draw()
            self.update()

    def single_events(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()
                if event.key == pygame.K_u:
                    self.debug_interface.toggle_framerate()

    def multi_events(self):
        pass

    def draw(self):
        self.screen.fill(lib.color.BLACK)

        self.world.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self):
        self.world.update()

        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()