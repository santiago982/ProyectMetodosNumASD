# bisection.py

import numpy as np

def bisection_method(expression, a, b, tol=1e-6, max_iter=100):
    def func(x):
        return eval(expression)
    
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
