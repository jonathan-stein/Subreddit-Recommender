import tweepy
import keys
import sys
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def get_user_tweets(username):
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline,id=username, tweet_mode='extended').items():
        tweets.append(tweet.full_text)
    return tweets

# current code is based off https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/

def clean(tweet):
    stop_free = ' '.join([i for i in tweet.lower().split() if i not in stop])
    punc_free = ''.join([ch for ch in stop_free if ch not in exclude])
    normalized = ' '.join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

def run_lda(clean_tweets):
    dictionary = corpora.Dictionary(clean_tweets)
    doc_term_matrix = [dictionary.doc2bow(tweet) for tweet in clean_tweets]
    lda = gensim.models.ldamodel.LdaModel(doc_term_matrix, num_topics=1, id2word=dictionary, passes=1)
    print(lda.print_topics(num_topics=1, num_words=20))

if __name__ == '__main__':
    tweets = get_user_tweets(sys.argv[1])
    clean_tweets = [clean(tweet).split() for tweet in tweets]
    run_lda(clean_tweets)
