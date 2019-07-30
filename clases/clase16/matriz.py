class Matrix:
    """Create a matrix of n rows and m columns."""
    def __init__(self, n, m):
        self.cols = m
        self.rows = n
        self.m = []
        for i in range(self.rows):
            self.m.append([0]*self.cols)
        
    def __str__(self):
        s = '\n'
        for i in range(len(self.m)):
            s += '[ '
            for j in range(len(self.m[i])):
                s += str(self.m[i][j]) + ' '
            s += ']\n'
        return s
        
    
    def get(self, row, col):
        assert row < self.rows
        assert col < self.cols
        return self.m[row][col]
    
    def set(self, row, col, value):
        assert row < self.rows
        assert col < self.cols
        self.m[row][col] = value
    
    def id_elem(self):
        s = '\n'
        for row in self.m:
            s += str(id(row))
            s += ' -> [ '
            for elem in row: s += str(id(elem)) + ' '
            s += ']\n'
        return s
        
m = Matrix(4, 5)
print('type(m):', type(m))
print('m:', m)
m.set(0, 1, 99)
print('m:', m)

print(id(m))
print(m.id_elem())