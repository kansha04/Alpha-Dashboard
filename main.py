# Alpha Dashbboard
import yfinance as yf

# get the current stock price of a ticker given by the user
def get_stock_price():
    # get user to enter a stock ticker
    user_input = input("Please enter a stock ticker (eg. AAPL, MSFT): ")
    ticker_symbol = user_input.upper()
    
    ticker = yf.Ticker(ticker_symbol)
    name = ticker.info['longName']
    price = ticker.fast_info['last_price']
    print(f"{name}: ${price:.2f}")
    
get_stock_price()