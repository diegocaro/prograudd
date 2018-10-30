import stddraw

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

class Ball:
    def __init__(self, rx, ry, vx, vy, radius, color):
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        
    def update(self):
        """
        Bounce of wall according to elastic collition and
        update velocity.
        """
        if abs(self.rx + self.vx) + self.radius > 1.0:
            self.vx = -self.vx
        if abs(self.ry + self.vy) + self.radius > 1.0:
            self.vy = -self.vy
        
        self.rx = self.rx + self.vx
        self.ry = self.ry + self.vy

    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.rx, self.ry, self.radius)

ball = Ball(.480, .860, .015, .023, .05, stddraw.BLACK)

while True:
    # update velocity
    ball.update()
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    ball.draw()
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)