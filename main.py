import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical gold spot prices (daily data)
def get_gold_data():
    # Downloading data for the past 10 years (you can adjust dates as needed)
    gold = yf.download('GC=F', start='2013-01-01', end='2023-01-01')
    return gold

# Fetch data
gold_data = get_gold_data()

# Show the first few rows
print(gold_data.head())

# Plot the data
plt.figure(figsize=(10,6))
plt.plot(gold_data['Close'], label='Gold Spot Price')
plt.title('Gold Spot Price (Last 10 Years)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
