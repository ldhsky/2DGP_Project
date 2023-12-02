from pico2d import *

import game_framework
import server

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Idle:
    @staticmethod
    def enter(kirby, e):
        # if boy.action == 0:
        #     boy.action = 2
        # elif boy.action == 1:
        #     boy.action = 3
        kirby.speed = 0
        kirby.dir = 0

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        pass


class StateMachine:
    def __init__(self, kirby):
        self.kirby = kirby
        self.cur_state = Idle
        # self.transitions = {
        #     Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, upkey_down: RunUp,
        #            downkey_down: RunDown, upkey_up: RunDown, downkey_up: RunUp},
        #     RunRight: {right_up: Idle, left_down: Idle, upkey_down: RunRightUp, upkey_up: RunRightDown,
        #                downkey_down: RunRightDown, downkey_up: RunRightUp},
        #     RunRightUp: {upkey_up: RunRight, right_up: RunUp, left_down: RunUp, downkey_down: RunRight},
        #     RunUp: {upkey_up: Idle, left_down: RunLeftUp, downkey_down: Idle, right_down: RunRightUp,
        #             left_up: RunRightUp, right_up: RunLeftUp},
        #     RunLeftUp: {right_down: RunUp, downkey_down: RunLeft, left_up: RunUp, upkey_up: RunLeft},
        #     RunLeft: {left_up: Idle, upkey_down: RunLeftUp, right_down: Idle, downkey_down: RunLeftDown,
        #               upkey_up: RunLeftDown, downkey_up: RunLeftUp},
        #     RunLeftDown: {left_up: RunDown, downkey_up: RunLeft, upkey_down: RunLeft, right_down: RunDown},
        #     RunDown: {downkey_up: Idle, left_down: RunLeftDown, upkey_down: Idle, right_down: RunRightDown,
        #               left_up: RunRightDown, right_up: RunLeftDown},
        #     RunRightDown: {right_up: RunDown, downkey_up: RunRight, left_down: RunDown, upkey_down: RunRight}
        # }

    def start(self):
        self.cur_state.enter(self.kirby, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.kirby)
        self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        self.kirby.x += math.cos(self.kirby.dir) * self.kirby.speed * game_framework.frame_time
        self.kirby.y += math.sin(self.kirby.dir) * self.kirby.speed * game_framework.frame_time


    def handle_event(self, e):
        # for check_event, next_state in self.transitions[self.cur_state].items():
        #     if check_event(e):
        #         self.cur_state.exit(self.kirby, e)
        #         self.cur_state = next_state
        #         self.cur_state.enter(self.kirby, e)
        #         return True
        #
        # return False
        pass


class Kirby:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.action = 0
        self.image = load_image('texture/kirby_idle.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, 100, 100)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        pass
