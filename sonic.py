from pico2d import *

import game_framework
import game_world
import server
from sonic_skill.sonic_ball import SonicBall


def respawn(e):
    return e[0] == 'RESPAWN' and e[1] == 0


def right_down(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def space_down(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_0
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_0
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


def on_the_ground(e):
    return e[0] == 'GROUND' and e[1] == 0


def inhaled(e):
    return e[0] == 'INHALED' and e[1] == 0


def skill1_down(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_1
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j


def skill1_up(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j


def skill2_down(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_1
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j


def skill2_up(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j


def knockback(e):
    return e[0] == 'KNOCKBACK' and e[1] == 0


def end_knockback(e):
    return e[0] == 'END_KNOCKBACK' and e[1] == 0

def end_ball(e):
    return e[0] == 'END_BALL' and e[1] == 0

def end_groggy(e):
    return e[0] == 'END_GROGGY' and e[1] == 0

def groggy(e):
    return e[0] == 'GROGGY' and e[1] == 0


def guard(e):
    if server.sonic.player_number == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_1
    elif server.sonic.player_number == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j




# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Respwan:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic.png")
        if sonic.dir == 1:
            sonic.action = 5
        elif sonic.dir == -1:
            sonic.action = 4
        sonic.x = 800
        sonic.y = 900
        sonic.life -= 1
        sonic.damage= 0
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        pass

    @staticmethod
    def draw(sonic):
        if sonic.dir == 1:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)
        elif sonic.dir == -1:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class Idle:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic.png")
        if sonic.dir == 1:
            sonic.action = 5
        elif sonic.dir == -1:
            sonic.action = 4
        sonic.speed = 0
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        if sonic.dir == 1:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)
        elif sonic.dir == -1:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class RunLeft:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic_run.png")
        sonic.dir, sonic.action = -1, 2
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        # boy.frame = (boy.frame + 1) % 8
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time
        sonic.y_move -= server.gravity * game_framework.frame_time
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class RunRight:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic_run.png")
        sonic.dir, sonic.action = 1, 3
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        # boy.frame = (boy.frame + 1) % 8
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time
        sonic.y_move -= server.gravity * game_framework.frame_time
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)


class Jump:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.image = load_image('texture/sonic_jump.png')
            sonic.y_move = 1000
        if sonic.dir == 1:
            sonic.face_dir = True
        elif sonic.dir == -1:
            sonic.face_dir = False

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        if sonic.face_dir:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 90, 90)
        else:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 90, 90)


class BallJump:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.image = load_image('texture/sonic_ball.png')
            sonic.y_move = 1000
        if sonic.dir == 1:
            sonic.face_dir = True
        elif sonic.dir == -1:
            sonic.face_dir = False
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()

    @staticmethod
    def exit(sonic, e):
        if not left_down(e) and not right_down(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass


class JumpLeft:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.y_move = 1000
            sonic.image = load_image('texture/sonic_jump.png')
        sonic.dir = -1

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 90, 90)


class BallJumpLeft:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.y_move = 1000
            sonic.image = load_image('texture/sonic_jump.png')
        sonic.dir = -1
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()

    @staticmethod
    def exit(sonic, e):
        if not left_up(e) and not right_down(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass


class JumpRight:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.y_move = 1000
            sonic.image = load_image('texture/sonic_jump.png')
        sonic.dir = 1

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 90, 90)


class BallJumpRight:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount = 2
            sonic.y_move = 1000
            sonic.image = load_image('texture/sonic_jump.png')
        sonic.dir = 1
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()

    @staticmethod
    def exit(sonic, e):
        if not left_down(e) and not right_up(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass


class DoubleJump:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.image = load_image('texture/sonic_jump.png')
            sonic.jumpCount -= 1
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if sonic.dir == 1:
            sonic.face_dir = True
        elif sonic.dir == -1:
            sonic.face_dir = False
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        if sonic.face_dir:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 90, 90)
        else:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 90, 90)

