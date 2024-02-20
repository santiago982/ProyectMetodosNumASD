import sympy as sp                 #para convertir una expresión simbólica en una función numérica
import matplotlib.pyplot as plt  #libreria para Graficar
import numpy as np               # para operaciones numericas y manipulacion de arreglos

def convertir_a_funcion(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr), "numpy")

def calcular_error_simpson(funcion, a, b, n):
    x = sp.Symbol('x')   # Se define x 
    cuarta_derivada = sp.diff(funcion, x, 4)
    K = max([cuarta_derivada.subs(x, val) for val in np.linspace(a, b, 1000)])
    error = (K * (b - a)**5) / (180 * n**4)
    print(f"Error de aproximación: {error:.6f}")
    return error

def simpson(funcion, a, b, n):
    if n == 2:
        h = (b - a) / 6  #Calcula el ancho de cada subintervalo.
        valores = np.linspace(a, b, n+1)  # espaciado en puentos intermedios
        resultado = h * \
            (funcion(valores[0]) + 4*funcion(valores[1]) + funcion(valores[2]))# Calcula la aproximación de la integral utilizando la fórmula de Simpson simple. Multiplica el ancho del subintervalo por la suma ponderada de los  valores de la función en los extremos y el punto medio del intervalo.
        print(f"El resultado del método es = {round(resultado, 5)}")
        return resultado
# si es mas de 2 usa la formula 2 o caso2
    elif n > 2 and n % 2 == 0:
        h = (b - a) / (3 * n) # Calcula el ancho de cada subintervalo para el método compuesto.
        valores = np.linspace(a, b, n+1) # Calcula el ancho de cada subintervalo para el método compuesto.
        sumatoria_xi = funcion(valores[0]) + funcion(valores[-1])  # Calcula la suma de los valores de la función en los extremos del intervalo.
        sumatoria_mi = sum([2 * funcion(valores[i]) for i in range(1, n, 2)]) #  Calcula la suma de los valores de la función multiplicados por 2 en los puntos intermedios impares.
        sumatoria_mi += sum([4 * funcion(valores[i]) for i in range(2, n-1, 2)])  # Suma los valores de la función multiplicados por 4 en los puntos intermedios pares.
        resultado = h * (sumatoria_xi + sumatoria_mi) #  Calcula la aproximación de la integral utilizando la fórmula compuesta del método de Simpson.
        print(f"El resultado del método es = {round(resultado, 5)}")
        return resultado # regresa resultado

    else:
        print("Para el caso n > 2, n debe ser un número par.")
        return None

# Solicitar al usuario la función hasta que sea válida
funcionEntrante = None
while funcionEntrante is None:
    funcionEntrante = input("Ingrese la función (por ejemplo, sqrt(5 + x**3)): ")
    try:
        funcionConvertida = convertir_a_funcion(funcionEntrante)
    except:
        print("La función ingresada no es válida. Inténtelo de nuevo.")
        funcionEntrante = None

# Solicitar al usuario el número de n hasta que sea un número par
n = None
while n is None or n % 2 != 0:
    try:
        n = int(input("Introduce el número de n (debe ser un número par): "))
    except ValueError:
        print("Por favor, ingrese un número entero.")

a = float(input("Introduce a: "))
b = float(input("Introduce b: "))

resultado = simpson(funcionConvertida, a, b, n)

if resultado is not None:
    error_aproximado = calcular_error_simpson(sp.sympify(funcionEntrante), a, b, n)

    x_vals = np.linspace(a, b, 400)
    y_vals = funcionConvertida(x_vals)

    fig, ax = plt.subplots()

    ax.plot(x_vals, y_vals, 'b', linewidth=2, label='Función')

    x_area = np.linspace(a, b, n+1)
    y_area = funcionConvertida(x_area)

    ax.fill_between(x_area, y_area, alpha=0.2, color='green',
                    label='Área bajo la curva')

    for xi in x_area[1:-1]:
        ax.axvline(xi, color='red', linestyle='--', linewidth=1)

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(
        f'Gráfica de la función y Área bajo la curva con {n} divisiones y líneas')

    ax.legend()

    plt.show()# pintar grafico area bajo la curva
