import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def convertir_a_funcion(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr), "numpy")

def calcular_error_simpson(funcion, a, b, n):
    x = sp.Symbol('x')
    cuarta_derivada = sp.diff(funcion, x, 4)
    K = max([cuarta_derivada.subs(x, val) for val in np.linspace(a, b, 1000)])
    error = (K * (b - a)**5) / (180 * n**4)
    print(f"Error de aproximación: {error:.6f}")
    return error

def simpson(funcion, a, b, n):
    if (n == 2):
        h = (b - a) / 6
        valores = np.linspace(a, b, n+1)
        resultado = h * \
            (funcion(valores[0]) + 4*funcion(valores[1]) + funcion(valores[2]))
        print(f"El resultado del método es = {round(resultado, 5)}")

    if (n > 2 & n % 2 == 0):
        h = (b - a) / (6 * n)
        valores = np.linspace(a, b, n+1)
        sumatoria_xi = 0
        sumatoria_mi = 0
        valores_xi = []
        valores_mi = []

        for i in range(0, n+1):
            valores_xi.append(funcion(valores[i]))
            sumatoria_xi += funcion(valores[i])

        for i in range(0, n):
            valores_mi.append((valores_xi[i] + valores_xi[i+1])/2)
            sumatoria_mi += (valores_xi[i] + valores_xi[i+1])/2
        resultado = h * (valores_xi[0] + 4*sumatoria_mi +
                         2 * (sumatoria_mi + valores_xi[-1]))
        print(f"El resultado del método es = {round(resultado, 5)}")

    return resultado, valores_mi

n = int(input("Introduce el número de n: "))
funcionEntrante = input("Ingrese la función: f(x) ")
funcionConvertida = convertir_a_funcion(funcionEntrante)
a = float(input("Introduce a: "))
b = float(input("Introduce b: "))

resultado, valores_mi = simpson(funcionConvertida, a, b, n)
error_aproximado = calcular_error_simpson(funcionEntrante, a, b, n)

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

plt.show()