class BallDoubleJump:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.image = load_image('texture/sonic_jump.png')
            sonic.jumpCount -= 1
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if sonic.dir == 1:
            sonic.face_dir = True
        elif sonic.dir == -1:
            sonic.face_dir = False
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        if not left_down(e) and not right_down(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass

class DoubleJumpLeft:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount -= 1
            sonic.image = load_image('texture/sonic_jump.png')
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 90, 90)


class BallDoubleJumpLeft:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount -= 1
            sonic.image = load_image('texture/sonic_jump.png')
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        if not left_up(e) and not right_down(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass


class DoubleJumpRight:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount -= 1
            sonic.image = load_image('texture/sonic_jump.png')
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 90, 90)


class BallDoubleJumpRight:
    @staticmethod
    def enter(sonic, e):
        if space_down(e):
            sonic.jumpCount -= 1
            sonic.image = load_image('texture/sonic_jump.png')
            if sonic.jumpCount > 0:
                sonic.y_move = 1000
        if skill1_down(e):
            sonic.groggy_time = get_time()
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        if not left_down(e) and not right_up(e) and not space_down(e) and not on_the_ground(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass

class Inhaled:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image('texture/temp.png')
        sonic.inhaled_time = 0


    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        sonic.y = server.player1.y
        sonic.x = server.player1.x

    @staticmethod
    def draw(sonic):
        sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 90, 90)


class Ball:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic.png")
        if skill1_down(e):
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0
    @staticmethod
    def exit(sonic, e):
        if not left_down(e) and not right_down(e) and not space_down(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y_move -= server.gravity / 4 * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        pass


class BallLeft:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic.png")
        if skill1_down(e):
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        if not left_up(e) and not right_down(e) and not space_down(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y_move -= server.gravity / 4 * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        pass


class BallRight:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic.png")
        if skill1_down(e):
            sonic.ball = SonicBall(sonic.x, sonic.y)
            game_world.add_object(sonic.ball)
            game_world.add_collision_pair('sonic_ball:kirby', sonic.ball, None)
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        if not right_up(e) and not left_down(e) and not space_down(e):
            game_world.remove_object(sonic.ball)

    @staticmethod
    def do(sonic):
        if get_time() - sonic.ball_time >= 4.0:
            sonic.state_machine.handle_event(('GROGGY', 0))
            sonic.ball_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y_move -= server.gravity / 4 * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x += RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(kirby):
        pass


class KnockBack:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic_knockback.png")
        if sonic.dir == 1:
            sonic.action = 5
        elif sonic.dir == -1:
            sonic.action = 4
        sonic.damage += 150
        sonic.x_move = sonic.damage * 5
        sonic.y_move = sonic.damage * 2
        sonic.knockback_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        if get_time() - sonic.knockback_time > 0.5:
            sonic.state_machine.handle_event(('END_KNOCKBACK', 0))
        sonic.y_move -= server.gravity * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time
        sonic.x_move -= sonic.x_move / 50
        sonic.y_move -= sonic.y_move / 50
        if sonic.player_number == 1:
            sonic.x += sonic.x_move * server.player2.dir * game_framework.frame_time
        elif sonic.player_number == 2:
            sonic.x += sonic.x_move * server.player1.dir * game_framework.frame_time

    @staticmethod
    def draw(sonic):
        if sonic.dir == 1:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)
        elif sonic.dir == -1:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class Groggy:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic_knockback.png")
        sonic.groggy_time = get_time()
        if not sonic.flying:
            sonic.y_move = 0

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        if get_time() - sonic.groggy_time > 3.0:
            sonic.state_machine.handle_event(('END_GROGGY', 0))
        if not sonic.flying:
            sonic.y_move = 0
        sonic.y_move -= server.gravity / 4 * game_framework.frame_time
        sonic.y += sonic.y_move * game_framework.frame_time


    @staticmethod
    def draw(sonic):
        if sonic.dir == 1:
            sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y)
        elif sonic.dir == -1:
            sonic.image.clip_composite_draw(int(sonic.frame) * 100, 0, 100, 100, 0, 'h', sonic.x, sonic.y, 100, 100)


