import pygame

import lib

class DebugInterface:
    def __init__(self):
        self.active = False
        self.font = pygame.font.SysFont("Courier", 16)
        self.offset = 10
        self.display_surface = pygame.display.get_surface()

        self.t_fps = None
        self.t_mouse = None

        self.o_fps = None
        self.o_mouse = None

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, lib.color.WHITE)
        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset)

        return text, offset

    def get_mouse(self) -> list [pygame.Surface, int]:
        x, y = pygame.mouse.get_pos()

        string = "Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.WHITE)
        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset)

        return text, offset
    
    def toggle_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self):
        self.display_surface.blit(self.t_fps, (self.o_fps, 10))
        self.display_surface.blit(self.t_mouse, (self.o_mouse, 30))

    def update(self, clock: pygame.time.Clock):
        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()