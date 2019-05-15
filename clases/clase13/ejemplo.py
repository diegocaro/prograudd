class Rational:
    """ Rational representa una fraccion de numerador n y
        denominador m.
    """
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
    def times(self, b):
        return self.simplify(Rational(self.n * b.n, self.m * b.m))
    
    def plus(self, b):
        return self.simplify(Rational(self.n*b.m+self.m*b.n, self.m*b.m))
    
    def simplify(self, b):
        a = max(b.n, b.m)
        c = min(b.n, b.m)
        if a % c == 0:
            return Rational(b.n//c, b.m//c)
        else:
            return b
        
    
    def __str__(self):
        return "{}/{}".format(self.n, self.m)
        
a = Rational(40, 20)
print(a)
b = Rational(29, 31)
print(b)
c = a.times(b)
print(c)
cs = c.simplify(c)
print(cs)
#d = a.plus(b)
#print(d)

