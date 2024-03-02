import sympy as sym
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x') # La variable simbolica para realizar los caálculos correspondientes

# Diferencias divididas y Polinomio de Newton
def ddn(m, z):
    #Obtencion de diferencias divididas
    #Se crea una matriz para añadir los vectores de x y de y
    a = []
    #La matriz tiene dimensiones (n+1) x n, donde n es la cantidad de puntos dados.
    for g in range(len(m)+1):
        aux = []
        for e in range(len(m)):
            aux.append(0)
        a.append(aux)


    for s in range(len(m)):
        # Se llena la primera fila de la matriz a con las coordenadas en x (m) y la segunda fila con las coordenadas en y (z).
        a[0][s] = (m[s])
        a[1][s] = (z[s])
        b = 1
        c = 1
        d = 1           

    for i in range(len(a[0])):
        for j in range(len(a[0])-b):
            a[c+1][j] = ((a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j])) #Formula de las diferencias divididas, los resultados que se guardaran en la matriz
        b+= 1
        c+= 1
        d+= 1


    #Se imprime en consola la matriz de diferencias divididas, mostrando los valores de x y f(x) de manera ordenada.
    print(" X | f(X)")
    matrix = np.array(a)
    matrix_t = np.transpose(matrix)
    print(matrix_t)

    # Se inicializan variables para representar el polinomio y un contador.
    p=0
    w=0

    #Se utiliza un bucle para construir el polinomio interpolante utilizando las diferencias divididas.
    for t in range(len(a[0])):
        terminos=1
        for r in range(w):
            terminos*=(x-a[0][r])
        w+=1
        p+= a[t+1][0]*terminos
        # Se simplifica el polinomio y se imprime.
        pol=simplify(p)
    print("\n Polinomio: ")
    print(pol)
    return pol

# Datos de entrada
m = [1, 0, -3]
z = [2, 4, -2]

#Grafica
px = sym.lambdify(x,ddn(m,z)) #Transforma la expresion en una funcion lambda
pxi=np.linspace(-10,10,100)
pfi = px(pxi)
np.set_printoptions(precision = 4)
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.axvline(x=0, ymin=-10, ymax=10)
plt.axhline(y=0, xmin=-10, xmax=10)
plt.axvline(color="black")
plt.axhline(color="black")

#PUNTOS
plt.plot(m,z,'ro', label = 'Puntos')
#FUNCION
plt.plot(pxi,pfi, label = 'Polinomio')
plt.title('Diferencias Divididas - Newton')
plt.legend() 
plt.show()