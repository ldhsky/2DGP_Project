from pico2d import *
import game_framework

import game_world
import kirby
import server
from background import Background
from ground import Ground
from kirby import Kirby
from sonic import Sonic


def init():
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.player1 = Kirby(400, 400)
    server.player1.player_number = 1

    game_world.add_object(server.player1, 2)
    game_world.add_collision_pair('kirby:ground', server.player1, None)

    server.grounds = [Ground(1000, 300), Ground(600, 600), Ground(200, 300)]
    for o in server.grounds:
        game_world.add_object(o, 1)
        game_world.add_collision_pair('kirby:ground', None, o)

    server.player2 = Sonic(1400, 400)
    server.player2.player_number = 2
    game_world.add_object(server.player2, 2)
    game_world.add_collision_pair('sonic:ground', server.player2, None)
    game_world.add_collision_pair('kirby_inhale:sonic', None, server.player2)

    server.kirby = Kirby(400, 400)
    server.kirby.player_number = 1
    server.sonic = Sonic(1400, 400)
    server.sonic.player_number = 2


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


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
