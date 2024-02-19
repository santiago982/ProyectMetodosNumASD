import numpy as np#matrices,vectores
import matplotlib.pyplot as plt#graficar

#entradas
# Solicitar la función al usuario
expression = input("Ingrese la función (utilice 'x' como variable): ")
#Ejemplo
#2*3*x
fx= lambda x: eval(expression)
a=-0;
b=5;

n = 1;
h=(b-a)/n;
muestras = n+1;
areaTotal=0;

xi = a;
for i in range ( 0, n,1):
    areaTrapecio = h*(fx(xi)+fx(xi+h))/2
    areaTotal = areaTotal+areaTrapecio
    xi= xi +h;
    xi=np.linspace(a,b,muestras);
    fi= fx(xi)
    print("CANTIDAD DE TRAPECIOS")
    print("el resultado de la integral es:",areaTotal)
    plt.plot(xi,fi,"bo")
for i in range (0,muestras,1):
    plt.axvline(xi[i], color ="b")
plt.fill_between(xi,0,fi,color="green")
plt.show()