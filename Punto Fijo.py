import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

xi = []
fx_input = ""
gx_input = ""


def puntofijo(gx, x0, t=0.0001, itMax=100):
    global xi
    xi = []
    it = 0
    x1 = gx(x0)
    intervalo = abs(x1 - x0)
    while intervalo >= t and it <= itMax:
        x0 = x1
        x1 = gx(x0)
        it += 1
        intervalo = abs(x1 - x0)
        xi.append(x1)
    raiz = x1
    if it >= itMax:
        raiz = np.nan
    return raiz


def fx(x):
    return eval(fx_input)


def gx(x):
    return np.sqrt(eval(gx_input))


def calcular_raiz():
    global xi, fx_input, gx_input
    xi = []
    fx_input = fx_entry.get()
    gx_input = gx_entry.get()
    x0 = float(x0_entry.get())
    tolera = float(tolera_entry.get())

    respuesta = puntofijo(gx, x0, tolera)

    # Limpiar el gráfico anterior
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # Crear un rango de valores x desde -3 hasta 3
    x = np.linspace(-3, 3, 100)
    y = fx(x)
    raiz = respuesta
    y_punto = fx(raiz)

    # Crear el gráfico
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x, y, label='f(x) = ' + fx_input)
    plot.axhline(y=0, color='black', linestyle='--')
    plot.axvline(x=0, color='black', linestyle='--')
    for i in range(len(xi)):
        plot.scatter(xi[i], 0, color='blue', marker='.', label='Iteracion ' + str(i + 1))
    plot.scatter(raiz, y_punto, marker='*', color='red', label='Raíz')
    plot.set_xlabel('x')
    plot.set_ylabel('f(x)')
    plot.legend()
    plot.grid(True)

    # Agregar el gráfico a la interfaz
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Método del Punto Fijo")

# Crear y configurar el frame principal
frame_principal = ttk.Frame(root, padding="10")
frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiquetas y campos de entrada
ttk.Label(frame_principal, text="Función f(x):").grid(row=0, column=0, sticky=tk.W)
fx_entry = ttk.Entry(frame_principal)
fx_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame_principal, text="Función g(x):").grid(row=1, column=0, sticky=tk.W)
gx_entry = ttk.Entry(frame_principal)
gx_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame_principal, text="Valor inicial x0:").grid(row=2, column=0, sticky=tk.W)
x0_entry = ttk.Entry(frame_principal)
x0_entry.grid(row=2, column=1, sticky=tk.W)

ttk.Label(frame_principal, text="Tolerancia:").grid(row=3, column=0, sticky=tk.W)
tolera_entry = ttk.Entry(frame_principal)
tolera_entry.grid(row=3, column=1, sticky=tk.W)

# Botón de calcular
calcular_button = ttk.Button(frame_principal, text="Calcular Raíz", command=calcular_raiz)
calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame para el gráfico
frame_grafico = ttk.Frame(root)
frame_grafico.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()