from pico2d import *

import server


class KirbyFire:
    def __init__(self, _x, _y):
        self.image = load_image('texture/ground.png')
        self.x = _x
        self.y = _y

    def draw(self):
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = server.player1.x
        self.y = server.player1.y
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 70, self.y - 70, self.x + 70, self.y + 45

    def handle_collision(self, group, other):
        if group == 'kirby_inhale:sonic':
            pass
