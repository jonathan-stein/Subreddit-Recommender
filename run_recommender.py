import twitter_scraper
import recommender
import sys
import add_subreddits
if __name__ == '__main__':

    file = open('items.csv', 'w')
    file.write('name,text\n')
    file.close()
    twitter_scraper.get_user_tweets(sys.argv[1], 'items.csv')
    add_subreddits.add_subreddits('items.csv')

    results = recommender.train('items.csv')
    recommended_subreddits = results['user_twitter'][:5]  # returns top 5 subreddits right now
    i = 1
    for rec in recommended_subreddits:
        print(str(i) + ': '+ rec)
        i+=1
