class Point:
    """A 2d point in (x, y)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distX(self, p):  return abs(self.x - p.x)
    def distY(self, p):  return abs(self.y - p.y)

class Rectangle:
    """A rectangle with the lower-left corner in
    p1 and upper-right corner in p2."""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def area(self):
        return self.p1.distX(self.p2) * self.p1.distY(self.p2)

def main():
    p1 = Point(-1, -1)
    p2 = Point(1, 1)
    r = Rectangle(p1, p2)
    print('area de r:', r.area())

if __name__ == '__main__': main()