from pico2d import *


class Ground:
    def __init__(self, _x, _y, ):
        self.image = load_image('texture/ground2.png')
        self.w = self.image.w
        self.h = self.image.h
        self.x = _x
        self.y = _y

    def draw(self):
        self.image.clip_draw_to_origin(0, 0, self.w, self.h, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        #self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        #self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x, self.y, self.x + 500, self.y + 50

    def handle_collision(self, group, other):
        if group == 'kirby:ground':
            pass