class SonicWin:
    @staticmethod
    def enter(sonic, e):
        sonic.image = load_image("texture/sonic_win.png")

    @staticmethod
    def exit(sonic, e):
        pass

    @staticmethod
    def do(sonic):
        pass

    @staticmethod
    def draw(sonic):
        sonic.image.clip_draw(int(sonic.frame) * 100, 0, 100, 100, sonic.x, sonic.y, 150, 150)


class StateMachine:
    def __init__(self, sonic):
        self.sonic = sonic
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, space_down: Jump,
                   inhaled: Inhaled, knockback: KnockBack, respawn: Respwan, skill1_down: Ball},
            RunLeft: {right_down: Idle, left_up: Idle, space_down: JumpLeft,
                      inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallLeft},
            RunRight: {left_down: Idle, right_up: Idle, space_down: JumpRight,
                       inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallRight},
            Jump: {right_down: JumpRight, left_down: JumpLeft, left_up: JumpRight, right_up: JumpLeft,
                   on_the_ground: Idle, space_down: DoubleJump, skill1_down: BallJump,
                   inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, knockback: KnockBack},
            JumpLeft: {right_down: Jump, left_up: Jump, on_the_ground: RunLeft, space_down: DoubleJumpLeft,
                       inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallJumpLeft},
            JumpRight: {left_down: Jump, right_up: Jump, on_the_ground: RunRight, space_down: DoubleJumpRight,
                        inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallJumpRight},
            DoubleJump: {on_the_ground: Idle, space_down: DoubleJump, left_down: DoubleJumpLeft, right_down: DoubleJumpRight,
                         inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallDoubleJump},
            DoubleJumpLeft: {on_the_ground: RunLeft, space_down: DoubleJumpLeft, left_up: DoubleJump, right_down: DoubleJumpRight,
                             inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallDoubleJumpLeft},
            DoubleJumpRight: {on_the_ground: RunRight, space_down: DoubleJumpRight, right_up: DoubleJump, left_down: DoubleJumpLeft,
                              inhaled: Inhaled, respawn: Respwan, knockback: KnockBack, skill1_down: BallDoubleJumpRight},
            Inhaled: {knockback: KnockBack, respawn: Respwan, knockback: KnockBack, inhaled: Inhaled},
            KnockBack: {end_knockback: Idle, respawn: Respwan},
            Respwan: {space_down: Jump},
            Ball: {knockback: KnockBack, right_down: BallRight, left_down: BallLeft, groggy: Groggy, respawn: Respwan,
                   space_down: BallJump, inhaled: Inhaled},
            BallLeft: {knockback: KnockBack, right_down: BallRight, left_up: Ball, groggy: Groggy, respawn: Respwan,
                       space_down: BallJumpLeft, inhaled: Inhaled},
            BallRight: {knockback: KnockBack, right_up: Ball, left_down: BallLeft, groggy: Groggy, respawn: Respwan,
                        space_down: BallJumpRight, inhaled: Inhaled},
            BallJump: {groggy: Groggy, space_down: BallDoubleJump, left_down: BallJumpLeft, right_down: BallJumpRight, respawn: Respwan,
                       on_the_ground: Ball, inhaled: Inhaled},
            BallJumpLeft: {groggy: Groggy, right_down: BallJumpRight, left_up: BallJump, respawn: Respwan,
                           space_down: BallDoubleJumpLeft, on_the_ground: BallLeft, inhaled: Inhaled},
            BallJumpRight: {groggy: Groggy, left_down: BallJumpLeft, right_up: BallJump, respawn: Respwan,
                            space_down: BallDoubleJumpRight, on_the_ground: BallRight, inhaled: Inhaled},
            BallDoubleJump: {groggy: Groggy, right_down: BallDoubleJumpRight, left_down: BallDoubleJumpLeft, respawn: Respwan,
                             space_down: BallDoubleJump, on_the_ground: Ball, inhaled: Inhaled},
            BallDoubleJumpLeft: {groggy: Groggy, right_down: BallDoubleJumpRight, left_up: BallDoubleJump, respawn: Respwan,
                                 space_down: BallDoubleJumpLeft, on_the_ground: BallLeft, inhaled: Inhaled},
            BallDoubleJumpRight: {groggy: Groggy, left_down: BallDoubleJumpLeft, right_up: BallDoubleJump, respawn: Respwan,
                                  space_down: BallDoubleJumpRight, on_the_ground: BallRight, inhaled: Inhaled},
            Groggy: {end_groggy: Idle, respawn: Respwan, knockback: KnockBack, inhaled: Inhaled},
            SonicWin: {}
        }

    def start(self):
        self.cur_state.enter(self.sonic, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.sonic)

        if self.cur_state == Idle:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        elif self.cur_state == DoubleJump or self.cur_state == DoubleJumpLeft or self.cur_state == DoubleJumpRight:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        elif self.cur_state == KnockBack or self.cur_state == Groggy:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        elif self.cur_state == Respwan:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        elif self.cur_state == Ball or self.cur_state == BallLeft or self.cur_state == BallRight\
                or self.cur_state == BallJump or self.cur_state == BallJumpLeft or self.cur_state == BallJumpRight\
                or self.cur_state == BallDoubleJump or self.cur_state == BallDoubleJumpLeft or self.cur_state == BallDoubleJumpRight\
                or self.cur_state == SonicWin:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        else:
            self.sonic.frame = (self.sonic.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.sonic.x += math.cos(self.sonic.dir) * self.sonic.speed * game_framework.frame_time
        self.sonic.y += math.sin(self.sonic.dir) * self.sonic.speed * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.sonic, e)
                self.cur_state = next_state
                self.cur_state.enter(self.sonic, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.sonic)


