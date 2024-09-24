from pico2d import *
import math

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 중앙에서 이동
x = 400
while (400 <= x < 600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x += 2
    delay(0.01)

# 위로 90도 이동
y = 90
while(90 <= y < 300):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y += 2
    delay(0.01)

while (x > 400 or y > 90): 
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    
    if x > 400:
        x -= 2
    if y > 90:
        y -= 2
    
    delay(0.01)

start_x = 400
start_y = 30

center_x = start_x
center_y = start_y + 200

radius = 200

angle = 270 

while (angle < 360 * 5 + 270): 
    clear_canvas_now()
    grass.draw_now(400, 30)
    
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    character.draw_now(x, y)
    
    angle += 2  
    delay(0.01)


close_canvas()
