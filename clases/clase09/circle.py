from math import sqrt

class Circle:
    """Creates a circle at (px, py) with radio r."""
    def __init__(self, px, py, r):
        self.x = px
        self.y = py
        self.radio = r
    
    def dist(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def __str__(self):
        return "Circle at ({}, {}) with radio {}." \
                .format(self.x, self.y, self.radio)
                
c = Circle(10, 10, 5)
print(c.dist())
help(Circle)