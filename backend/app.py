from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Update these paths to your actual data location
DATA_FOLDER = '../data_pipeline/data'
EVENT_FILE = 'oil_market_events.csv'
OIL_FILE = 'BrentOilPrices.csv'

@app.route('/api/oil-prices')
def get_oil_prices():
    df = pd.read_csv(os.path.join(DATA_FOLDER, OIL_FILE))
    df['Date'] = pd.to_datetime(df['Date'])
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/events')
def get_events():
    df = pd.read_csv(os.path.join(DATA_FOLDER, EVENT_FILE))
    df['Date'] = pd.to_datetime(df['Date'])
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/change-point')
def get_change_point():
    # Hardcoded results or load from file
    result = {
        "tau_index": 756,
        "mu_1": -0.001,
        "mu_2": 0.0003,
        "prob_mu1_greater_than_mu0": "75.00%",
        "prob_mu2_greater_than_mu0": "50.00%"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
