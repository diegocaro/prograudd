def creatematrix(n, m):
    """Return a matrix of n rows and m columns."""
    return [ [0]*m ]*n
    
def strmatrix(m):
    s = '\n'
    for i in range(len(m)):
        s += '[ '
        for j in range(len(m[i])):
            s += str(m[i][j]) + ' '
        s += ']\n'
    return s

m = creatematrix(4, 5)
print('type(m):', type(m))
print('m:', strmatrix(m))
m[1] = [99]
print('m:', strmatrix(m))