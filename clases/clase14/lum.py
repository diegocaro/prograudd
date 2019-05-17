from mycolor import Color
def readint(): return int(input())

def lum(c):
    red   = c.red()
    green = c.green()
    blue  = c.blue()
    return (.299 * red) + (.587 * green) + (.114 * blue)

def compatible(a, b):
    return abs(lum(a) - lum(b)) > 128

def grayscale(c):
    y = round(lum(c))
    return Color(y, y, y)

if __name__ == '__main__':
    r = readint()
    g = readint()
    b = readint()
    c = Color(r, g, b)
    print(round(lum(c)))