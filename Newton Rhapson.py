#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    # Define la función para la cual quieres encontrar la raíz
    return x**3 - 5*x + 27

def derivative_func(x):
    # Define la derivada de la función
    return 3*x**2 - 5

def newton_raphson_method(x0, tol=1e-6, max_iter=100):

    x = x0
    num_iterations = 0
    while abs(func(x)) > tol and num_iterations < max_iter:
        x = x - func(x) / derivative_func(x)
        num_iterations += 1
    return x, num_iterations

# Definimos la aproximación inicial para buscar la raíz
x0 = -3

# Llamamos a la función del método de Newton-Raphson para encontrar la raíz
root, num_iterations = newton_raphson_method(x0)

print(f"Aproximación de la raíz: {root}")
print(f"Número de iteraciones: {num_iterations}")

# Generamos puntos para graficar la función en un rango cercano a la raíz
x_vals = np.linspace(root - 2, root + 2, 100)
y_vals = func(x_vals)

# Graficamos la función y la aproximación de la raíz
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='red')
plt.axvline(root, color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Gráfica de la función y aproximación de la raíz')
plt.show()