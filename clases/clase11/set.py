A = {1, 2, 2, 3}
print('A:', A)

print('2 in A?:', 2 in A)

A.add(99)
print('A.add(99):', A)

A.remove(2)
print('A.remove(2):', A)

B = set([1, 2, 3, 'hola'])
print('B:', B)

print('A ∩ B:', A.intersection(B))
print('A ∩ B:', A & B)

print('A ∪ B:', A.union(B))
print('A ∪ B:', A | B)

print('A - B:', A.difference(B))
print('A - B:', A - B)