from flask import Flask, request, jsonify
import sympy as sp
from bisection import bisection_method
from div_polinomios import DiferenciasDivididas
from metodo_simpson import simpson, convertir_a_funcion, calcular_error_simpson

app = Flask(__name__)

@app.route('/bisection', methods=['POST'])
def bisection():
    data = request.get_json()
    expression = data['expression']
    a = float(data['a'])
    b = float(data['b'])

    try:
        root, num_iterations = bisection_method(expression, a, b)
        return jsonify({'root': root, 'iterations': num_iterations})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/div_polynomial', methods=['POST'])
def div_polynomial():
    data = request.get_json()
    m = data['m']
    z = data['z']

    try:
        pol = DiferenciasDivididas.ddn(m, z)
        return jsonify({'polynomial': str(pol)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route('/simpson', methods=['POST'])
def calcular_simpson():
    data = request.get_json()
    expression = data['expression']
    a = float(data['a'])
    b = float(data['b'])
    n = int(data['n'])

    try:
        funcion = convertir_a_funcion(expression)
        resultado = simpson(funcion, a, b, n)
        error = calcular_error_simpson(funcion, a, b, n)
        return jsonify({'resultado': resultado, 'error': error})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/calcularSecante', methods=['POST'])
def calcular_secante():
    data = request.get_json()
    funcion = data['funcion']
    x0 = data['x0']
    x1 = data['x1']
    tolera = data['tolera']
    
    funcion_convertida = convertir_a_funcion(funcion)
    
    raiz, it = secante(funcion_convertida, x0, x1, tolera)
    
    return jsonify({"raiz": raiz, "iteraciones": it})


if __name__ == '__main__':
    app.run(debug=True)
