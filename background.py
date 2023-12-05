from pico2d import *

class Background:

    def __init__(self):
        self.image = load_image('texture/background5.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        # fill here


    def draw(self):
        self.image.clip_draw_to_origin(0, 0, self.cw, self.ch, 0, 0)
        # self.image.clip_composite_draw(0, 0, self.cw, self.ch, 0, 'h', self.cw/2, self.ch/2, 100, 100)

    def update(self):
        #self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        #self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def handle_event(self, event):
        pass
