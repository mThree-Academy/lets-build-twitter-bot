import yfinance as yf

data = yf.download(tickers='JW-A', period='1D', interval='1D')
print(data)