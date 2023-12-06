from pico2d import *

import game_framework
import game_world
import server
from kirby_skill.kirby_fire import KirbyFire
from kirby_skill.kirby_inhale import KirbyInhale
from kirby_skill.kirby_sword import KirbySword


def right_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def bottom_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s


def bottom_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s


def top_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def top_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w


def left_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def space_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_0
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_0
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def skill1_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_1
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j


def skill1_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j


def skill2_down(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_1
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j


def skill2_up(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j


def guard(e):
    if server.kirby.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.kirby.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j


def time_out(e):
    return e[0] == 'TIME_OUT'


def on_the_ground(e):
    return e[0] == 'NONE' and e[1] == 0


def eat(e):
    return e[0] == 'EAT' and e[1] == 0


def end_inhale(e):
    return e[0] == 'END_INHALE' and e[1] == 0


def end_eat(e):
    return e[0] == 'END_EAT' and e[1] == 0


def respawn(e):
    return e[0] == 'RESPAWN' and e[1] == 0


def end_fire(e):
    return e[0] == 'END_FIRE' and e[1] == 0


def end_sword(e):
    return e[0] == 'END_SWORD' and e[1] == 0

def knockback(e):
    return e[0] == 'KNOCKBACK' and e[1] == 0


def end_knockback(e):
    return e[0] == 'END_KNOCKBACK' and e[1] == 0


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# class Delay:
#     @staticmethod
#     def enter(kirby, e):
#         kirby.image = load_image("texture/kirby.png")
#         if kirby.dir == 1:
#             kirby.action = 5
#         elif kirby.dir == -1:
#             kirby.action = 4
#         kirby.speed = 0
#
#     @staticmethod
#     def exit(kirby, e):
#         pass
#
#     @staticmethod
#     def do(kirby):
#         kirby.y_move -= server.gravity * game_framework.frame_time
#         if not kirby.flying:
#             kirby.y_move = 0
#         kirby.y += kirby.y_move * game_framework.frame_time
#
#     @staticmethod
#     def draw(kirby):
#         kirby.image.clip_draw(int(kirby.frame) * 100, kirby.action * 100, 100, 100, kirby.x, kirby.y)


class Respwan:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        kirby.x = 800
        kirby.y = 900
        kirby.life -= 1
        kirby.damage = 0

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        if kirby.dir == 1:
            kirby.image.clip_draw(int(kirby.frame) * 100, 500, 100, 100, kirby.x, kirby.y)
        elif kirby.dir == -1:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 500, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class Idle:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        if kirby.dir == 1:
            kirby.action = 5
        elif kirby.dir == -1:
            kirby.action = 4
        kirby.speed = 0

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
            kirby.jumpCount = 5
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
            kirby.jumpCount = 5
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
            kirby.jumpCount = 5
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
                kirby.y_move = 300
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
                kirby.y_move = 300

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
                kirby.y_move = 300

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


class Inhale:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby_inhale.png")
        kirby.inhale = KirbyInhale(kirby.x + 75 * kirby.dir, kirby.y)
        game_world.add_object(kirby.inhale)
        game_world.add_collision_pair('kirby_inhale:sonic', kirby.inhale, None)
        if kirby.player_number == 1:
            server.inhaled_time2 = 0
        elif kirby.player_number == 2:
            server.inhaled_time1 = 0

    @staticmethod
    def exit(kirby, e):
        game_world.remove_object(kirby.inhale)
        kirby.inhale = None

    @staticmethod
    def do(kirby):
        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

        if kirby.player_number == 1 and server.inhaled_time2 >= 0.5 or kirby.player_number == 2 and server.inhaled_time1 >= 0.5:
            kirby.state_machine.handle_event(('EAT', 0))

    @staticmethod
    def draw(kirby):
        if kirby.dir == 1:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)
        elif kirby.dir == -1:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class Fire:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        kirby.fire = KirbyFire(kirby.x, kirby.y)
        game_world.add_object(kirby.fire)
        game_world.add_collision_pair('kirby_fire:sonic', kirby.fire, None)
        kirby.fire_time = get_time()

    @staticmethod
    def exit(kirby, e):
        game_world.remove_object(kirby.fire)
        kirby.fire = None

    @staticmethod
    def do(kirby):
        if get_time() - kirby.fire_time >= 1.0:
            kirby.state_machine.handle_event(('END_FIRE', 0))
        kirby.y_move = 0
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time * 1.5 * kirby.dir

    @staticmethod
    def draw(kirby):
        pass


class Sword:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        if skill1_down(e):
            kirby.sword = KirbySword(kirby.x, kirby.y)
            game_world.add_object(kirby.sword)
            game_world.add_collision_pair('kirby_sword:sonic', kirby.sword, None)
            kirby.sword_time = get_time()

    @staticmethod
    def exit(kirby, e):
        if not left_down(e) and not right_down(e):
            game_world.remove_object(kirby.sword)

    @staticmethod
    def do(kirby):
        if get_time() - kirby.sword_time >= 1.0:
            kirby.state_machine.handle_event(('END_SWORD', 0))
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        pass


class SwordLeft:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        if skill1_down(e):
            kirby.sword = KirbySword(kirby.x, kirby.y)
            game_world.add_object(kirby.sword)
            game_world.add_collision_pair('kirby_sword:sonic', kirby.sword, None)
            kirby.sword_time = get_time()

    @staticmethod
    def exit(kirby, e):
        if not left_up(e) and not right_down(e):
            game_world.remove_object(kirby.sword)

    @staticmethod
    def do(kirby):
        if get_time() - kirby.sword_time >= 1.0:
            kirby.state_machine.handle_event(('END_SWORD', 0))
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        pass


class SwordRight:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        if skill1_down(e):
            kirby.sword = KirbySword(kirby.x, kirby.y)
            game_world.add_object(kirby.sword)
            game_world.add_collision_pair('kirby_sword:sonic', kirby.sword, None)
            kirby.sword_time = get_time()

    @staticmethod
    def exit(kirby, e):
        if not right_up(e) and not left_down(e):
            game_world.remove_object(kirby.sword)

    @staticmethod
    def do(kirby):
        if get_time() - kirby.sword_time >= 1.0:
            kirby.state_machine.handle_event(('END_SWORD', 0))
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y_move -= server.gravity / 4 * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        pass


class Eat:
    @staticmethod
    def enter(kirby, e):
        if eat(e):
            kirby.eating_time = get_time()
        kirby.image = load_image("texture/kirby_eating.png")
        kirby.inhale = KirbyInhale(kirby.x + 75 * kirby.dir, kirby.y)

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        if get_time() - kirby.eating_time > 1.5:
            kirby.state_machine.handle_event(('END_INHALE', 0))

        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        if kirby.dir == 1:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)
        elif kirby.dir == -1:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class EatLeft:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby_eating.png")
        kirby.dir = -1

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        if get_time() - kirby.eating_time > 3.0:
            kirby.state_machine.handle_event(('END_INHALE', 0))

        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class EatRight:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby_eating.png")
        kirby.dir = 1

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        if get_time() - kirby.eating_time > 3.0:
            kirby.state_machine.handle_event(('END_INHALE', 0))

        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)


