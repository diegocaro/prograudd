def leerpais(linea):
    return linea

f = open('gini_by_country.csv','r')
for l in f:
    print(leerpais(l))
f.close()