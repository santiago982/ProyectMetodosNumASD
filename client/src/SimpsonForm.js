import React, { useState, useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

function SimpsonsForm() {
  const [expression, setExpression] = useState('Math.sin(x)'); // Valor de ejemplo para la expresión
  const [n, setN] = useState(10); // Valor de ejemplo para n
  const [a, setA] = useState(0); // Valor de ejemplo para a
  const [b, setB] = useState(Math.PI); // Valor de ejemplo para b
  const [resultado, setResultado] = useState(null);
  const chartRef = useRef(null);
  const xAxisLineRef = useRef(null);
  const yAxisLineRef = useRef(null);

  useEffect(() => {
    drawAxisLines();
    return () => {
      if (chartRef.current) {
        chartRef.current.destroy();
      }
    };
  }, []);

   const handleSubmit = (e) => {
    e.preventDefault();

    // Validar que 'n' sea par
    if (n % 2 !== 0) {
      alert('El número de segmentos (n) debe ser par.');
      return;
    }

    const funcion = (x) => eval(expression);
    const h = (b - a) / n;
    let sumatoria = funcion(a) + funcion(b);
    for (let i = 1; i < n; i++) {
      const x = a + i * h;
      sumatoria += i % 2 === 0 ? 2 * funcion(x) : 4 * funcion(x);
    }
    const resultadoIntegral = (h / 3) * sumatoria;

    // Actualizar el estado del resultado
    setResultado(resultadoIntegral);

    // Graficar la función y el área bajo la curva
    if (chartRef.current) {
      chartRef.current.destroy();
    }
    const ctx = document.getElementById('myChart2').getContext('2d');
    chartRef.current = new Chart(ctx, {
      type: 'line',
      data: {
        labels: Array.from({ length: n + 1 }, (_, i) => a + (i * (b - a)) / n),
        datasets: [
          {
            label: 'Función y área bajo la curva',
            data: Array.from({ length: n + 1 }, (_, i) => funcion(a + (i * (b - a)) / n)),
            borderColor: 'blue',
            fill: 'origin',
            backgroundColor: 'rgba(0, 128, 0, 0.2)', // Color del área bajo la curva
          },
        ],
      },
      options: {
        scales: {
          x: {
            title: {
              display: true,
              text: 'x',
            },
          },
          y: {
            title: {
              display: true,
              text: 'f(x)',
            },
          },
        },
      },
    });
  };

  const drawAxisLines = () => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext('2d');
      ctx.beginPath();
      ctx.strokeStyle = 'red';

      // Dibujar eje X
      ctx.moveTo(0, chartRef.current.height / 2);
      ctx.lineTo(chartRef.current.width, chartRef.current.height / 2);

      // Dibujar eje Y
      ctx.moveTo(chartRef.current.width / 2, 0);
      ctx.lineTo(chartRef.current.width / 2, chartRef.current.height);

      ctx.stroke();
    }
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
            <label htmlFor="n" className="form-label">
              Introduzca n:
            </label>
            <input
              type="number"
              className="form-control"
              id="n"
              value={n}
              onChange={(e) => setN(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="a" className="form-label">
              Introduzca a:
            </label>
            <input
              type="number"
              className="form-control"
              id="a"
              value={a}
              onChange={(e) => setA(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="b" className="form-label">
              Introduzca b:
            </label>
            <input
              type="number"
              className="form-control"
              id="b"
              value={b}
              onChange={(e) => setB(e.target.value)}
            />
          </div>
          <div className="col d-flex align-items-end">
            <button type="submit" className="btn btn-primary">
              Calcular
            </button>
          </div>
        </div>
      </form>
      <div className="mt-3">
        {resultado !== null && <p>El resultado del método es = {resultado}</p>}
        <div className="position-relative border border-2 border-primary rounded-3" style={{ width: '1000px', height: '500px' }}>
        <canvas id="myChart2" className="position-absolute" style={{ zIndex: '1' }}></canvas>
        <div className="axis-line x-axis-line" ref={xAxisLineRef}></div>
        <div className="axis-line y-axis-line" ref={yAxisLineRef}></div>
      </div>
      </div>
    </div>
  );
}

export default SimpsonsForm;
