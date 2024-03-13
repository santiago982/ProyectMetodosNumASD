import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import Chart from "chart.js/auto";
import Form from "./SimpsonForm";
import "./App.css"; 
import PuntoFijoForm from "./PuntoFijoForm";
import SecanteForm from "./SecanteForm";

function App() {
  const [expression, setExpression] = useState("");
  const [a, setA] = useState("");
  const [b, setB] = useState("");
  const [root, setRoot] = useState(null);
  const [iterations, setIterations] = useState(null);
  const chartRef = useRef(null);
  const xAxisLineRef = useRef(null);
  const yAxisLineRef = useRef(null);
  const polynomialChartRef = useRef(null);
  const [chartData, setChartData] = useState(null);
  const [polynomialValues, setPolynomialValues] = useState({
    a: 1,
    b: -1,
    c: 4,
  });

  const handleChartData = (data) => {
    setChartData(data);
  };

  useEffect(() => {
    renderChart();
    drawAxisLines();
    renderPolynomialChart();
  }, [root]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/bisection", {
        expression,
        a,
        b,
      });
      setRoot(response.data.root);
      setIterations(response.data.iterations);
    } catch (error) {
      console.error(error.response.data.error);
    }
  };

  const renderChart = () => {
    if (root !== null) {
      if (chartRef.current !== null) {
        chartRef.current.destroy();
      }
      const xValues = [...Array(100).keys()].map(
        (x) => parseFloat(a) + ((parseFloat(b) - parseFloat(a)) * x) / 100
      );
      const yValues = xValues.map((x) => eval(expression));

      const ctx = document.getElementById("myChart").getContext("2d");
      const myChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: xValues,
          datasets: [
            {
              label: "Function",
              data: yValues,
              borderColor: "rgb(75, 192, 192)",
              tension: 0.1,
            },
          ],
        },
        options: {
          scales: {
            x: {
              type: "linear",
              position: "bottom",
              scaleLabel: {
                display: true,
                labelString: "Eje X",
              },
            },
            y: {
              type: "linear",
              position: "left",
              scaleLabel: {
                display: true,
                labelString: "Eje Y",
              },
            },
          },
        },
      });
      chartRef.current = myChart;
    }
  };

  const drawAxisLines = () => {
    if (chartRef.current) {
      const xAxis = chartRef.current.scales["x"];
      const yAxis = chartRef.current.scales["y"];

      const xAxisLine = xAxisLineRef.current;
      const yAxisLine = yAxisLineRef.current;

      if (xAxisLine && yAxisLine) {
        xAxisLine.style.top = `${yAxis.getPixelForValue(0)}px`;
        xAxisLine.style.width = `${chartRef.current.width}px`;

        yAxisLine.style.left = `${xAxis.getPixelForValue(0)}px`;
        yAxisLine.style.height = `${chartRef.current.height}px`;
      }
    }
  };

  const handlePolynomialValuesChange = (e) => {
    const { name, value } = e.target;
    setPolynomialValues({ ...polynomialValues, [name]: parseFloat(value) });
  };

  const evaluatePolynomial = (x) => {
    const { a, b, c } = polynomialValues;
    return a * Math.pow(x, 2) + b * x + c;
  };

  const generatePolynomialData = () => {
    const step = 0.1;
    const data = [];
    for (let x = parseFloat(a); x <= parseFloat(b); x += step) {
      data.push({ x, y: evaluatePolynomial(x) });
    }
    return data;
  };

  const renderPolynomialChart = () => {
    const polynomialData = generatePolynomialData();
    if (polynomialChartRef.current !== null) {
      polynomialChartRef.current.destroy();
    }
    const ctx = document.getElementById("polynomialChart").getContext("2d");
    const myChart = new Chart(ctx, {
      type: "line",
      data: {
        datasets: [
          {
            label: "Polynomial",
            data: polynomialData,
            borderColor: "rgb(255, 99, 132)",
            fill: false,
          },
        ],
      },
      options: {
        scales: {
          x: {
            type: "linear",
            position: "bottom",
            scaleLabel: {
              display: true,
              labelString: "Eje X",
            },
          },
          y: {
            type: "linear",
            position: "left",
            scaleLabel: {
              display: true,
              labelString: "Eje Y",
            },
          },
        },
      },
    });
    polynomialChartRef.current = myChart;
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-3">Gráfico del Metodo Biseccion</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="row mt-3">
          <div className="col">
            <label htmlFor="expression" className="form-label">
              Ingrese la expresión:
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
            <label htmlFor="lowerBound" className="form-label">
              Límite inferior (a):
            </label>
            <input
              type="number"
              className="form-control"
              id="lowerBound"
              value={a}
              onChange={(e) => setA(e.target.value)}
            />
          </div>
          <div className="col">
            <label htmlFor="upperBound" className="form-label">
              Límite superior (b):
            </label>
            <input
              type="number"
              className="form-control"
              id="upperBound"
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

      {/* Gráfico de la función */}
      <div
        className="position-relative border border-2 border-primary rounded-3"
        style={{ width: "1000px", height: "500px" }}
      >
        <canvas
          id="myChart"
          className="position-absolute"
          style={{ zIndex: "1" }}
        ></canvas>
        <div
          ref={xAxisLineRef}
          className="position-absolute border-bottom border-danger"
          style={{ width: "80%", left: "10%" }}
        ></div>
        <div
          ref={yAxisLineRef}
          className="position-absolute border-end border-danger"
          style={{ height: "80%", top: "10%" }}
        ></div>
      </div>

      {/* Gráfico del Polinomio */}
      <div className="mt-5">
        <h2 className="mb-3">Gráfico del Polinomio de Diferencias Divididas</h2>
        <div className="row">
          <div className="col">
            <label htmlFor="a" className="form-label">
              Valor de a:
            </label>
            <input
              type="number"
              className="form-control"
              id="a"
              name="a"
              value={polynomialValues.a}
              onChange={handlePolynomialValuesChange}
            />
          </div>
          <div className="col">
            <label htmlFor="b" className="form-label">
              Valor de b:
            </label>
            <input
              type="number"
              className="form-control"
              id="b"
              name="b"
              value={polynomialValues.b}
              onChange={handlePolynomialValuesChange}
            />
          </div>
          <div className="col">
            <label htmlFor="c" className="form-label">
              Valor de c:
            </label>
            <input
              type="number"
              className="form-control"
              id="c"
              name="c"
              value={polynomialValues.c}
              onChange={handlePolynomialValuesChange}
            />
          </div>
          <div className="col d-flex align-items-end">
            <button onClick={renderPolynomialChart} className="btn btn-primary">
              Calcular
            </button>
          </div>
        </div>
        <div
          className="position-relative border border-2 border-primary rounded-3"
          style={{ width: "1000px", height: "500px" }}
        >
          <canvas
            id="polynomialChart"
            className="position-absolute"
            style={{ zIndex: "1" }}
          ></canvas>
          <div
            ref={xAxisLineRef}
            className="position-absolute border-bottom border-danger"
            style={{ width: "80%", left: "10%" }}
          ></div>
          <div
            ref={yAxisLineRef}
            className="position-absolute border-end border-danger"
            style={{ height: "80%", top: "10%" }}
          ></div>
        </div>
        <div>
          <h2 className="mb-3">Gráfico del Metodo Simpson</h2>
          <Form />
        </div>
        <div>
          <h2 className="mb-3">Gráfico del Punto Fijo</h2>
          <PuntoFijoForm/>
        </div>
        <div>
          <h2 className="mb-3">Gráfico del Metodo Secante</h2>
          <SecanteForm/>
        </div>

        
      </div>
      <div className="mt-5">
        <h1 id="project-title">ProyectMetodosNumASD</h1>
        <p>Metodos Numericos 2023-2</p>
        <p>Proyecto Para Materia de Metodos Numericos 2023-2</p>
        <p>Sergio Andres Mesa</p>
        <p>Santiago Andres Bernal Ponguta</p>
        <p>Daniel Cardozo</p>
      </div>
    </div>
    
  );
}

export default App;
