import yfinance as yf

def get_stock_price():
    # get user to enter a stock ticker
    user_input = input("Please enter a stock ticker (eg. AAPL, MSFT): ")
    ticker_symbol = user_input.upper()
    
    ticker = yf.Ticker(ticker_symbol)
    
    try:
        # Try to access ticker info to validate
        name = ticker.info['longName']
        price = ticker.fast_info['last_price']
        print(f"{name}: ${price:.2f}")
    except (KeyError, Exception) as e:
        print(f"Error: '{ticker_symbol}' is not a valid stock ticker or data is unavailable.")
        print("Please check the ticker symbol and try again.")
    
get_stock_price()