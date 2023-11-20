def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Método de bisección para encontrar la raíz de una función.

    Parameters:
    - func: La función para la cual se busca la raíz.
    - a, b: Extremos del intervalo [a, b] donde se realizará la búsqueda.
    - tolerance: Tolerancia para la convergencia (valor predeterminado: 1e-6).
    - max_iterations: Número máximo de iteraciones (valor predeterminado: 100).

    Returns:
    - root: Aproximación de la raíz.
    - iterations: Número de iteraciones realizadas.
    """

    # Verificar si los extremos del intervalo tienen signos opuestos
    if func(a) * func(b) > 0:
        raise ValueError("Los extremos del intervalo deben tener signos opuestos.")

    # Inicializar variables
    iteration = 0
    root = None

    # Bucle de iteraciones
    while iteration < max_iterations:
        # Calcular el punto medio del intervalo
        c = (a + b) / 2

        # Verificar si c es la raíz o si la tolerancia se ha alcanzado
        if abs(func(c)) < tolerance:
            root = c
            break

        # Actualizar el intervalo [a, b]
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        # Incrementar el contador de iteraciones
        iteration += 1

    return root, iteration

# Ejemplo de uso
def example_function(x):
    return x**2 - 4

# Intervalo inicial [a, b]
a, b = 0, 3

# Llamada al método de bisección
root, iterations = bisection_method(example_function, a, b)

# Mostrar resultados
if root is not None:
    print(f"Aproximación de la raíz: {root}")
    print(f"Número de iteraciones: {iterations}")
else:
    print("El método de bisección no convergió.")
