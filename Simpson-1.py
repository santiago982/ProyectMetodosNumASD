import matplotlib.pyplot as plt
import numpy as np #importacion de librerias 


def integracion_sim13(x, y): #Definicion de la funcion
 I = [] #Valor acumulado de la integral 

 if len(y) == len(x): #Comparar tamaño de los vectores de la variable 'x' y 'y'
    n = len(x) - 1 #cantidad de subintervalos 

    if n%2 == 0: #Verificacion del numero de subintervalos par
        a = x[0] #Limite de integracion inferior
        b = x[n] #Limite de integracion superior        
        sumy1 = 0 #Sumatoria del valor de la funcion en las posiciones impares
        sumy2 = 0 #Sumatoria del valor de la funcion en las posiciones pares 

        for i in range(1, n): #ciclo para llevar a cabo las sumatorias 

            if i%2 != 0: #Condicional para posiciones impares
                sumy1 += y[i] #Sumatoria de impares 

            else:
                sumy2 += y[i] #Sumatoria de pares 

        I = round((b - a)*(y[0] + 4*sumy1 + 2*sumy2 + y[n])/(3*n), 6) #Formula de la regla de simpson 1/3 multiple

    else:
     print("+") 

 else:
    print("'x' y 'y' deben ser del mismo tamaño") 

 return(I) 

#DATOS DE ENTRADA
a = -1 #Limite de integracion inferior del problema
b = 3 #Limite de integracion superior del problema
n = 20 #Cantidad de subintervalos 

#DATOS DE ENTRADA FUNCION
x = np.linspace(a, b, n + 1) #Vector de datos en 'x'

y= np.sqrt(5+x**3)

print(integracion_sim13(x, y)) #solucion numerica de la integral 

#Graficación
def funcion(x):
 f = np.sqrt(5+x**3)
 return f 

yn = funcion(x)
plt.plot(x, yn) # frafica la funcion (establece el plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="black") # establece las lineas de origen en x y el color
plt.axvline(0, color="black") # establece las lineas de origen en y y el color
plt.title("Metodo simpson 1/3")
plt.ylabel("Eje X")
plt.xlabel("Ejey")
plt.show()