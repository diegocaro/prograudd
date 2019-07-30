import stddraw
from math import cos, sin

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

points_x = [-0.3, 0  ,  0.3]
points_y = [-0.3, 0.4, -0.3]

# post-condicion: número de puntos en x es la misma que en y
assert len(points_x) == len(points_y)

n = len(points_x)

# velocidad angular 
speed_rot = 0.1 # en radianes

while True:
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    
    # calculate rotations
    for i in range(n):
        newx = points_x[i]*cos(speed_rot) - points_y[i]*sin(speed_rot)
        newy = points_x[i]*sin(speed_rot) + points_y[i]*cos(speed_rot)
        points_x[i] = newx
        points_y[i] = newy
    
    # display triangle
    stddraw.polygon(points_x, points_y)
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)