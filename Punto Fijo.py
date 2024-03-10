import matplotlib.pyplot as plt #libreria de graficar
import numpy as np  #libreria de uso y aplicacion de funciones y operaciones matematicas
from sympy import symbols, sqrt, lambdify, Eq, solve #libreria para recibir todas las funciones
from sympy import sympify

# Lista para almacenar las aproximaciones sucesivas
xi = []


# gx: La función de punto fijo.
# x0: El valor inicial.
# t: La tolerancia para la aproximación de la raíz,
# (valor por defecto: 0.0001).
#  itMax: Número máximo de iteraciones (valor por defecto: 100).


def puntofijo(gx, x0, t=0.0001, itMax=100):
    it = 0     # iteraciones contador
    x = symbols('x')
    gx_expr = gx(x) # Obtener la expresión de gx en términos de x

    # Convertir la expresión simbólica a una función numérica
    gx_func = lambdify(x, gx_expr, 'numpy')

    intervalo = float('inf')  # Inicializar el intervalo con infinito

    while (intervalo >= t and it < itMax):
        # Calcular la siguiente aproximación usando la función de punto fijo
        x1 = gx_func(x0)

        intervalo = abs(x1 - x0) # Calcular el intervalo entre aproximaciones
        
        # Imprimir información de la iteración actual
        print("Iteracion: ", it, " Raiz: ", x1, " Intervalo: ", intervalo)
        # Agregar la nueva aproximación a la lista
        xi.append(x1)

        # Actualizar el valor inicial para la siguiente iteración
        x0 = x1
        it += 1


    # Establecer el resultado como la última aproximación si no se alcanza el número máximo de iteraciones
    raiz = x1 if it < itMax else np.nan
    return raiz


# INGRESO DE DATOS
#fx_input = input("Ingrese la función f(x): Ejemplo 2*x**2 - x - 5  : ")
#gx_input = input("Ingrese la función g(x): Ejemploqrt(x + 5) / 2)  :")
while True:
    try:
        fx_input = input("Ingrese la función f(x): ")
        fx_expr = sympify(fx_input)
        break  # Salir del bucle si la expresión es válida
    except:
        print("Error en la expresión. Por favor, ingrese una función válida.")

while True:
    try:
        gx_input = input("Ingrese la función g(x): ")
        gx_expr = sympify(gx_input)
        break  # Salir del bucle si la expresión es válida
    except:
        print("Error en la expresión. Por favor, ingrese una función válida.")
x0 = float(input("Ingrese el valor inicial x0: "))
tolerancia = float(input("Ingrese la tolerancia para la aproximación de la raíz: "))

# Definir las funciones f(x) y g(x) utilizando sympy
x = symbols('x')
fx_expr = eval(fx_input)
gx_expr = eval(gx_input)



# Pruebas
# 2*x**2 - x - 5
# raiz o sqrt(x + 5) / 2)

# -x**2+1/3-1/9*x
#  1/3-2/9*x 


# Definir las funciones f(x) y g(x) a partir de las entradas del usuario


def fx(x): return fx_expr.subs('x', x)
def gx(x): return gx_expr.subs('x', x)

# PROCEDIMIENTO para Aplicar el método del punto fijo
respuesta = puntofijo(gx, x0, tolerancia)
print(xi)

# SALIDA
print("La raíz aproximada es:", respuesta)

# Gráfico
x_vals = np.linspace(-3, 3, 100)
y_fx = lambdify(x, fx_expr, 'numpy')(x_vals)

plt.title('Gráfico de la función f(x)')
plt.plot(x_vals, y_fx, label='f(x) = ' + fx_input)
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
for i in range(len(xi)):
    plt.scatter(xi[i], 0, color='blue', marker='.', label='Iteracion ' + str(i + 1))
plt.scatter(respuesta, fx(respuesta), marker='*', color='red', label='Raíz')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
