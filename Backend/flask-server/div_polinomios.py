import sympy as sym
import numpy as np

class DiferenciasDivididas:
    @staticmethod
    def ddn(m, z):
        x = sym.symbols('x')
        a = []
        for g in range(len(m)+1):
            aux = []
            for e in range(len(m)):
                aux.append(0)
            a.append(aux)

        for s in range(len(m)):
            a[0][s] = m[s]
            a[1][s] = z[s]
            b = 1
            c = 1
            d = 1           

        for i in range(len(a[0])):
            for j in range(len(a[0])-b):
                a[c+1][j] = ((a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j]))
            b += 1
            c += 1
            d += 1

        p = 0
        w = 0

        for t in range(len(a[0])):
            terminos = 1
            for r in range(w):
                terminos *= (x-a[0][r])
            w += 1
            p += a[t+1][0] * terminos
            pol = sym.simplify(p)

        return pol
