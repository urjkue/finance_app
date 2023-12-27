import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

known_stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'UBER', 'NFLX']  # List of known stocks

stock_tickers = []
while True:
    print("Known stocks:", known_stocks)
    ticker = input("Enter a stock ticker (or 'done' to finish): ")
    if ticker.lower() == 'done':
        print(stock_tickers)
        break
    stock_tickers.append(ticker.upper())

start_date = pd.Timestamp.today().strftime('%Y-01-01')
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

df = pd.DataFrame()
for ticker in stock_tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    print(data)
    data = data[['Adj Close']]
    data.columns = [ticker]
    print(ticker)
    df = pd.concat([df, data], axis=1)

df.index = pd.to_datetime(df.index)

# Plotting
plt.figure(figsize=(12, 6))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)
plt.title('Stock Performance')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

output_file = 'user_stock_performance.xlsx'
df.to_excel(output_file)
print(f"Stock performance data saved to {output_file}.")
