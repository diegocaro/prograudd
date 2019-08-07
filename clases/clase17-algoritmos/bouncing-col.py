import stddraw
from ballcol import Ball

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

balls = [
    Ball(.480, .860, .015, .023, .05, stddraw.BLACK),
    Ball(.380, .260, .030, .046, .05, stddraw.BLUE),
    Ball(.180, .260, .040, .026, .05, stddraw.GREEN),
    Ball(.880, .260, .040, .026, .1, stddraw.RED)
]

while True:
    # update velocity (balls collision)
    for i in range(len(balls)):
        for j in range(len(balls)):
            if i > j:
                balls[i].collision(balls[j])
    
    # update velocity (border collision)
    for b in balls:
        b.update()
    
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    for b in balls:
        b.draw()
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)