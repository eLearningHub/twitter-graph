import os
import tweepy
from tweepy import OAuthHandler
    
def twitter_client():
    ''' Client for Twitter API V2 '''

    return tweepy.Client(bearer_token=os.environ.get('BEARER_TOKEN'))

def main():
    client = twitter_client()
    # Replace with your own search query
    query = 'from:suhemparack -is:retweet'
    
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
    
    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)

if __name__ == "__main__":
    main()
