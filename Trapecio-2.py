import matplotlib.pyplot as plt
import numpy as np

#Entradas
fx = lambda x: 1 + 2*x + 3*x**2
    #2 + 3*x

#Intervalo de integración
a = -2
b = 4

# n Segmentos o trapecios
trapecios = 50
# h
h = (b-a)/trapecios

# Metodo Trapezoidal
muestras = trapecios+1
area_total = 0

xi = a

for i in range(0, trapecios, 1):
    area_trapecio = h*(fx(xi)+fx(xi+h))/2
    area_total = area_total + area_trapecio
    # avanza al siguiente trapecio
    xi = xi + h
# Crear un distribución de puntos equidistantes
xi = np.linspace(a, b, muestras)
#Evaluamos cada xi en la funcion
fi = fx(xi)

# Salidas
print('Cantidad de trapecios: ', trapecios)
print('El resultado de la integral en: ', area_total)
# Grafica puntos de muestra incluyendo extremos
plt.plot(xi, fi,'bo')
# Dibujamos lineas para dividir los trapecios
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w')
# Rellenamos los trapecios
plt.fill_between(xi, 0, fi, color='red')
plt.show()