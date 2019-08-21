year = int(input('Ingrese año: '))
if year%400 == 0 or (year%4 == 0 and year % 100 != 0):
    print('{} es bisiesto'.format(year))
else:
    print('{} NO es bisiesto'.format(year))