from pico2d import *
import game_framework

import game_world
import kirby
import server
from background import Background
from ground import Ground
from kirby import Kirby


def init():
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.kirby = Kirby(400, 400)
    game_world.add_object(server.kirby, 2)
    game_world.add_collision_pair('kirby:ground', server.kirby, None)

    server.grounds = [Ground(1000, 300), Ground(600, 600), Ground(200, 300)]
    for o in server.grounds:
        game_world.add_object(o, 1)
        game_world.add_collision_pair('kirby:ground', None, o)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.kirby.handle_event(event)



def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
