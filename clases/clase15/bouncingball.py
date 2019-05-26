import stddraw

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

radius = .05

rx = .480
ry = .860
vx = .015
vy = .023

while True:
    # bounce of wall according to elastic collition
    # update velocity
    if abs(rx + vx) + radius > 1.0:
        vx = -vx
    if abs(ry + vy) + radius > 1.0:
        vy = -vy

    # update position
    rx = rx + vx
    ry = ry + vy
    
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(rx, ry, radius)
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)