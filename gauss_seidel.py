import numpy as np
import matplotlib.pyplot as plt

def metodo_gauss_seidel(matriz_ecuaciones, val_indep_ecuaciones, x_inicial, tolerancia, max_iter=100):
    n = len(matriz_ecuaciones)
    x = x_inicial.copy()
    
    # Almacenar resultados para análisis
    iteraciones = []
    errores = []
    
    for k in range(max_iter):
        for i in range(n):
            suma = np.dot(matriz_ecuaciones[i, :i], x[:i]) + np.dot(matriz_ecuaciones[i, i+1:], x_inicial[i+1:])
            x[i] = (val_indep_ecuaciones[i] - suma) / matriz_ecuaciones[i, i]

        error = np.linalg.norm(x - x_inicial, ord=np.inf)
        iteraciones.append(x.copy())
        errores.append(error)
        
        if error < tolerancia:
            return x, iteraciones, errores
        
        x_inicial = x.copy()
        print(f"Iteración {k+1}: x = {np.round(x, 5)}, Error = {error}")

    print("El método no convergió en el número máximo de iteraciones.")
    return x, iteraciones, errores

# Ejemplo de uso simplificado
n = int(input("Introduce el número de ecuaciones: "))
matriz_ecuaciones = np.zeros((n, n))
val_indep_ecuaciones = np.zeros(n)
x_inicial = np.zeros(n)

print("Introduce las ecuaciones en el formato 'a11 a12 ... a1n b1', donde aij son los coeficientes y bi es el término independiente.")
for i in range(n):
    ec = list(map(float, input(f"Introduce la ecuación {i+1}: ").split()))
    matriz_ecuaciones[i] = ec[:-1]
    val_indep_ecuaciones[i] = ec[-1]
    x_inicial[i] = float(input(f"Introduce el valor inicial para x_{i+1}: "))

tolerancia = float(input("Introduce la tolerancia: "))
max_iter = int(input("Introduce el número máximo de iteraciones: "))

x_solucion, iteraciones, errores = metodo_gauss_seidel(matriz_ecuaciones, val_indep_ecuaciones, x_inicial, tolerancia, max_iter)

# Mostrar tabla de iteraciones y errores
tabla_iteraciones = np.vstack(iteraciones)
tabla_errores = np.array(errores)
print("\nTabla de Iteraciones:")
print(tabla_iteraciones)
print("\nErrores en cada iteración:")
print(tabla_errores)

# Graficar convergencia
plt.figure(figsize=(10, 6))
for i in range(n):
    plt.plot(range(1, len(errores)+1), tabla_iteraciones[:, i], label=f'x_{i+1}')

plt.title("Convergencia del Método de Gauss-Seidel")
plt.xlabel("Iteración")
plt.ylabel("Valor de x")
plt.legend()
plt.grid(True)
plt.show()    