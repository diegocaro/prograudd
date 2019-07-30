import stddraw
from playthatnote import tone

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
            tone(220*(1/self.radius), 0.04)
        if abs(self.ry + self.vy) + self.radius > 1.0:
            self.vy = -self.vy
            tone(220*(1/self.radius), 0.04)
        
        self.rx = self.rx + self.vx
        self.ry = self.ry + self.vy
    
    def increase_speed(self, vx, vy):
        if self.vx + vx >= 0: self.vx += vx
        if self.vy + vy >= 0: self.vy += vy
        
    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.rx, self.ry, self.radius)