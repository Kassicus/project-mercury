import lib

class Animation():
    def __init__(self, frames: list) -> None:
        self.frames = frames
        self.frame_index = 0
        self.animate_speed = 2

    def animate(self):
        self.frame_index += self.animate_speed * lib.delta_time

        if self.frame_index > len(self.frames):
            self.frame_index = 0

        image = self.frames[int(self.frame_index)]

        return image