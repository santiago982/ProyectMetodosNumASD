import matplotlib.pyplot as plt #libreria de graficar
import numpy as np 
#libreria de uso y aplicacion de funciones y operaciones matematicas

 


xi = []   # Lista para almacenar las aproximaciones sucesivas

# gx: La función de punto fijo.
# x0: El valor inicial.
# t: La tolerancia para la aproximación de la raíz,
# (valor por defecto: 0.0001).
#  itMax: Número máximo de iteraciones (valor por defecto: 100).


def puntofijo(gx, x0, t=0.0001, itMax=100):
    it = 0       # iteraciones contador
    x1 = gx(x0)  # Calcular la primera aproximación
    intervalo = abs(x1-x0)   # Calcular el intervalo entre aproximaciones
    while (intervalo >= t and it <= itMax): # Iterar mientras se cumplan las condiciones de convergencia y el número máximo de iteraciones no se haya alcanzado
        x0 = x1              # Iterar mientras se cumplan las condiciones de convergencia y el número máximo de iteraciones no se haya alcanzado
        x1 = gx(x0)          # Calcular la siguiente aproximación
        it = it + 1          # Incrementar el contador de iteraciones
        intervalo = abs(x1-x0)   # Calcular el nuevo intervalo
        
        
        print("Iteracion: ", it, " Raiz: ", x1, " Intervalo: ", intervalo)
        xi.append(x1)    # Agregar la nueva aproximación a la lista

    raiz = x1              # Establecer el resultado como la última aproximación
    if (it >= itMax):      # Verificar si se alcanzó el número máximo de iteraciones
        raiz = np.nan      # Si sí, establecer el resultado como NaN (no es un número)
    return raiz            #devuelve resultado


# PROGRAMA -----------------
# INGRESO---------Datos
fx_input = input("Ingrese la función f(x): ") #funcion inicial 
gx_input = input("Ingrese la función g(x): ") #su despeje
x0 = float(input("Ingrese el valor inicial x0: ")) #Punto Inicial
tolera = float(
    input("Ingrese la tolerancia para la aproximación de la raíz: "))

# Pruebas
# 2*x**2 - x - 5
# (x + 5) / 2

# -x**2+1/3-1/9*x
#  1/3-2/9*x 


# Definir las funciones f(x) y g(x) a partir de las entradas del usuario


def fx(x): return eval(fx_input)
def gx(x): return np.sqrt(eval(gx_input))


b = 0      # intervalo
# tolera = 0.001
iteramax = 100  # iteraciones máximas

# PROCEDIMIENTO para Aplicar el método del punto fijo
respuesta = puntofijo(gx, x0, tolera)
print(xi)     # Imprimir la lista de aproximaciones


# SALIDA
print(respuesta)

# Gráfico
# Crear un rango de valores x desde -10 hasta 10
x = np.linspace(-3, 3, 100)

# Evaluar la función para cada valor de x
y = fx(x)
raiz = respuesta
y_punto = fx(raiz)


# Crear el gráfico
plt.title('Gráfico de la función f(x)')
plt.plot(x, y, label='f(x) = '+fx_input)
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
for i in range(len(xi)):
    plt.scatter(xi[i], 0, color='blue', marker='.',
                label='Iteracion '+str(i+1))
plt.scatter(raiz, y_punto, marker='*', color='red', label='Raíz')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
