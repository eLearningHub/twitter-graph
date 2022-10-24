import os
import tweepy
from tweepy import OAuthHandler
    
def twitter_api():
    ''' Twitter API '''

    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_secret = os.environ.get('ACCESS_SECRET')
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)

def main():
    api = twitter_api()

if __name__ == "__main__":
    main()
