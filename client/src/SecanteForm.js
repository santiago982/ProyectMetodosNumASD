import React, { useState, useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

function SecanteForm() {
  const [expression, setExpression] = useState('x**3 + 2*x**2 + 10*x - 20');
  const [x0, setX0] = useState(3);
  const [x1, setX1] = useState(2);
  const [tolerance, setTolerance] = useState(1e-6);
  const [root, setRoot] = useState(null);
  const [iterations, setIterations] = useState(null);
  const chartRef = useRef(null);

  useEffect(() => {
    drawChart();
  }, [root]); // Este efecto se ejecutará cada vez que `root` cambie

  const handleSubmit = (e) => {
    e.preventDefault();

    // Convertir la entrada a una función simbólica
    const fC = (x) => eval(expression);

    // Método de la secante
    const secantMethod = (fC, x0, x1, tolerance, maxIter) => {
      let xi = x0;
      let xiPlus1 = x1;
      let fi = fC(xi);
      let fiPlus1 = fC(xiPlus1);
      let iter = 0;

      while (iter < maxIter) {
        const xNext = xiPlus1 - fiPlus1 * (xiPlus1 - xi) / (fiPlus1 - fi);
        const fNext = fC(xNext);
        const error = Math.abs((xNext - xiPlus1) / xNext);

        if (error < tolerance) {
          return [xNext, iter];
        }

        xi = xiPlus1;
        fi = fiPlus1;
        xiPlus1 = xNext;
        fiPlus1 = fNext;
        iter++;
      }

      return [xiPlus1, iter];
    };

    // Calcular la raíz utilizando el método de la secante
    const [foundRoot, iterations] = secantMethod(fC, x0, x1, tolerance, 100);

    // Actualizar el estado con el resultado
    setRoot(foundRoot);
    setIterations(iterations);
  };

  const drawChart = () => {
    if (root === null || chartRef.current === null) {
      return;
    }

    // Graficar la función y la raíz encontrada
    const ctx = chartRef.current.getContext('2d');
    const fC = (x) => eval(expression);
    const data = {
      labels: Array.from({ length: 100 }, (_, i) => i - 50),
      datasets: [
        {
          label: 'Función',
          data: Array.from({ length: 100 }, (_, i) => fC(i - 50)),
          borderColor: 'blue',
          fill: false,
        },
        {
          label: 'Raíz',
          data: [{ x: root, y: fC(root) }],
          borderColor: 'red',
          fill: false,
          pointRadius: 5,
          pointHoverRadius: 10,
        },
      ],
    };

    // Verificar si ya existe una instancia y destruirla si es necesario
    if (chartRef.current.chart) {
      chartRef.current.chart.destroy();
    }

    // Crear una nueva instancia de Chart.js
    chartRef.current.chart = new Chart(ctx, {
      type: 'line',
      data: data,
      options: {
        scales: {
          x: {
            title: {
              display: true,
              text: 'X',
            },
          },
          y: {
            title: {
              display: true,
              text: 'Y',
            },
          },
        },
      },
    });
  };

  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="row mt-3">
          <div className="col">
            <label htmlFor="expression" className="form-label">
              Ingrese la función:
            </label>
            <input
              type="text"
              className="form-control"
              id="expression"
              value={expression}
              onChange={(e) => setExpression(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="x0" className="form-label">
              Ingrese el valor de x0:
            </label>
            <input
              type="number"
              className="form-control"
              id="x0"
              value={x0}
              onChange={(e) => setX0(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="x1" className="form-label">
              Ingrese el valor de x1:
            </label>
            <input
              type="number"
              className="form-control"
              id="x1"
              value={x1}
              onChange={(e) => setX1(e.target.value)}
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
              onChange={(e) => setTolerance(e.target.value)}
            />
          </div>
          <div className="col d-flex align-items-end">
            <button type="submit" className="btn btn-primary">
              Calcular
            </button>
          </div>
        </div>
      </form>
      <div>
        {root !== null && iterations !== null && (
          <div>
            <p>El valor de la raíz es: {root.toFixed(5)} en la iteración: {iterations}.</p>
            <div className="position-relative border border-2 border-primary rounded-3" style={{ width: '1000px', height: '500px' }}>
              <canvas id="myChart" ref={chartRef} className="position-absolute" style={{ zIndex: '1' }}></canvas>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default SecanteForm;
