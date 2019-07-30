import stddraw
from picture import Picture

mariohead = Picture('mario_head.png')

stddraw.setCanvasSize(600, 600)
stddraw.setXscale(0, 600)
stddraw.setYscale(0, 600)

stddraw.picture(mariohead, 300, 400)
stddraw.show()
