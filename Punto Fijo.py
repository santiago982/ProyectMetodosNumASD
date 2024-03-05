import matplotlib.pyplot as plt
import numpy as np

xi = []  # Lista para almacenar las aproximaciones sucesivas

def puntofijo(gx, x0, t=0.0001, itMax=100):
    it = 0
    x1 = gx(x0)
    intervalo = abs(x1 - x0)
    
    while intervalo >= t and it < itMax:
        x0 = x1
        x1 = gx(x0)
        it += 1
        intervalo = abs(x1 - x0)
        
        print("Iteracion: ", it, " Raiz: ", x1, " Intervalo: ", intervalo)
        xi.append(x1)

    raiz = x1
    if it >= itMax:
        raiz = np.nan
        print("El método no converge después de", itMax, "iteraciones.")
    else:
        print("Convergencia alcanzada en la iteración", it)

    return raiz


# Validaciones de error al ingresar datos
while True:
    try:
        fx_input = input("Ingrese la función f(x): ")
        gx_input = input("Ingrese la función g(x): ")
        x0 = float(input("Ingrese el valor inicial x0: "))
        tolera = float(input("Ingrese la tolerancia para la aproximación de la raíz: "))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# Definir las funciones f(x) y g(x)
def fx(x): return eval(fx_input)
def gx(x): return np.sqrt(x) if "sqrt" in gx_input else np.exp(x) if "exp" in gx_input else gx_input(x)

# PROCEDIMIENTO para Aplicar el método del punto fijo
respuesta = puntofijo(gx, x0, tolera)
print(xi)

# Imprimir información final
print("\nResultado final:")
if np.isnan(respuesta):
    print("El método no converge.")
else:
    print("Raíz encontrada:", respuesta)

# Gráfico
x = np.linspace(-3, 3, 100)
y = fx(x)
raiz = respuesta
y_punto = fx(raiz)

plt.title('Gráfico de la función f(x)')
plt.plot(x, y, label='f(x) = '+fx_input)
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
for i in range(len(xi)):
    plt.scatter(xi[i], 0, color='blue', marker='.', label='Iteracion '+str(i+1))
plt.scatter(raiz, y_punto, marker='*', color='red', label='Raíz')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
