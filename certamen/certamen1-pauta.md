#### (2 puntos) Problema 1

Solicitando un número real $z$ que cumpla $|z|<1$ y un número $n$ entero, calcule el valor de la serie geométrica $$ \displaystyle S = \sum_{k=1}^{n} z^k  $$ utilizando un ciclo `for`. Adicionalmente, escriba en su código una verificación de que el resultado de la sumatoria coincide con el valor de la expresión $$ \displaystyle \dfrac{1-z^n}{1-z}. $$

**Respuesta:**

```python
z = float(input("Ingrese z: "))
n = int(input("Ingrese n: "))
S = 0
if abs(z)<1:
    for k in range(1, n+1):
        S = S + z**k
else:
    print("|z| debe ser menor a 1")

R = (1-z**n)/(1-z)
if R/S == 1:
    print("La serie S es igual al resultado R")
else:
    print("La serie S es diferente al resultado R")
```

#### (2 puntos) Problema 2

El objetivo de este problema consiste en estimar el valor del número irracional $\pi$ usando números (pseudo) aleatorios. Consideremos un cículo de radio $1/2$ inscrito en un cuadrado de lado $1$. Suponga que tenemos a nuestra disposición una funcion `RANDOM2D` que genera un par ordenado de números aleatorios $(x,y)$, cada uno con una distribución homogénea en el intervalo $[-0.5,0.5]$.

Podemos notar que el cociente entre el número $n$ de pares ordenados que caen dentro del círculo inscrito y el número de pares ordenados totales $N$ converge al cociente entre el área del círculo y la del cuadrado cuando $N$ es grande, es decir 

$$ \displaystyle \lim_{N\rightarrow\infty} \dfrac{n}{N} = \dfrac{\pi\left(\frac{1}{2}\right)^2}{1^2}=\dfrac{\pi}{4}, $$

lo que nos permite estimar el valor de $\pi$ mediante números aleatorios. Lo anterior queda descrito por el siguiente diagrama de flujo:

Traduzca el diagrama de flujo anterior en un código `Python`

_Hint:_ dentro del programa, puede llamar a la función `RANDOM2D` usando la línea `x, y = RANDOM2D()`.

```python
N = int(input("Ingrese N: "))
i=0
n=0
x, y = RAND2D()
while i<N:
    if x**2+y**2 < 1/4:
        n = n+1
    i=i+1
    x, y = RAND2D()
pi = 4*n/N
print("Pi es aproximadamente ", pi)

```


#### (2 puntos) Problema 3

Lea atentamente el siguiente código e indique cuáles son los valores de las variables mostradas en la tabla, a medida de que se ejecuta el ciclo while.

``` python
L = [1, 1]  
n = 5  
i = 2  
R = L.copy()  
while i < n:  
    k = L[i-1] + L[i-2]  
    L.append(k)  
    if k % 2 == 1:  
        R.append(k)  
    i  = i + 1  
print(len(R)) 
```

Por ejemplo, la segunda fila de la tabla muestra el contenido de las variables justo antes de ejecutar el ciclo while (antes de la línea 5 del código).

| `i`  |   `L`   | `k`  |   `R`   | `n`  |
| :--: | :-----: | :--: | :-----: | :--: |
| `2`  | `[1,1]` |  --  | `[1,1]` | `5`  |
|  |  |     |         |    |
|  |  |     |         |    |
|  |  |     |         |    |


**Respuesta:** Si desarrolló una traza línea por línea, también se considera como respuesta correcta.

| `i`  |   `L`   | `k`  |   `R`   | `n`  |
| :--: | :-----: | :--: | :-----: | :--: |
| `2`  | `[1,1]` |  --  | `[1,1]` | `5`  |
| `3`  |  `[1,1,2]` | `2`     | `[1,1]`        | `5`     |
|  `4` | `[1,1,2,3]` | `3`     | `[1,1,3]`        |  `5`    |
|  `5` | `[1,1,2,3,5]` | `5` | `[1,1,3,5]`    |  `5`    |

```python
L = [1, 1]
n = 5
i = 2
R = L.copy()
#print('i:', i, 'L:', L, 'k:', '-', 'R:', R, 'n:', n)
while i < n:
    k = L[i-1] + L[i-2]
    L.append(k)
    if k % 2 == 1:
        R.append(k)
    i = i + 1
    #print('i:', i, 'L:', L, 'k:', k, 'R:', R, 'n:', n)
print(len(R))

```


##### (2 puntos) Problema 4

La empresa Computer S.A. está planificando un aumento de sueldo para sus 3 empleados. Escriba un programa que calcule e imprima el nuevo sueldo para cada uno de los tres empleados, de acuerdo a las siguientes reglas:

| Salario actual                  | Porcentaje de aumento |
| ------------------------------- | --------------------- |
| Menor o igual a \$900.000        | 20% de aumento        |
| Entre \$900.001 y \$1.300.000   | 10% de aumento        |
| Entre \$1.300.001 y \$1.800.000 | 5% de aumento         |
| Mayor a \$1.800.001             | 2% de aumento         |

Por ejemplo:

| Entrada / Sueldo actual | Salida / Sueldo futuro |
|-------------------------|------------------------|
| 400000                  | 480000                 |
| 1000000                 | 1100000                |
| 2000000                 | 2040000                |

Respuesta 1: usando ciclos

```python
for i in range(3):
    s = int(input())
    if s <= 900000: print(int(s*1.2))
    elif s > 900000 and s <= 1300000: print(int(s*1.1))
    elif s > 1300000 and s <= 1800000: print(int(s*1.05))
    else: print(int(s*1.02))
```

Respuesta 2: no usar ciclos

```python
s = int(input())
if s <= 900000: print(int(s*1.2))
elif s > 900000 and s <= 1300000: print(int(s*1.1))
elif s > 1300000 and s <= 1800000: print(int(s*1.05))
else: print(int(s*1.02))

s = int(input())
if s <= 900000: print(int(s*1.2))
elif s > 900000 and s <= 1300000: print(int(s*1.1))
elif s > 1300000 and s <= 1800000: print(int(s*1.05))
else: print(int(s*1.02))

s = int(input())
if s <= 900000: print(int(s*1.2))
elif s > 900000 and s <= 1300000: print(int(s*1.1))
elif s > 1300000 and s <= 1800000: print(int(s*1.05))
else: print(int(s*1.02))
```
