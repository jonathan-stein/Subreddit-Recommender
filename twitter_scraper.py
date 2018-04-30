import tweepy
import keys
import sys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

def get_user_tweets(username):
    f = open('tweets.txt', 'w')
    for tweet in tweepy.Cursor(api.user_timeline,id=username, tweet_mode='extended').items():
        f.write(tweet.full_text + '\n')
    f.close()

if __name__ == '__main__':
    get_user_tweets(sys.argv[1])
