import pandas as pd

def load_brent_data(path):
    try:
        df = pd.read_csv(path)
        df['Date'] = pd.to_datetime(df['Date'], format='mixed')
        return df.sort_values('Date').reset_index(drop=True)
    except Exception as e:
        print(f"Error loading Brent data: {e}")
        return None
