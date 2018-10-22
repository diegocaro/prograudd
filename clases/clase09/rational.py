class Rational:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def __str__(self):
        return "Rational: {}/{}".format(self.n, self.d)

    def times(self, b):
        k = Rational(self.n * b.n, self.d * b.d)
        return k
    

r = Rational(10, 20)
m = Rational(1, 10)
print(r.times(m))
