import matplotlib.pyplot as plt
import numpy as np

#librerias de graficar y librerias de uso y aplicacion de funciones matematicas


xi = []


def puntofijo(gx, x0, t=0.0001, itMax=100):
    it = 0  # iteracion
    x1 = gx(x0)
    intervalo = abs(x1-x0)
    while (intervalo >= t and it <= itMax):
        x0 = x1
        x1 = gx(x0)
        it = it + 1
        intervalo = abs(x1-x0)
        print("Iteracion: ", it, " Raiz: ", x1, " Intervalo: ", intervalo)
        xi.append(x1)
    raiz = x1
    if (it >= itMax):
        raiz = np.nan
    return raiz


# PROGRAMA -----------------
# INGRESO
fx_input = input("Ingrese la función f(x): ")
gx_input = input("Ingrese la función g(x): ")
x0 = float(input("Ingrese el valor inicial x0: "))
tolera = float(
    input("Ingrese la tolerancia para la aproximación de la raíz: "))

# Pruebas
# 2*x**2 - x - 5
# (x + 5) / 2

# -x**2+1/3-1/9*x
#  1/3-2/9*x 




def fx(x): return eval(fx_input)
def gx(x): return np.sqrt(eval(gx_input))


b = 0      # intervalo
# tolera = 0.001
iteramax = 100  # iteraciones máximas

# PROCEDIMIENTO
respuesta = puntofijo(gx, x0, tolera)
print(xi)


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
