""" 
    Introduce el número de ecuaciones: 4
    Introduce la ecuación 1: 4 -1 0 0 1
    Introduce el valor inicial para x_1: 0
    Introduce la ecuación 2: -1 4 -1 0 1
    Introduce el valor inicial para x_2: 0
    Introduce la ecuación 3: 0 -1 4 -1 1
    Introduce el valor inicial para x_3: 0
    Introduce la ecuación 4: 0 0 -1 4 1
    Introduce el valor inicial para x_4: 0
    Introduce la tolerancia: 0.01
"""

import numpy as np


def metodo_jacobi(matriz_ecuaciones, val_indep_ecuaciones, x_inicial, tolerancia, N=100):
    D = np.diag(np.diag(matriz_ecuaciones))
    LU = matriz_ecuaciones - D
    x = x_inicial
    for i in range(N):
        D_inv = np.diag(1 / np.diag(D))
        x_nuevo = np.dot(D_inv, val_indep_ecuaciones - np.dot(LU, x))
        diff_norm = np.linalg.norm(x_nuevo - x)
        if diff_norm < tolerancia:
            return x_nuevo
        x = x_nuevo
        print(
            f"Iteración {i+1}: x = {np.round(x, 5)}")
    return x


n = int(input("Introduce el número de ecuaciones: "))
matriz_ecuaciones = np.zeros((n, n))
val_indep_ecuaciones = np.zeros(n)
x_inicial = np.zeros(n)

for i in range(n):
    ec = list(map(float, input(f"Introduce la ecuación {i+1}: ").split(' ')))
    matriz_ecuaciones[i] = ec[:-1]
    val_indep_ecuaciones[i] = ec[-1]
    x_inicial[i] = float(input(f"Introduce el valor inicial para x_{i+1}: "))

tolerancia = float(input("Introduce la tolerancia: "))

x = metodo_jacobi(matriz_ecuaciones, val_indep_ecuaciones,
                  x_inicial, tolerancia)
print("Solución: ", np.round(x, 5))
