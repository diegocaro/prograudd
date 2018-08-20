# sqrt.py
from sys import argv
EPS = 1e-15
c = float(argv[1])
t = c
while abs(t - c/t) > t*EPS:
    t = (c/t  + t)/2.0
print(t)
