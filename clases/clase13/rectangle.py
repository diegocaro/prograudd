class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        
    def area(self):
        return self.w * self.h

def main():
    rA = Rectangle(3, 4)
    rB = Rectangle(9, 8)
    print('area rA:', rA.area())
    print('area rB:', rB.area())
    
if __name__ == '__main__': main()