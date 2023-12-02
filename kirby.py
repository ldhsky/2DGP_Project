from pico2d import *
from utils import make_color_transparent

import server




class Kirby:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.action = 0
        self.image = load_image('texture/kirby_idle.png')
        # self.state_machine = StateMachine(self)
        # self.state_machine.start()

    def update(self):
        # self.state_machine.update()
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, 100, 100)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        pass
