from random import shuffle

archivo = 'equipos.csv'
equipos = []
alerta = []
with open(archivo, 'rt') as f:
    for i, linea in enumerate(f):
        # nos saltamos la primera linea
        if i == 0: continue
        campos = linea.split(',')
        # campo[4] indica si entregó informe
        # campo[5] indica si entregó código
        if campos[4] == '1' or campos[5]=='1':
            if len(campos[2]) > 0:
                equipos.append(' y '.join(campos[1:3]))
            else:
                equipos.append(campos[1])
        else:
            alerta.append(campos[1:3])

print('Un total de', len(equipos), 'equipos entregaron la tarea.')

# crea una permutación aleatoria de los equipos
shuffle(equipos)

for i in range(len(equipos)//2):
    if i == len(equipos)//2-1 and len(equipos)%2 == 1:
        print(str(i+1)+'.', equipos[2*i], 'revisa con', equipos[2*i+1], 'y además', equipos[2*i+2])
    else:
        print(str(i+1)+'.', equipos[2*i], 'revisa con', equipos[2*i+1])



for a in alerta:
    if len(a) > 1:
        print('Alerta:', a[0], 'y', a[1], 'deben conversar con el profesor.')
    else:
        print('Alerta:', a[0], 'debe conversar con el profesor.')

