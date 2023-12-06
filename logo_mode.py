from pico2d import *
import game_framework

import game_world
import kirby
import play_mode
import server
from background import Background
from deadline import Deadline
from ground import Ground
from kirby import Kirby
from sonic import Sonic


def init():
    hide_cursor()

    global image
    image = load_image('texture/logo.png')

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_mode(play_mode)


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    global image
    image.clip_draw(0, 0, 1600, 1000, 800, 500)
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
