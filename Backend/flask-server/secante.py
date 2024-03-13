import sympy as sp
import numpy as np

def convertir_a_funcion(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr))

def secante(fC, x0, x1, tolera=1e-6, max_iter=100):
    x = [x0, x1]
    y = [fC(x0), fC(x1)]
    it = 0
    while it < max_iter:
        x_next = x[-1] - y[-1] * (x[-1] - x[-2]) / (y[-1] - y[-2])
        x.append(x_next)
        y.append(fC(x_next))

        err = abs((x[-1] - x[-2]) / x[-1])

        if err < tolera:
            break

        it += 1

    return x[-1], it
