notas = {'Diego'    : ('prograudd',4.1)
        ,'Francisca': ('algebra'  ,5.5)
        ,'Daniela'  : ('fisica'   ,6.8)
        ,'Leo'      : ('prograudd',3.9)}

def obtener_notas(estudiante, dict_notas):
    curso, nota = dict_notas[estudiante]
    return (curso, nota)
    
curso, nota = obtener_notas('Diego', notas)
print('Diego tiene un', nota, 'en', curso)



    