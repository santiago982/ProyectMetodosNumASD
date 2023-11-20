# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def get_user_input():
    # Solicitar la función al usuario
    expression = input("Ingrese la función (utilice 'x' como variable): ")
    # Crear la función a partir de la expresión proporcionada
    func = lambda x: eval(expression)
    
    # Solicitar los extremos del intervalo al usuario
    a = float(input("Ingrese el extremo izquierdo del intervalo: "))
    b = float(input("Ingrese el extremo derecho del intervalo: "))
    
    return func, a, b

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")

    num_iterations = 0
    while (b - a) / 2 > tol and num_iterations < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        num_iterations += 1

    root = (a + b) / 2
    return root, num_iterations

def plot_function_and_root(func, a, b, root):
    x_vals = np.linspace(a, b, 100)
    y_vals = func(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color="red")
    plt.axvline(0, color="green")
    plt.scatter(root, func(root), color='blue', label='Root')
    plt.xlabel('eje x')
    plt.ylabel('eje y')
    plt.legend()
    plt.grid(True)
    plt.title('Bisección')
    plt.show()

def main():
    func, a, b = get_user_input()
    root, num_iterations = bisection_method(func, a, b)

    print(f"Aproximación de la raíz: {root}")
    print(f"Número de iteraciones: {num_iterations}")

    plot_function_and_root(func, a, b, root)

if __name__ == "__main__":
    main()

