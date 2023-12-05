from pico2d import *


class Deadline:
    def __init__(self, _x, _y, ):
        self.x = _x
        self.y = _y

    def draw(self):
        draw_rectangle(*self.get_bb())

    def update(self):
        #self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        #self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 1000, self.y - 900, self.x + 1000, self.y + 900

    def handle_collision(self, group, other):
        pass

