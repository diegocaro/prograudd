nombre = 'hola.py'
partes = []
for i in range(len(nombre)):
    if nombre[i] == '.':
        n = nombre[0:i]
        e = nombre[i+1:]
        partes.append(n)
        partes.append(e)
        break
print('nombre archivo:', partes[0])
print('extension archivo:', partes[1])