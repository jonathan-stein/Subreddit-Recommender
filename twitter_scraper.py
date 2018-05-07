import tweepy
import keys
import sys
import re

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def get_user_tweets(username, filename):
    f = open(filename, 'a')
    f.write('user_twitter, ')
    for tweet in tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended').items():
        tweet_text = clean(tweet.full_text)
        f.write(tweet_text + ' ')
    f.write('\n')
    f.close()
def clean(tweet):
    tweet = re.sub('@\\w+ *', '', tweet)  # get rid of anything that starts with @
    tweet = re.sub(r'http\S+', '', tweet) # get rid of urls
    tweet = tweet.replace('\n',' ')
    return tweet

if __name__ == '__main__':
    get_user_tweets(sys.argv[1], 'tweets.txt')
