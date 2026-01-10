import yfinance as yf

def get_price(ticker):
    try:
        price = ticker.fast_info['last_price']
        return price
    except (KeyError, Exception) as e:
        return None

def main():
    # get user to enter a stock ticker
    while True:
        user_input = input("Please enter a stock ticker (eg. AAPL, MSFT): ")
        user_input = user_input.upper()
        if user_input == "EXIT" or user_input == "Q":
            print("Thank you for using this stock ticker.")
            break

        ticker = yf.Ticker(user_input)
        try:
            # Try to access ticker info to validate
            name = ticker.info['longName']
            print(f"{name}: ${get_price(ticker):.2f}")
        except (KeyError, Exception) as e:
            print(f"Error: '{user_input}' is not a valid stock ticker or data is unavailable.\nPlease check the ticker symbol and try again.")

if __name__ == '__main__':
    main()