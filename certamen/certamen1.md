<img src="figuras/logo_UDD_Facultad_Ingenieria.jpg" style="float: center; height: 60px;">

<h4 align="center">Tecnologías de la Información 2</h4>
<h4 align="center">Certamen 1</h4>
<h5 align="center">10 de septiembre de 2018</h5>

---

**Instrucciones** 

- Lea atentamente el enunciado de cada uno de los problemas. 
- Escriba con letra legible y de tamano adecuado
- Elija **SÓLO TRES** de los 4 problemas del certamen.
- **Para demarcar la indentación utilice TRES cuadrados del cuadernillo.**

---

##### (2 puntos) Problema 1

Solicitando un número real $z$ que cumpla $|z|<1$ y un número $n$ entero, calcule el valor de la serie geométrica $$ \displaystyle S = \sum_{k=1}^{n} z^k  $$ utilizando un ciclo `for`. Adicionalmente, escriba en su código una verificación de que el resultado de la sumatoria coincide con el valor de la expresión $$ \displaystyle \dfrac{1-z^n}{1-z}. $$

<div style="page-break-after: always;"></div>

##### (2 puntos) Problema 2

El objetivo de este problema consiste en estimar el valor del número irracional $\pi$ usando números (pseudo) aleatorios. Consideremos un cículo de radio $1/2$ inscrito en un cuadrado de lado $1$. Suponga que tenemos a nuestra disposición una funcion `RANDOM2D` que genera un par ordenado de números aleatorios $(x,y)$, cada uno con una distribución homogénea en el intervalo $[-0.5,0.5]$.

<img src="pi_montecarlo.png" width=100>

Podemos notar que el cociente entre el número $n$ de pares ordenados que caen dentro del círculo inscrito y el número de pares ordenados totales $N$ converge al cociente entre el área del círculo y la del cuadrado cuando $N$ es grande, es decir 

$$ \displaystyle \lim_{N\rightarrow\infty} \dfrac{n}{N} = \dfrac{\pi\left(\frac{1}{2}\right)^2}{1^2}=\dfrac{\pi}{4}, $$

lo que nos permite estimar el valor de $\pi$ mediante números aleatorios. Lo anterior queda descrito por el siguiente diagrama de flujo:

<img src="calculo_pi.png" width=400>



Traduzca el diagrama de flujo anterior en un código `Python`

_Hint:_ dentro del programa, puede llamar a la función `RANDOM2D` usando la línea `x, y = RANDOM2D()`.

<div style="page-break-after: always;"></div>

##### (2 puntos) Problema 3

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
|      |         |      |         |      |
|      |         |      |         |      |
|      |         |      |         |      |

<div style="page-break-after: always;"></div>

##### (2 puntos) Problema 4

La empresa Computer S.A. está planificando un aumento de sueldo para sus 3 empleados. Escriba un programa que calcule e imprima el nuevo sueldo para cada uno de los tres empleados, de acuerdo a las siguientes reglas:

| Salario actual                  | Porcentaje de aumento |
| ------------------------------- | --------------------- |
| Menor o igual a $900.000        | 20% de aumento        |
| Entre 900.001 y 1.300.000   | 10% de aumento        |
| Entre 1.300.001 y 1.800.000 | 5% de aumento         |
| Mayor a 1.800.001             | 2% de aumento         |

Por ejemplo:

| Entrada / Sueldo actual | Salida / Sueldo futuro |
|-------------------------|------------------------|
| 400000                  | 480000                 |
| 1000000                 | 1100000                |
| 2000000                 | 2040000                |

