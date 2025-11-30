import React from 'react';
import { Scatter } from 'react-chartjs-2';
import { Chart as ChartJS, LinearScale, PointElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(LinearScale, PointElement, Tooltip, Legend);

const ScatterChart = ({ data }) => {
  const datasets = data.slice(0, 20).map((entry, i) => ({
    label: entry.region || 'Unknown',
    data: [{ x: entry.relevance || 0, y: entry.intensity || 0 }],
    backgroundColor: `hsl(${i * 360 / 20}, 70%, 50%)`,
    pointRadius: Math.max(3, (entry.likelihood || 1) * 2)
  }));
  
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'top' }
    },
    scales: {
      x: { 
        title: { display: true, text: 'Relevance' },
        min: 0,
        max: 10
      },
      y: { 
        title: { display: true, text: 'Intensity' },
        min: 0,
        max: 10
      }
    }
  };
  
  return (
    <div style={{ height: '400px', position: 'relative' }}>
      <Scatter data={{ datasets }} options={options} />
    </div>
  );
};
export default ScatterChart;