class EndInhale:
    @staticmethod
    def enter(kirby, e):
        kirby.frame = 0
        kirby.image = load_image("texture/kirby_end_inhale.png")

    @staticmethod
    def exit(kirby, e):
        if kirby.player_number == 1:
            server.player2.state_machine.handle_event(('KNOCKBACK', 0))
        elif kirby.player_number == 2:
            server.player1.state_machine.handle_event(('KNOCKBACK', 0))

    @staticmethod
    def do(kirby):
        if kirby.frame >= 8:
            kirby.state_machine.handle_event(('END_EAT', 0))
        kirby.y_move -= server.gravity * game_framework.frame_time
        if not kirby.flying:
            kirby.y_move = 0
        kirby.y += kirby.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        if kirby.dir == 1:
            kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y)
        elif kirby.dir == -1:
            kirby.image.clip_composite_draw(int(kirby.frame) * 100, 0, 100, 100, 0, 'h', kirby.x, kirby.y, 100, 100)


class Knockback:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby.png")
        if kirby.dir == 1:
            kirby.action = 5
        elif kirby.dir == -1:
            kirby.action = 4
        kirby.damage += 150
        kirby.x_move = kirby.damage * 5
        kirby.y_move = kirby.damage * 2
        kirby.knockback_time = get_time()

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        if get_time() - kirby.knockback_time > 0.5:
            kirby.state_machine.handle_event(('END_KNOCKBACK', 0))
        kirby.y_move -= server.gravity * game_framework.frame_time
        kirby.y += kirby.y_move * game_framework.frame_time
        kirby.x_move -= kirby.x_move / 50
        kirby.y_move -= kirby.y_move / 50
        if kirby.player_number == 1:
            kirby.x += kirby.x_move * server.player2.dir * game_framework.frame_time
        elif kirby.player_number == 2:
            kirby.x += kirby.x_move * server.player1.dir * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        if sonic.dir == 1:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)
        elif sonic.dir == -1:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class KirbyWin:
    @staticmethod
    def enter(kirby, e):
        kirby.image = load_image("texture/kirby_win.png")

    @staticmethod
    def exit(kirby, e):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(int(kirby.frame) * 100, 0, 100, 100, kirby.x, kirby.y, 150, 150)



