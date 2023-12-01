from pico2d import *
import game_framework

import game_world

def init():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()



def finish():
    game_world.clear()
