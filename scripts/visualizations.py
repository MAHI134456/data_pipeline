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
