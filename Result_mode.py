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
from sonic import Sonic, SonicWin


def init():
    hide_cursor()

    global image
    image = load_image('texture/win.png')

    if server.player1.life > server.player2.life:
        server.player1 = Kirby(800, 500)
        server.player1.state_machine.cur_state = kirby.KirbyWin
        server.player1.image = load_image('texture/kirby_win.png')
        game_world.add_object(server.player1, 2)
    elif server.player1.life < server.player2.life:
        server.player2 = Sonic(800, 500)
        server.player2.state_machine.cur_state = SonicWin
        server.player2.image = load_image('texture/sonic_win.png')
        game_world.add_object(server.player2, 2)


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
