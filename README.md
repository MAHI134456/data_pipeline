#  Brent Oil Price Change Point Detection

This project analyzes how **major geopolitical and economic events** have impacted **Brent crude oil prices** over time. Using **Bayesian change point detection** (with PyMC3), we aim to identify statistically significant shifts in oil price behavior and relate them to real-world events such as wars, OPEC policy changes, sanctions, and global crises like COVID-19.

---

##  Objective

To detect structural breaks in daily Brent oil prices from **1987 to 2022**, quantify the impact of major global events, and deliver insights for:

- **Investors** to make better market decisions
- **Policymakers** to plan for energy and economic stability
- **Energy companies** to improve operational forecasting

---

##  Project Structure
```bash
data_pipeline/
│
├── data/
│ ├── BrentOilPrices.csv # Raw daily oil prices
│ └── EventDataset.csv # Manually compiled key events
│
├── notebooks/
│ └── 01_data_preparation.ipynb # Load, clean, and explore data
│ └── 02_time_series_analysis.ipynb # Trend & stationarity analysis
│
├── scripts/
│ ├── load_data.py # Data loading function
│ ├── preprocess.py # Cleaning & preprocessing
│ ├── visualizations.py # Plotting utilities
│ └── time_series_utils.py # ADF test and helpers
│
├── reports/
│ ├── assumptions_and_limits.md # Limitations & causal discussion
│ ├── communication_plan.md # Formats for key stakeholders
│ └── model_description.md # Summary of change point modeling
│
├── outputs/
│ └── plots/ # Optional folder for exported visuals
│
├── README.md # You're here!
└── requirements.txt # Python dependencies
```

---

##  Key Concepts Covered

- Bayesian Inference using PyMC3
- Change Point Detection
- Time Series Stationarity & Trend Analysis
- Analytical Storytelling
- Event Mapping & Interpretation
- Policy Impact Reporting

---

##  Data Description

| Column | Description                            |
|--------|----------------------------------------|
| `Date` | Date of recorded oil price (`dd-mmm-yy`) |
| `Price`| Brent oil price in USD per barrel      |

---

##  Requirements

Install dependencies via pip:

```bash
pip install -r requirements.txt
