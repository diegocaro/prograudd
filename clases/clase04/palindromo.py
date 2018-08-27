palabra = 'anitalavalatina'
N = len(palabra)
palindromo = True
for i in range(N//2):
    if palabra[i] != palabra[N-i-1]:
        palindromo = False
        break #detiene ciclo for
print(palindromo)