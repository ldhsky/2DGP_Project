from pico2d import *

import server


class KirbyFire:
    def __init__(self, _x, _y):
        self.image = load_image('texture/kirby_fire.png')
        self.x = _x
        self.y = _y

    def draw(self):
        if server.player1.dir == 1:
            self.image.clip_draw(int(server.player1.frame) * 100, 0, 100, 100, self.x, self.y)
        elif server.player1.dir == -1:
            self.image.clip_composite_draw(int(server.player1.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.x = server.player1.x
        self.y = server.player1.y
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 45, self.y - 50, self.x + 45, self.y + 40

    def handle_collision(self, group, other):
        pass
