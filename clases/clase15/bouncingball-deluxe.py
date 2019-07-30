import stddraw
from balldeluxe import Ball

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

balls = [
    Ball(.480, .860, .015, .023, .05, stddraw.RED),
    Ball(.480, .860, .030, .046, .1, stddraw.BLUE),
    Ball(.180, .260, .040, .026, .2, stddraw.GREEN)
]

while True:
    # get keystrokes
    if stddraw.hasNextKeyTyped():
        k = stddraw.nextKeyTyped()
        if k == stddraw.K_UP: 
            for b in balls: b.increase_speed(0.1, 0.1)
        elif k == stddraw.K_DOWN:
            for b in balls: b.increase_speed(-0.1, -0.1)
    
    # update velocity
    for b in balls: b.update()
    
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    for b in balls: b.draw()
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)