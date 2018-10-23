import stddraw
from color import Color

def readint(): return int(input())

r1 = readint()
g1 = readint()
b1 = readint()
c1 = Color(r1, g1, b1)

r2 = readint()
g2 = readint()
b2 = readint()
c2 = Color(r2, g2, b2)

stddraw.setCanvasSize(512, 256)
stddraw.setYscale(.25, .75)

stddraw.setPenColor(c1)
stddraw.filledSquare(.25, .5, .2)

stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .5, .1)

stddraw.setPenColor(c2)
stddraw.filledSquare(.75, .5, .2)

stddraw.setPenColor(c1)
stddraw.filledSquare(.75, .5, .1)

stddraw.show()
