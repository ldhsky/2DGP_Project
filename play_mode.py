from pico2d import *
import game_framework

import game_world
import kirby
import server
from background import Background
from kirby import Kirby


def init():
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.kirby = Kirby(400, 400)
    game_world.add_object(server.kirby, 1)
    pass


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
