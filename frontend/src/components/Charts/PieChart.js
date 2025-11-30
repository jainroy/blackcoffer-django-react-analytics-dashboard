import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = ({ data }) => {
  const counts = data.reduce((acc, entry) => {
    const topic = entry.topic || 'Unknown';
    acc[topic] = (acc[topic] || 0) + 1;
    return acc;
  }, {});
  
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'right' }
    }
  };
  
  return (
    <div style={{ height: '400px', position: 'relative' }}>
      <Pie 
        data={{
          labels: Object.keys(counts),
          datasets: [{
            data: Object.values(counts),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
          }]
        }} 
        options={options}
      />
    </div>
  );
};
export default PieChart;