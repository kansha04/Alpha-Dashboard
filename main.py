import yfinance as yf
import csv
import pandas as pd
import matplotlib.pyplot as plt

def get_price(ticker):
    try:
        price = ticker.fast_info['last_price']
        return price
    except (KeyError, Exception) as e:
        return None

# WHen the user exits its saves history list to a CSV file (e.g., stock_log.csv).
def stock_logger_csv(history):
    with open('stock_log.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Ticker', 'Price'])
        for ticker in history:
            csv_writer.writerow([ticker[0].ticker, ticker[1]])

def generate_chart():
    try:
        df = pd.read_csv('stock_log.csv')
        if df.empty:
            print('No data to plot.')
            return
        top_5 = df.nlargest(5, 'Price')
        tickers = top_5['Ticker']
        prices = top_5['Price']
        # generate chart
        plt.bar(tickers, prices, width=0.5, color='green')
        plt.xlabel('Stock Ticker')
        plt.ylabel('Price in USD ($)')
        plt.title('Stock Price Watchlist')
        # display the graph
        plt.show() # plt.savefig('chart.png') if we want to make the program to save the graph to a file so it doesn't freeze the backend
    except FileNotFoundError:
        print('No data file found.')


def plot_history(ticker, user_input):
    monthly_data = ticker.history(period='1mo')
    print(monthly_data.head())
    sma_5 = monthly_data['Close'].rolling(window=5).mean()
    # Graphing
    plt.figure(figsize=(10, 10))
    plt.plot(monthly_data['Close'], label='Price', color='blue')
    plt.plot(sma_5, label='5-day SMA', color='red')
    plt.title(f'{user_input} Price History')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

def main():
    # enter stock ticker
    print("Welcome to the Alpha Dashboard!")
    print("===============================")
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
            generate_chart()
            break

        ticker = yf.Ticker(user_input)
        try:
            # Try to access ticker info to validate
            price = get_price(ticker)
            if price is None:
                print(f"Error: Price data unavailable for '{user_input}'")
            else:
                print(f"{ticker.ticker}: ${price:.2f}")
                history.append([ticker, price])
                show_plot = input("Plot history? (y/n): ").lower()
                if show_plot == 'y':
                    plot_history(ticker, user_input)
                    print("Graph generated.")
        except (KeyError, Exception) as e:
            print(f"Error: '{user_input}' is not a valid stock ticker or data is unavailable.\nPlease check the ticker symbol and try again.")
    stock_logger_csv(history)
if __name__ == '__main__':
    main()