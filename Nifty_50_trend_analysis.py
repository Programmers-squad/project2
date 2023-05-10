import yfinance as yf
import matplotlib.pyplot as plt

# Define the index symbol and date range
symbol = '^NSEI'  # Symbol for Nifty 50 index
start_date = '2010-01-01'
end_date = '2021-12-31'

# Fetch the historical index price data
index_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate the 50-day moving average
index_data['MA_50'] = index_data['Close'].rolling(window=50).mean()

# Plotting the index price and moving average
plt.figure(figsize=(10, 6))
plt.plot(index_data['Close'], label='Index Price')
plt.plot(index_data['MA_50'], label='50-day Moving Average')
plt.title('Nifty 50 Index Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
