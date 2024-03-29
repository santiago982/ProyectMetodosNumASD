import sympy as sp
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
    if n == 2:
        h = (b - a) / 6
        valores = np.linspace(a, b, n+1)
        resultado = h * \
            (funcion(valores[0]) + 4*funcion(valores[1]) + funcion(valores[2]))
        print(f"El resultado del método es = {round(resultado, 5)}")
        return resultado
    elif n > 2 and n % 2 == 0:
        h = (b - a) / (3 * n)
        valores = np.linspace(a, b, n+1)
        sumatoria_xi = funcion(valores[0]) + funcion(valores[-1])
        sumatoria_mi = sum([2 * funcion(valores[i]) for i in range(1, n, 2)])
        sumatoria_mi += sum([4 * funcion(valores[i]) for i in range(2, n-1, 2)])
        resultado = h * (sumatoria_xi + sumatoria_mi)
        print(f"El resultado del método es = {round(resultado, 5)}")
        return resultado
    else:
        print("Para el caso n > 2, n debe ser un número par.")
        return None
