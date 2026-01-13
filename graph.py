import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stock_log.csv')
top_5 = df.nlargest(5, 'Price')
tickers = top_5['Ticker']
prices = top_5['Price']

plt.bar(tickers, prices, width=0.5, color = 'green')
plt.xlabel('Stock Ticker')
plt.ylabel('Price in USD ($)')
plt.title('Stock Price Watchlist')
# display the graph
plt.show()