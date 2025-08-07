import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { fetchOilPrices, fetchEvents, fetchChangePoint } from '../api';

const OilPriceChart = () => {
  const [oilPrices, setOilPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoint, setChangePoint] = useState(null);

  useEffect(() => {
    fetchOilPrices().then(res => setOilPrices(res.data));
    fetchEvents().then(res => setEvents(res.data));
    fetchChangePoint().then(res => setChangePoint(res.data));
  }, []);

  if (oilPrices.length === 0) return <div>Loading...</div>;

  const labels = oilPrices.map(d => d.Date);
  const data = oilPrices.map(d => d.Price || d.Close || d['Brent Spot Price']);

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Brent Oil Price',
        data,
        borderColor: 'blue',
        fill: false
      },
      ...(changePoint ? [{
        label: 'Change Point',
        data: Array(labels.length).fill(null).map((_, i) => i === changePoint.tau_index ? data[i] : null),
        borderColor: 'red',
        borderWidth: 3,
        pointRadius: 6,
        type: 'line'
      }] : [])
    ]
  };

  return (
    <div>
      <h2>Brent Oil Price & Change Point</h2>
      <Line data={chartData} />
      <h4>Change Point Summary</h4>
      {changePoint && (
        <ul>
          <li>Index (τ): {changePoint.tau_index}</li>
          <li>μ₁: {changePoint.mu_1}</li>
          <li>μ₂: {changePoint.mu_2}</li>
          <li>P(μ₁ &gt; μ₀): {changePoint.prob_mu1_greater_than_mu0}</li>
          <li>P(μ₂ &gt; μ₀): {changePoint.prob_mu2_greater_than_mu0}</li>
        </ul>
      )}
    </div>
  );
};

export default OilPriceChart;
