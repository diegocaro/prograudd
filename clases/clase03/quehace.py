a = int(input())
b = int(input())
if b < a:
    t = b
    b = a
    a = t
print(a)
print(b)