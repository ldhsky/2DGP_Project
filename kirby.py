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


def on_the_ground(e):
    return e[0] == 'NONE' and e[1] == 0


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
        if kirby.dir == 1:
            kirby.action = 5
        elif kirby.dir == -1:
            kirby.action = 4
        kirby.speed = 0
        kirby.dir = 0

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class RunLeft:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        kirby.dir, kirby.action = -1, 2


    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        # boy.frame = (boy.frame + 1) % 8
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time
        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class RunRight:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        kirby.dir, kirby.action = 1, 3

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        # boy.frame = (boy.frame + 1) % 8
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time
        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class Jump:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.jumpCount = 4
            kirby.image = load_image('texture/kirby_jump.png')
            kirby.y_move = 800
        if kirby.dir == 1:
            kirby.face_dir = True
        elif kirby.dir == -1:
            kirby.face_dir = False

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        if kirby.face_dir:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y, 90, 90)
        else:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 90, 90)


class JumpLeft:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.jumpCount = 4
        if not kirby.flying:
            kirby.y_move = 800
            kirby.image = load_image('texture/kirby_jump.png')
        kirby.dir = -1

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 90, 90)


class JumpRight:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.jumpCount = 4
        if not kirby.flying:
            kirby.y_move = 800
            kirby.image = load_image('texture/kirby_jump.png')
        kirby.dir = 1

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y, 90, 90)


class DoubleJump:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.image = load_image('texture/kirby_doublejump.png')
            kirby.jumpCount -= 1
        if kirby.jumpCount > 0:
            kirby.y_move = 200
        if kirby.dir == 1:
            kirby.face_dir = True
        elif kirby.dir == -1:
            kirby.face_dir = False

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        if kirby.face_dir:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y, 90, 90)
        else:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 90, 90)


class DoubleJumpLeft:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.jumpCount -= 1
            kirby.image = load_image('texture/kirby_doublejump.png')
        if kirby.jumpCount > 0:
            kirby.y_move = 200

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 90, 90)


class DoubleJumpRight:
    @staticmethod
    def enter(kirby, e):
        if space_down(e):
            kirby.jumpCount -= 1
            kirby.image = load_image('texture/kirby_doublejump.png')
        if kirby.jumpCount > 0:
            kirby.y_move = 200


    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y, 90, 90)



class StateMachine:
    def __init__(self, kirby):
        self.kirby = kirby
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, space_down: Jump},
            RunLeft: {right_down: Idle, left_up: Idle, space_down: JumpLeft},
            RunRight: {left_down: Idle, right_up: Idle, space_down: JumpRight},
            Jump: {right_down: JumpRight, left_down: JumpLeft, left_up: JumpRight, right_up: JumpLeft,
                   on_the_ground: Idle, space_down: DoubleJump},
            JumpLeft: {right_down: Jump, left_up: Jump, on_the_ground: RunLeft, space_down: DoubleJumpLeft},
            JumpRight: {left_down: Jump, right_up: Jump, on_the_ground: RunRight, space_down: DoubleJumpRight},
            DoubleJump: {on_the_ground: Idle, space_down: DoubleJump, left_down: DoubleJumpLeft, right_down: DoubleJumpRight},
            DoubleJumpLeft: {on_the_ground: RunLeft, space_down: DoubleJumpLeft, left_up: DoubleJump, right_down: DoubleJumpRight},
            DoubleJumpRight: {on_the_ground: RunRight, space_down: DoubleJumpRight, right_up: DoubleJump, left_down: DoubleJumpLeft}
        }

    def start(self):
        self.cur_state.enter(self.kirby, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.kirby)

        if self.cur_state == Idle:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        elif self.cur_state == DoubleJump or self.cur_state == DoubleJumpLeft or self.cur_state == DoubleJumpRight:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        else:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.kirby.x += math.cos(self.kirby.dir) * self.kirby.speed * game_framework.frame_time
        self.kirby.y += math.sin(self.kirby.dir) * self.kirby.speed * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
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
        self.dir = 1
        self.flying = False
        self.frame = 0
        self.action = 5
        self.y_move = 0
        self.face_dir = True
        self.jumpCount = 4
        self.left, self.bottom, self.right, self.top = self.get_bb()
        self.image = load_image('texture/kirby.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)
        self.left, self.bottom, self.right, self.top = self.get_bb()
        for ground in server.grounds:
            ground_left, ground_bottom, ground_right, ground_top = ground.get_bb()
            if self.left <= ground_right and self.right >= ground_left and self.bottom <= ground_top and self.bottom >= ground_top - 10:
                self.state_machine.handle_event(('NONE', 0))  # 땅과 충돌하면 Idle 상태로 전환
                self.flying = False
                self.y += ground_top - self.bottom
                return
            else:
                self.flying = True


    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        #self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y

    def handle_collision(self, group, other):
        pass
