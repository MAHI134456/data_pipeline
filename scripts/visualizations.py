import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Prices (1987–2022)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD/barrel)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
import matplotlib.pyplot as plt

def plot_log_returns(df, date_col='Date', return_col='Log_Return'):
    """
    Plot the log returns over time.
    
    Parameters:
        df (pd.DataFrame): DataFrame with Date and Log_Return columns.
        date_col (str): Column name for date.
        return_col (str): Column name for log returns.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df[date_col], df[return_col], linewidth=0.8)
    plt.title("Log Returns of Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
