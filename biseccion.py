# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import re  # Importar el módulo de expresiones regulares para las validaciones

def get_user_input():
    # Solicitar la función al usuario
    expression = input("Ingrese la función (utilice 'x' como variable): ")
    
    # Validar la expresión utilizando una expresión regular
    if not re.match(r'^[0-9\(\)\*\+\-\./x ]+$', expression):
        raise ValueError("La expresión ingresada no es válida.")

    # Crear la función a partir de la expresión proporcionada
    func = lambda x: eval(expression)
    
    # Solicitar los extremos del intervalo al usuario
    a = float(input("Ingrese el extremo izquierdo del intervalo: "))
    b = float(input("Ingrese el extremo derecho del intervalo: "))
    
    return func, a, b
    return func, a, b

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    
     # Verificar si la función tiene signos opuestos en los extremos del intervalo
    while func(a) * func(b) >= 0:
        print("Error: La función debe tener signos opuestos en los extremos del intervalo.")
        
        # Solicitar los extremos del intervalo al usuario nuevamente
        while True:
            try:
                a = float(input("Ingrese el extremo izquierdo del intervalo: "))
                b = float(input("Ingrese el extremo derecho del intervalo: "))
                if b <= a:
                    raise ValueError("El extremo derecho debe ser mayor que el extremo izquierdo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, inténtelo nuevamente.")
     # Inicializar el contador de iteraciones
    num_iterations = 0
    
    
    # Realizar iteraciones hasta que se cumpla la condición de parada o se alcance el número máximo de iteraciones
    while (b - a) / 2 > tol and num_iterations < max_iter:
        # Calcular el punto medio del intervalo
        c = (a + b) / 2
        
        # Si la función en el punto medio es cero, se ha encontrado la raíz
        if func(c) == 0:
            break
        
        # Actualizar los extremos del intervalo basándose en el signo de la función en el punto medio
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
            
        # Incrementar el contador de iteraciones
        num_iterations += 1

     # Calcular la raíz como el punto medio del intervalo final
    root = (a + b) / 2
    
     # Retornar la raíz y el número de iteraciones realizadas
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

# ejercicios Pruebas
# x**2 - 4*x - 5
# [-2, 3]

#x**3 - 5*x + 27
#[-4, 1]

