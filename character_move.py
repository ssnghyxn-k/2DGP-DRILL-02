from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    r = 300
    cx = 800 // 2 
    cy = 600 // 2

    for d in range (0,360):
        x = r * math.cos(math.radians(d))
        y = r * math.sin(math.radians(d))

        clear_canvas_now()
        character.draw_now(400,300)
        delay(0.01)

    pass

def run_top():
    pass

def run_right():
    pass

def run_bottom():
    pass

def run_left():
    pass


def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()


while True:
    run_circle
    break

