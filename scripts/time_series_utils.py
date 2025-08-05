from statsmodels.tsa.stattools import adfuller

def adf_test(series):
    result = adfuller(series.dropna())
    return {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Used lags": result[2],
        "Number of observations": result[3],
        "Critical Values": result[4]
    }
