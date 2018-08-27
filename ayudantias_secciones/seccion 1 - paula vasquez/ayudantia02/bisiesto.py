# Un año es bisiesto si cumple los siguientes criterios:
# 1. Es divisible entre 4.
# 2. Si termina en 00, es divisible entre 400 (2000 y 2400 sí son bisiestos. 2100, 2200 y 2300 no lo son).
# Extraído desde https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto

year = int(input('ingrese el año: '))
if year % 4 == 0 and (year%100 != 0 or year%400==0):
    print(year, 'es bisiesto')
else:
    print(year, 'no es bisiesto')