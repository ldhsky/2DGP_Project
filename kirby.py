from pico2d import *

import game_framework
import server


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def w_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def w_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w


def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s


def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s


def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def d_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def time_out(e):
    return e[0] == 'TIME_OUT'





# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
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
        kirby.image = load_image("texture/kirby.png")
        if kirby.action == 3:
            kirby.action = 5
        elif kirby.action == 2:
            kirby.action = 4
        kirby.speed = 0
        kirby.dir = 0
        kirby.y_move = 0
        kirby.fly = False

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y -= kirby.y_move

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class Run:
    @staticmethod
    def enter(kirby, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            kirby.dir, kirby.action = 1, 3
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            kirby.dir, kirby.action = -1, 2

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        # boy.frame = (boy.frame + 1) % 8
        kirby.x += kirby.dir * RUN_SPEED_PPS * game_framework.frame_time
        kirby.y -= kirby.y_move
        # kirby.x = clamp(25, kirby.x, 1600 - 25)
        # kirby.frame = (kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class Jump:
    @staticmethod
    def enter(kirby, e):
        # if right_down(e) or left_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = 1, 3, 1
        # elif left_down(e) or right_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = -1, 2, -1
        if space_down(e):
            kirby.image = load_image('texture/kirby_jump.png')
            kirby.y_move = 800
        kirby.fly = True
        kirby.flying = True

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= 1000 * game_framework.frame_time
        # boy.frame = (boy.frame + 1) % 8
        # kirby.x += kirby.dir * RUN_SPEED_PPS * game_framework.frame_time
        # kirby.x = clamp(25, kirby.x, 1600 - 25)
        # kirby.frame = (kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        if kirby.dir == 1:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)
        else:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class JumpLeft:
    @staticmethod
    def enter(kirby, e):
        # if right_down(e) or left_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = 1, 3, 1
        # elif left_down(e) or right_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = -1, 2, -1
        pass

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= 1000 * game_framework.frame_time
        # boy.frame = (boy.frame + 1) % 8
        # kirby.x += kirby.dir * RUN_SPEED_PPS * game_framework.frame_time
        # kirby.x = clamp(25, kirby.x, 1600 - 25)
        # kirby.frame = (kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class JumpRight:
    @staticmethod
    def enter(kirby, e):
        # if right_down(e) or left_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = 1, 3, 1
        # elif left_down(e) or right_up(e):
        #     kirby.dir, kirby.action, kirby.face_dir = -1, 2, -1
        pass

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= 1000 * game_framework.frame_time
        # boy.frame = (boy.frame + 1) % 8
        # kirby.x += kirby.dir * RUN_SPEED_PPS * game_framework.frame_time
        # kirby.x = clamp(25, kirby.x, 1600 - 25)
        # kirby.frame = (kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)


class StateMachine:
    def __init__(self, kirby):
        self.kirby = kirby
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Jump},
            Run: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, space_down: Jump},
            Jump: {right_down: JumpRight, left_down: JumpLeft, left_up: JumpRight, right_up: JumpLeft},
            JumpLeft: {right_down: Jump, left_up: Jump},
            JumpRight: {left_down: Jump, right_up: Jump}
        }

    def start(self):
        self.cur_state.enter(self.kirby, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.kirby)

        if self.cur_state == Idle:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

        else:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.kirby.x += math.cos(self.kirby.dir) * self.kirby.speed * game_framework.frame_time
        self.kirby.y += math.sin(self.kirby.dir) * self.kirby.speed * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if self.kirby.fly and not self.kirby.flying:
                self.cur_state.exit(self.kirby, e)
                self.cur_state = Idle
                self.cur_state.enter(self.kirby, e)
                return True
            if check_event(e):
                self.cur_state.exit(self.kirby, e)
                self.cur_state = next_state
                self.cur_state.enter(self.kirby, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.kirby)


class Kirby:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.fly = False
        self.flying = False
        self.frame = 0
        self.action = 5
        self.image = load_image('texture/kirby.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.y_move = 0

    def update(self):
        self.state_machine.update()
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        #self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y

    def handle_collision(self, group, other):
        if group == 'kirby:ground':
            self.flying = False
