import stddraw
from math import sqrt

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
    
    def collision(self, p):
        d = sqrt(((self.rx+self.vx)-(p.rx+p.vx))**2 + ((self.ry+self.vy)-(p.ry+p.vy))**2)
        
        if d <= self.radius + p.radius:
            # collision detected!
            nx = self.rx-p.rx
            ny = self.ry-p.ry
            n = sqrt(nx*nx + ny*ny)
            un = (nx/n, ny/n) #normal
            ut = (-un[1], un[0]) #tangent
            
            # normal and tangent magnitude velocities for self
            v0n = un[0]*self.vx + un[1]*self.vy
            v0t = ut[0]*self.vx + ut[1]*self.vy
            
            # normal and tangent magnitude velocities for p
            v1n = un[0]*p.vx + un[1]*p.vy
            v1t = ut[0]*p.vx + ut[1]*p.vy
            
            v0n_v = (v1n * un[0], v1n * un[1])
            v0t_v = (v0t * ut[0], v0t * ut[1])
            
            v1n_v = (v0n * un[0], v0n * un[1])
            v1t_v = (v1t * ut[0], v1t * ut[1])
            
            # update final velocities
            self.vx = v0n_v[0] + v0t_v[0]
            self.vy = v0n_v[1] + v0t_v[1]
                
            p.vx = v1n_v[0] + v1t_v[0]
            p.vy = v1n_v[1] + v1t_v[1]
    
    def increase_speed(self, vx, vy):
        if self.vx + vx >= 0: self.vx += vx
        if self.vy + vy >= 0: self.vy += vy
        
    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.rx, self.ry, self.radius)