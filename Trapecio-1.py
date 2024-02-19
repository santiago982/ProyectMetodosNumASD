import numpy as np
import matplotlib.pyplot as plt

# Solicitar la función al usuario
expression = input("Ingrese la función (utilice 'x' como variable): ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
n = int(input("Ingrese el número de trapecios (n): "))

# Definir la función fx
fx = lambda x: eval(expression)

# Calcular el paso h
h = (b - a) / n

# Inicializar listas para almacenar las coordenadas de los puntos de la función
xi = np.linspace(a, b, n+1)
fi = fx(xi)

# Inicializar el área total
areaTotal = 0

# Calcular la integral utilizando el método del trapecio
for i in range(n):
    areaTrapecio = h * (fi[i] + fi[i+1]) / 2
    areaTotal += areaTrapecio

# Mostrar el resultado de la integral
print("El resultado de la integral es:", areaTotal)

# Graficar la función y los trapecios
plt.plot(xi, fi, "bo-", label="Función")
plt.fill_between(xi, 0, fi, color="green", alpha=0.3, label="Área bajo la curva")
plt.title("Método del Trapecio")
plt.legend()
plt.show()
