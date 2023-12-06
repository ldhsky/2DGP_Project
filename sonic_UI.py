from pico2d import *

import server


class SonicUI:
    def __init__(self, _x, _y):
        self.image = load_image('texture/sonic_UI.png')
        self.x = _x
        self.y = _y
        self.font = load_font('ENCR10B.TTF', 50)
        self.font2 = load_font('ENCR10B.TTF', 50)

    def draw(self):
        self.image.clip_draw(0, 0, 200, 350, self.x, self.y, 200, 300)
        self.font.draw(self.x + 100, self.y + 50, 'Damage : 'f'{int(server.player2.damage):d}', (0, 0, 255))
        self.font2.draw(self.x + 100, self.y+ 10, 'Life : 'f'{int(server.player2.life):d}', (0, 0, 255))


    def update(self):
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 45, self.y - 50, self.x + 45, self.y + 40

    def handle_collision(self, group, other):
        pass
