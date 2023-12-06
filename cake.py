from pico2d import *

import game_framework
import game_world
import server


class Cake:
    def __init__(self, _x, _y):
        self.image = load_image('texture/cake.png')
        self.x = _x
        self.y = _y

    def draw(self):
        self.image.clip_draw(0, 0, 70, 70, self.x, self.y)

        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= 200 * game_framework.frame_time
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def handle_collision(self, group, other):
        if group == 'kirby:cake' or group == 'sonic:cake':
            game_world.remove_object(self)
