nombres = ['Diego', 'Francisca', 'Daniela', 'Leo']
notas = [4.1, 5.5, 6.8, 3.9]
cursos = ['progra', 'algebra', 'fisica', 'calculo']

def obtener_notas(estudiante, lista_nombres, lista_notas, lista_cursos):
    i = lista_nombres.index(estudiante)
    nota = lista_notas[i]
    curso = lista_cursos[i]
    return (curso, nota)

curso, nota = obtener_notas('Diego', nombres, notas, cursos)
print('Diego tiene un', nota, 'en', curso)