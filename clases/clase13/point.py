class Point:
    """A 2d point in (x, y)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'is a point at ({}, {})'.format(self.x, self.y)

def main():
    p1 = Point(-1, -1)
    print('p1', p1)
    p2 = Point('hola', 'chao')
    print('p2', p2)

if __name__ == '__main__': main()