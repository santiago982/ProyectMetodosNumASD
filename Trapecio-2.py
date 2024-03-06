import matplotlib.pyplot as plt
import numpy as np


#Solicitar la función al usuario
expression = input("Ingrese la función (utilice 'x' como variable): ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
n = int(input("Ingrese el número de trapecios (n): "))

# Definir la función fx
fx = lambda x: eval(expression)
#Entradas
#fx = lambda x: 1 + 2*x + 3*x**2
    #2 + 3*x

#Intervalo de integración
#a = -2
#b = 4

# n Segmentos o trapecios
#trapecios = 50
# h
h = (b-a)/n

# Metodo Trapezoidal
muestras = n+1
area_total = 0

xi = a

for i in range(0, n, 1):
    area_trapecio = h*(fx(xi)+fx(xi+h))/2
    area_total = area_total + area_trapecio
    # avanza al siguiente trapecio
    xi = xi + h
# Crear un distribución de puntos equidistantes
xi = np.linspace(a, b, muestras)
#Evaluamos cada xi en la funcion
fi = fx(xi)

# Salidas
print('Cantidad de trapecios: ', n)
print('El resultado de la integral en: ', area_total)
# Graficar la función y los trapecios de manera mejorada
plt.plot(xi, fi, 'bo-', label="Función")
plt.fill_between(xi, 0, fi, color='green', alpha=0.3, label="Área bajo la curva")
plt.title("Método del Trapecio - Caso 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()