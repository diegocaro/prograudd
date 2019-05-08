def fibonacci(N):
    # precondicion
    assert N >= 0, "N must be non-negative" 
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

fibonacci(-2)