import pandas as pd

def check_missing(df):
    return df.isnull().sum()

def clean_prices(df):
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    return df.dropna(subset=['Price'])
import numpy as np
import pandas as pd

def compute_log_returns(df, price_col='Price'):
    """
    Compute log returns for a given price column.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing a 'Price' column.
        price_col (str): Name of the column with price data.

    Returns:
        pd.DataFrame: DataFrame with a new 'Log_Return' column.
    """
    df = df.copy()
    df['Log_Return'] = np.log(df[price_col] / df[price_col].shift(1))
    df = df.dropna(subset=['Log_Return'])
    return df