class Sonic:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.dir = 1
        self.flying = False
        self.frame = 0
        self.action = 5
        self.x_move = 0
        self.y_move = 0
        self.face_dir = True
        self.jumpCount = 1
        self.player_number = 0
        self.inhaled_time = 0
        self.knockback_time = 0
        self.groggy_time = 0
        self.damage = 0.0
        self.life = 3
        self.ball = None
        self.ball_time = 0
        self.left, self.bottom, self.right, self.top = self.get_bb()
        self.image = load_image('texture/sonic.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)
        self.left, self.bottom, self.right, self.top = self.get_bb()
        for ground in server.grounds:
            ground_left, ground_bottom, ground_right, ground_top = ground.get_bb()
            if self.left <= ground_right and self.right >= ground_left and self.bottom <= ground_top and self.bottom >= ground_top - 20:
                self.state_machine.handle_event(('GROUND', 0))
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
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        if group == 'kirby_inhale:sonic':
            if self.player_number == 1:
                server.inhaled_time1 += game_framework.frame_time
            elif self.player_number == 2:
                server.inhaled_time2 += game_framework.frame_time
        else:
            if self.player_number == 1:
                server.inhaled_time1 = 0
            elif self.player_number == 2:
                server.inhaled_time2 = 0

        if group == 'kirby_fire:sonic' or group == 'kirby_sword:sonic':
            self.state_machine.handle_event(('KNOCKBACK', 0))

        if self.player_number == 1 and server.inhaled_time1 >= 0.5 or self.player_number == 2 and server.inhaled_time2 >= 0.5:
            self.state_machine.handle_event(('INHALED', 0))

        if group == 'sonic:deadline':
            self.state_machine.handle_event(('RESPAWN', 0))

        if group == 'sonic:cake':
            self.damage -= 100
            if self.damage > 0:
                self.damage = 0
