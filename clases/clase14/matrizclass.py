class Matrix:
    """Create a matrix of n rows and m columns."""
    def __init__(self, n, m):
        self.cols = m
        self.rows = n
        self.m = [ [0]*m ]*n
        
    def __str__(self):
        s = '\n'
        for i in range(len(self.m)):
            s += '[ '
            for j in range(len(self.m[i])):
                s += str(self.m[i][j]) + ' '
            s += ']\n'
        return s
        
m = Matrix(4, 5)
print('type(m):', type(m))
print('m:', m)
m[1] = [99]
print('m:', m)