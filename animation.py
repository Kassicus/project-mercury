import pygame

import lib

class Animation():
    def __init__(self, frames: list, animation_speed: int) -> None:
        self.frames = frames
        self.frame_index = 0
        self.animation_speed = animation_speed

    def animate(self, mirrored = False):
        self.frame_index += self.animation_speed * lib.delta_time

        if self.frame_index > len(self.frames):
            self.frame_index = 0

        if mirrored:
            image = pygame.transform.flip(self.frames[int(self.frame_index)], True, False)
        else:
            image = self.frames[int(self.frame_index)]

        return image