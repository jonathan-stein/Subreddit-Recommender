import tweepy
import keys
import sys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

def get_user_tweets(username):
    for tweet in tweepy.Cursor(api.user_timeline,id=username).items():
        print(tweet.text)

if __name__ == '__main__':
    get_user_tweets(sys.argv[1])
