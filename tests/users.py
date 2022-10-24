import os
import tweepy


def main():
    # Read Twitter credentials from environment variables
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_KEY = os.environ.get('ACCESS_KEY')
    ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

if __name__ == "__main__":
    main()
