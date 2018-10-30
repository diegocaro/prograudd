import stddraw

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

radius = .05
rx = .480
ry = .860
vx = .015
vy = .023

radius2 = .05
rx2 = .480
ry2 = .860
vx2 = .030
vy2 = .063

radius3 = .05
rx3 = .480
ry3 = .860
vx3 = .01
vy3 = .013

while True:
    # bounce of wall according to elastic collition
    # update velocity
    if abs(rx + vx) + radius > 1.0:
        vx = -vx
    if abs(ry + vy) + radius > 1.0:
        vy = -vy
        
    if abs(rx2 + vx2) + radius2 > 1.0:
        vx2 = -vx2
    if abs(ry2 + vy2) + radius2 > 1.0:
        vy2 = -vy2
        
    if abs(rx3 + vx3) + radius3 > 1.0:
        vx3 = -vx3
    if abs(ry3 + vy3) + radius3 > 1.0:
        vy3 = -vy3

    # update position
    rx = rx + vx
    ry = ry + vy
    
    rx2 = rx2 + vx2
    ry2 = ry2 + vy2
    
    rx3 = rx3 + vx3
    ry3 = ry3 + vy3
    
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(rx, ry, radius)
    stddraw.filledCircle(rx2, ry2, radius2)
    stddraw.filledCircle(rx3, ry3, radius3)
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)