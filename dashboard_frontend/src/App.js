import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
import React from 'react';
import OilPriceChart from './components/OilPriceChart';

function App() {
  return (
    <div className="App">
      <h1>Brent Oil Price Dashboard</h1>
      <OilPriceChart />
    </div>
  );
}




export default App;
