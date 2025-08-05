import pandas as pd

def check_missing(df):
    return df.isnull().sum()

def clean_prices(df):
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    return df.dropna(subset=['Price'])
