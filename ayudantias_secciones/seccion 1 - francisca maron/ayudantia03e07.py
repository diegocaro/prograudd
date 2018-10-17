s = int(input('s: '))
n = input('n: ')

d = int(str(n)[0])
print('imprimiendo dígito:', d)
print('tipo de dato variable d:', type(d))

# imprimir linea tipo 1, los que tienen raya arriba
if d in [1,4]:
    #print(' {} '.format(' '*s))
    print(' ', end='')
    for i in range(s):
        print(' ', end='')
    print(' ')
else:
    print(' {} '.format('-'*s))

# imprimir tipo 2: |   ,    |, |  |
espacios = ' '*s
for i in range(s):
    if d in [5,6]:
        print('|'+espacios+' ')
    elif d in [1,2,3,7]:
        print(' '+espacios+'|')
    else:
        print('|' + ' '*s + '|')
    
# imprimir tipo3:    , -- , 
if d in [0, 1, 7]:
    print(' {} '.format(' '*s))
else:
    print(' {} '.format('-'*s))
    
# imprimir tipo 2: |   ,    |, |  |
for i in range(s):
    if d in [2]:
        print('|{} '.format(' '*s))
    elif d in [1,3,7,4,5,9]:
        print(' {}|'.format(' '*s))
    else:
        print('|{}|'.format(' '*s))
    
# imprimir tipo 4:     , -- 
if d in [1, 4, 7,]:
    print(' {} '.format(' '*s))
else:
    print(' {} '.format('-'*s))
