import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Convertir la entrada a una función simbólica


def convertir_a_funcion(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr))

# método de la secante


def secante(fC, x0, x1, tolera=1e-6, max_iter=100):
    x = [x0, x1]
    y = [fC(x0), fC(x1)]
    it = 0
    while it < max_iter:
        # Calculo el siguiente valor de x mediante el método de la secante
        x_next = x[-1] - y[-1] * (x[-1] - x[-2]) / (y[-1] - y[-2])
        x.append(x_next)
        y.append(fC(x_next))

        # Calcular el error relativo
        err = abs((x[-1] - x[-2]) / x[-1])

        print(f"Iteración {it+1}: Raíz = {round(x[-1], 5)}")

        # Comprobar si se ha alcanzado la tolerancia deseada
        if err < tolera:
            break

        it += 1

    return x[-1], it


# Ingresar valores
funcionEntrante = input("Ingrese la función: ")
funcionConvertida = convertir_a_funcion(funcionEntrante)
x0 = float(input("Ingrese el valor de x0: "))
x1 = float(input("Ingrese el valor de x1: "))
tolera = float(
    input("Ingrese la tolerancia para la aproximación de la raíz: "))

# Calcular la raíz utilizando el método de la secante
print("--------------Método de la secante---------------")
raiz, it = secante(funcionConvertida, x0, x1)
print(f"El valor de la raíz es: {round(raiz, 5)} en la iteración: {it}.")

# Graficar la función y la raíz encontrada
x = np.linspace(raiz - 5, raiz + 5, 100)
y = funcionConvertida(x)
plt.plot(x, y, label='Función')
plt.plot(raiz, funcionConvertida(raiz), 'ro', label='Raíz')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfica del método de la secante')
plt.legend()
plt.show()

#Pruebas
#(x**3)+(2**2)+(10*x)-20
#3 ,2 

#
#