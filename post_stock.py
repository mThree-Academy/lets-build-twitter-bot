import tweepy 
import yfinance as yf 
import os 
 
# Authenticate to Twitter 
# Use real key values instead of placeholders 
api_key = "your_api_key" 
api_secret_key ="your_api_secret_key" 
access_token = "your_access_token" 
access_token_secret= "your_secret_access_token" 
 
# Call the variables using tweepy 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 
 
# Retrieve the stock data 
api = tweepy.API(auth) 
data = yf.download(tickers='JW-A', period='1D', interval='1D') 
 
row = data.iloc[0] 
status = "The open price of Wiley's stock is %s. The close price of Wiley's stock is %s. Volume recorded is %s." %(str(round(row['Open'], 2)),str(round(row['Close'], 2)),str(int(row['Volume']))) 
api.update_status(status) 