class StateMachine:
    def __init__(self, kirby):
        self.kirby = kirby
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: RunRight, left_down: RunLeft, space_down: Jump,
                   skill1_down: Inhale, respawn: Respwan, knockback: Knockback},
            RunLeft: {right_down: RunRight, left_up: Idle, space_down: JumpLeft, respawn: Respwan, skill1_down: Fire, knockback: Knockback},
            RunRight: {left_down: RunLeft, right_up: Idle, space_down: JumpRight, respawn: Respwan, skill1_down: Fire, knockback: Knockback},
            Jump: {right_down: JumpRight, left_down: JumpLeft, left_up: JumpRight, right_up: JumpLeft,
                   on_the_ground: Idle, space_down: DoubleJump, respawn: Respwan, skill1_down: Sword, knockback: Knockback},
            JumpLeft: {right_down: JumpRight, left_up: Jump, on_the_ground: RunLeft, space_down: DoubleJumpLeft, respawn: Respwan,
                       skill1_down: SwordLeft, knockback: Knockback},
            JumpRight: {left_down: JumpLeft, right_up: Jump, on_the_ground: RunRight, space_down: DoubleJumpRight, respawn: Respwan
                        , skill1_down: SwordRight, knockback: Knockback},
            DoubleJump: {on_the_ground: Idle, space_down: DoubleJump, left_down: DoubleJumpLeft,
                         right_down: DoubleJumpRight, respawn: Respwan, skill1_down: Sword, knockback: Knockback},
            DoubleJumpLeft: {on_the_ground: RunLeft, space_down: DoubleJumpLeft, left_up: DoubleJump,
                             right_down: DoubleJumpRight, respawn: Respwan, skill1_down: SwordLeft, knockback: Knockback},
            DoubleJumpRight: {on_the_ground: RunRight, space_down: DoubleJumpRight, right_up: DoubleJump,
                              left_down: DoubleJumpLeft, respawn: Respwan, skill1_down: SwordRight, knockback: Knockback},
            Inhale: {skill1_up: Idle, eat: Eat, respawn: Respwan, knockback: Knockback},
            Eat: {end_inhale: EndInhale, left_down: EatLeft, right_down: EatRight, bottom_down: EndInhale, respawn: Respwan, knockback: Knockback},
            EatLeft: {end_inhale: EndInhale, left_up: Eat, right_down: EatRight, bottom_down: EndInhale, respawn: Respwan, knockback: Knockback},
            EatRight: {end_inhale: EndInhale, right_up: Eat, left_up: EatLeft, bottom_down: EndInhale, respawn: Respwan, knockback: Knockback},
            EndInhale: {end_eat: Idle, respawn: Respwan, knockback: Knockback},
            Respwan: {space_down: Jump},
            Fire: {end_fire: Idle, respawn: Respwan, knockback: Knockback},
            Sword: {end_sword: Idle, space_down: DoubleJump, respawn: Respwan, left_down: SwordLeft, right_down: SwordRight, knockback: Knockback},
            SwordLeft: {end_sword: RunLeft, right_down: SwordRight, left_up: Sword, respawn: Respwan, knockback: Knockback},
            SwordRight: {end_sword: RunRight, left_down: SwordLeft, right_up: Sword, respawn: Respwan, knockback: Knockback},
            Knockback: {end_knockback: Idle},
            KirbyWin: {}
        }

    def start(self):
        self.cur_state.enter(self.kirby, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.kirby)

        if self.cur_state == Idle:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        elif self.cur_state == DoubleJump or self.cur_state == DoubleJumpLeft or self.cur_state == DoubleJumpRight:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        elif self.cur_state == Eat or self.cur_state == EatLeft or self.cur_state == EatRight:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        elif self.cur_state == Respwan:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20
        elif self.cur_state == EndInhale:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        elif self.cur_state == KirbyWin:
            self.kirby.frame = (self.kirby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 18
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
        self.x_move = 0
        self.y_move = 0
        self.knockback_time = 0
        self.face_dir = True
        self.jumpCount = 4
        self.player_number = 0
        self.inhale = None
        self.eating_time = 0
        self.damage = 0.0
        self.life = 3
        self.fire = None
        self.fire_time = 0
        self.sword = None
        self.sword_time = 0
        self.left, self.bottom, self.right, self.top = self.get_bb()
        self.image = load_image('texture/kirby.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        self.left, self.bottom, self.right, self.top = self.get_bb()
        for ground in server.grounds:
            ground_left, ground_bottom, ground_right, ground_top = ground.get_bb()
            if self.left <= ground_right and self.right >= ground_left and self.bottom <= ground_top and self.bottom >= ground_top - 20:
                self.state_machine.handle_event(('NONE', 0))  # 땅과 충돌하면 Idle 상태로 전환
                self.flying = False
                self.y += ground_top - self.bottom
                return
            else:
                self.flying = True

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y

    def handle_collision(self, group, other):
        if group == 'kirby:deadline':
            self.state_machine.handle_event(('RESPAWN', 0))
        if group == 'sonic_ball:kirby':
            self.state_machine.handle_event(('KNOCKBACK', 0))
        if group == 'kirby:cake':
            self.damage -= 100
            if self.damage > 0:
                self.damage = 0
