import tweepy

# Authenticate to Twitter
# Use real key values instead of placeholders
api_key = "your_api_key"
api_secret_key ="your_api_secret_key"
access_token = "your_access_token"
access_token_secret= "your_secret_access_token"

# Call the variables using tweepy
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('This is our first tweet!')