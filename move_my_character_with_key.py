from pico2d import *


open_canvas(800,600)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
dir_x, dir_y = 0, 0

running = True

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1

while running:
    clear_canvas()
    grass.draw(400, 30)

close_canvas()