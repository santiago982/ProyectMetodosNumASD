import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Método de Newton-Raphson
def newton_raphson(funcion, x0, tolerancia=1e-8, max_iter=100):
    # Símbolo de la variable x
    x = sp.Symbol('x')
    
    # Convertir la función de cadena a expresión simbólica
    f = sp.sympify(funcion)
    
    # Calcular la derivada de la función
    df = sp.diff(f, x)

    # Inicializar variables
    x_actual = x0
    iteracion = 0

    # Bucle principal del método de Newton-Raphson
    while abs(f.subs(x, x_actual)) > tolerancia and iteracion < max_iter:
        # Guardar el valor actual antes de la actualización
        x_actual_anterior = x_actual  

        # Actualizar x con la fórmula del método de Newton-Raphson
        x_actual = x_actual - f.subs(x, x_actual) / df.subs(x, x_actual)

        # Calcular el error absoluto
        error_absoluto = abs(x_actual - x_actual_anterior)

        # Incrementar el contador de iteraciones
        iteracion += 1

        # Imprimir información sobre la iteración actual
        print(f"Iteración {iteracion}: x = {x_actual}, |actual - anterior| = {error_absoluto}, g'(x) = {df.subs(x, x_actual)}")

    # Imprimir la raíz aproximada
    print(f"La raíz aproximada es: {x_actual}")

    return x_actual

# Entrada de datos
fx_input = input("Ingrese la función f(x): ")
x0 = float(input("Ingrese el valor inicial x0: "))
tolera = float(input("Ingrese la tolerancia para la aproximación de la raíz: "))

# Función para evaluar la expresión ingresada
def f(x): return eval(fx_input)

# Aplicar el método de Newton-Raphson
respuesta = newton_raphson(fx_input, x0, tolera)

# Función para evaluar la expresión con NumPy
def func_numpy(x): return eval(fx_input)

# Crear un array de valores de x para la gráfica
x_vals = np.linspace(x0 - 5, x0 + 5, 500)

# Calcular los valores de la función en los puntos de x_vals
y_vals = func_numpy(x_vals)

# Graficar la función y la raíz aproximada
plt.plot(x_vals, y_vals, label='f(x) = ' + fx_input)
plt.scatter(respuesta, func_numpy(respuesta), color='red',
            label='Raíz aproximada en x = ' + str(respuesta.round(5)))
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(respuesta, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Gráfica de la función y la raíz aproximada')
plt.show()


#pruebas 
# (1/3)*(x**3)+(2*x/3)-(4*x**2)+3
#  x0 = 0
