import stddraw
from math import cos, sin

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

points = [(-0.3, -0.3), (0, 0.4), (0.3, -0.3)]
n = len(points)
angle = 0.1 # in radians

while True:
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    
    # calculate rotations
    for i in range(n):
        p = points[i]
        newx = p[0]*cos(angle) - p[1]*sin(angle)
        newy = p[0]*sin(angle) + p[1]*cos(angle)
        points[i] = (newx, newy)
    
    # display triangle
    for i in range(n):
        stddraw.line(points[i][0],points[i][1], points[(i+1)%n][0], points[(i+1)%n][1])
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)