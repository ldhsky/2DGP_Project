import random

from pico2d import *

import Result_mode
import game_framework

import game_world
import kirby
import server
from background import Background
from cake import Cake
from deadline import Deadline
from ground import Ground
from kirby import Kirby
from sonic import Sonic
from kirby_UI import KirbyUI
from sonic_UI import SonicUI

def init():
    hide_cursor()

    global prev_time
    prev_time = get_time()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.player1 = Kirby(1300, 800)
    server.player1.player_number = 1
    server.player1.dir = -1
    server.player1.life = 3
    server.player1.damage = 0

    game_world.add_object(server.player1, 2)
    game_world.add_collision_pair('kirby:ground', server.player1, None)
    game_world.add_collision_pair('kirby:deadline', server.player1, None)
    game_world.add_collision_pair('sonic_ball:kirby', None, server.player1)

    server.UI1 = KirbyUI(300, 50)
    game_world.add_object(server.UI1, 3)

    if random.randint(0, 1) == 1:
        server.grounds = [Ground(1000, 500), Ground(600, 200), Ground(200, 500)]
    else:
        server.grounds = [Ground(850, 200), Ground(800, 800), Ground(350, 200), Ground(400, 500)]
    for o in server.grounds:
        game_world.add_object(o, 1)
        game_world.add_collision_pair('kirby:ground', None, o)

    server.player2 = Sonic(400, 800)
    server.player2.player_number = 2
    server.player2.dir = 1
    server.player2.life = 3
    server.player2.damage = 0

    game_world.add_object(server.player2, 2)
    game_world.add_collision_pair('sonic:ground', server.player2, None)
    game_world.add_collision_pair('kirby_inhale:sonic', None, server.player2)
    game_world.add_collision_pair('sonic:deadline', server.player2, None)
    game_world.add_collision_pair('kirby_fire:sonic', None, server.player2)
    game_world.add_collision_pair('kirby_sword:sonic', None, server.player2)

    server.UI1 = SonicUI(1100, 50)
    game_world.add_object(server.UI1, 3)

    server.kirby = Kirby(400, 400)
    server.kirby.player_number = 1
    server.sonic = Sonic(1400, 400)
    server.sonic.player_number = 2

    server.deadlines = [Deadline(-1500, 500), Deadline(800, -1200), Deadline(3100, 500), Deadline(800, 2200)]
    for o in server.deadlines:
        game_world.add_object(o, 1)
        game_world.add_collision_pair('kirby:deadline', None, o)
        game_world.add_collision_pair('sonic:deadline', None, o)

    game_world.add_collision_pair('kirby:cake', server.player1, None)
    game_world.add_collision_pair('sonic:cake', server.player2, None)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.player1.handle_event(event)
            server.player2.handle_event(event)



def update():
    game_world.update()
    game_world.handle_collisions()
    global prev_time
    if server.player1.life <= 0 or server.player2.life <= 0:
        game_framework.change_mode(Result_mode)
    if get_time() - prev_time > 10.0:
        server.cake = Cake(random.randint(100, 1500), 1100)
        game_world.add_object(server.cake)
        game_world.add_collision_pair('kirby:cake', None, server.cake)
        game_world.add_collision_pair('sonic:cake', None, server.cake)
        prev_time = get_time()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
