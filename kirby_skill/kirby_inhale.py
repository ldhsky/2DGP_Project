from pico2d import *

import server


class KirbyInhale:
    def __init__(self, _x, _y, ):
        self.image = load_image('texture/ground.png')
        self.w = self.image.w
        self.h = self.image.h
        self.x = _x
        self.y = _y

    def draw(self):
        # self.image.clip_draw_to_origin(0, 0, self.w, self.h, self.x, self.y)
        # draw_rectangle(*self.get_bb())
        pass

    def update(self):
        #self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        #self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)
        self.x = server.player1.x + 75 * server.player1.dir
        self.y = server.player1.y
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 25

    def handle_collision(self, group, other):
        if group == 'kirby_inhale:sonic':
            pass
