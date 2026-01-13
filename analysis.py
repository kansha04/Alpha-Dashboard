import pandas as pd

# read csv file
df = pd.read_csv('stock_log.csv')
print(df)

# get mean price
mean = df['Price'].mean()

print(f"Mean price is ${mean:.2f}")