import React, { useState, useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';

function PuntoFijoForm() {
    const [fxInput, setFxInput] = useState('2*x**2 - x - 5');
    const [gxInput, setGxInput] = useState('(x + 5) / 2');
    const [x0, setX0] = useState(0);
    const [tolerance, setTolerance] = useState(0.001);
    const [chartInstance, setChartInstance] = useState(null);
    const xAxisLineRef = useRef(null);
    const yAxisLineRef = useRef(null);
  
    useEffect(() => {
      
    }, []);
  
    const handleSubmit = (e) => {
      e.preventDefault();
  
      const xi = []; // Lista para almacenar las aproximaciones sucesivas
  
      // gx: La función de punto fijo.
      // x0: El valor inicial.
      // t: La tolerancia para la aproximación de la raíz.
      // itMax: Número máximo de iteraciones.
      const puntofijo = (gx, x0, t, itMax) => {
        let it = 0; // iteraciones contador
        let x1 = gx(x0); // Calcular la primera aproximación
        let intervalo = Math.abs(x1 - x0); // Calcular el intervalo entre aproximaciones
  
        while (intervalo >= t && it < itMax) {
          // Iterar mientras se cumplan las condiciones de convergencia y el número máximo de iteraciones no se haya alcanzado
          x0 = x1; // Iterar mientras se cumplan las condiciones de convergencia y el número máximo de iteraciones no se haya alcanzado
          x1 = gx(x0); // Calcular la siguiente aproximación
          it++; // Incrementar el contador de iteraciones
          intervalo = Math.abs(x1 - x0); // Calcular el nuevo intervalo
  
          xi.push(x1); // Agregar la nueva aproximación a la lista
        }
  
        return x1; // Devuelve la raíz
      };
  
      const gx = (x) => eval(gxInput.replace(/x/g, `(${x})`)); // Función g(x)
      const results = puntofijo(gx, x0, tolerance, 100); // Aplicar el método del punto fijo
  
      // Graficar la función y las iteraciones
      renderChart(xi);
    };
  
    const renderChart = (xi) => {
      const ctx = document.getElementById('puntofijo').getContext('2d');
  
      if (!chartInstance) {
        // Si no hay una instancia de gráfico, crea una nueva
        const newChartInstance = new Chart(ctx, {
          type: 'line',
          data: {
            labels: xi.map((_, i) => i),
            datasets: [
              {
                label: 'f(x)',
                data: xi.map((xi) => eval(fxInput.replace(/x/g, `(${xi})`))),
                borderColor: 'blue',
                fill: false
              }
            ]
          },
          options: {
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Iteraciones'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'f(x)'
                }
              }
            }
          }
        });
  
        // Guardar la instancia del gráfico
        setChartInstance(newChartInstance);
      } else {
        // Si ya hay una instancia de gráfico, actualiza sus datos
        chartInstance.data.labels = xi.map((_, i) => i);
        chartInstance.data.datasets[0].data = xi.map((xi) => eval(fxInput.replace(/x/g, `(${xi})`)));
        chartInstance.update();
      }
    };

  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="row mt-3">
          <div className="col">
            <label htmlFor="fxInput" className="form-label">
              Ingrese la función f(x):
            </label>
            <input
              type="text"
              className="form-control"
              id="fxInput"
              value={fxInput}
              onChange={(e) => setFxInput(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="gxInput" className="form-label">
              Ingrese la función g(x):
            </label>
            <input
              type="text"
              className="form-control"
              id="gxInput"
              value={gxInput}
              onChange={(e) => setGxInput(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="x0" className="form-label">
              Ingrese el valor inicial x0:
            </label>
            <input
              type="number"
              className="form-control"
              id="x0"
              value={x0}
              onChange={(e) => setX0(parseFloat(e.target.value))}
            />
          </div>
          <div className="col">
            <label htmlFor="tolerance" className="form-label">
              Ingrese la tolerancia:
            </label>
            <input
              type="number"
              className="form-control"
              id="tolerance"
              value={tolerance}
              onChange={(e) => setTolerance(parseFloat(e.target.value))}
            />
          </div>
          <div className="col d-flex align-items-end">
            <button type="submit" className="btn btn-primary">
              Calcular
            </button>
          </div>
        </div>
      </form>
      <div className="position-relative border border-2 border-primary rounded-3" style={{ width: '1000px', height: '500px' }}>
        <canvas id="puntofijo" className="position-absolute" style={{ zIndex: '1' }}></canvas>
      </div>
    </div>
  );
}

export default PuntoFijoForm;
