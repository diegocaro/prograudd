import stddraw
import sys
from picture import Picture

fileName = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])

source = Picture(fileName)
target = Picture(w, h)

for tCol in range(w):
    for tRow in range(h):
        sCol = tCol * source.width() // w
        sRow = tRow * source.height() // h
        target.set(tCol, tRow, source.get(sCol, sRow))

stddraw.setCanvasSize(w, h)
stddraw.picture(target)
stddraw.show()
