import praw
import pandas as pd
import keys
def add_subreddits(file):
    fd = open(file,'a')
    reddit = praw.Reddit(client_id=keys.reddit_client_id,
                         client_secret=keys.reddit_client_secret,
                         user_agent='<platform>:<app ID>:<version string> (by /u/AllHailLelouch)')
    #this is the list of subreddits from http://redditmetrics.com/top
    m = pd.read_csv(r"subreddits.txt", sep='\t');
#    print(m)
    subreddit_list = m['subreddit']
    counter = 0
    for i in subreddit_list:
        '''
        counter+=1
        if (counter > 30):
            break
        '''
        string = i + ',\"'
        for submission in reddit.subreddit(i).top(limit=50):
            string += (submission.title).replace('\"','') + " "
        fd.write(string+'\"\n')
    fd.close()
