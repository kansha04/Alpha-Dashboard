import yfinance as yf

def get_price(ticker):
    try:
        price = ticker.fast_info['last_price']
        return price
    except (KeyError, Exception) as e:
        return None

def main():
    # get user to enter a stock ticker
    history = []
    while True:
        user_input = input("Please enter a stock ticker (eg. AAPL, MSFT): ")
        user_input = user_input.upper().strip()
        if user_input == "EXIT" or user_input == "Q":
            print("Thank you for using this stock checker.")
            print("History")
            print("---------")
            for ticker in history:
                print(f"{ticker[0].ticker}: {ticker[1]:.2f}")
            break

        ticker = yf.Ticker(user_input)
        try:
            # Try to access ticker info to validate
            print(f"{ticker.ticker}: ${get_price(ticker):.2f}")
            history.append([ticker, get_price(ticker)])
        except (KeyError, Exception) as e:
            print(f"Error: '{user_input}' is not a valid stock ticker or data is unavailable.\nPlease check the ticker symbol and try again.")

if __name__ == '__main__':
    main()