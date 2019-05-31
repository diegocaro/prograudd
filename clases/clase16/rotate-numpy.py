import stddraw
import numpy as np

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

points = np.array([[-0.3, -0.3], [0, 0.3], [0.3, -0.3]])
n = points.shape[0] #numero de filas en matriz point

# velocidad angular 
speed_rot = 0.1 # en radianes
matrix_rot = np.array([ [np.cos(speed_rot),-np.sin(speed_rot)], 
                        [np.sin(speed_rot), np.cos(speed_rot)] ])

while True:
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    
    # calculate rotations
    for i in range(n):
        points[i] = matrix_rot.dot(points[i])
    # display triangle
    stddraw.polygon(points[:,0], points[:,1])
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)