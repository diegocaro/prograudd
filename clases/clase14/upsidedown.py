import sys
import stddraw
import luminance
from picture import Picture

source = Picture(sys.argv[1])
target = Picture(source.width(), source.height())
for col in range(source.width()):
    for row in range(source.height()):
        target.set(col, source.height()-row-1, source.get(col, row))

stddraw.setCanvasSize(target.width(), target.height())
stddraw.picture(target)
stddraw.show()
