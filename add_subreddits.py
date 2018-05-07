import praw 
import pandas as pd
def add_subreddits(file):
    fd = open(file,'a')
    reddit = praw.Reddit(client_id='3y4m9Lty70NOag',
                         client_secret='04NbkR-SwPvwhhIaVPZlWLimUqM',
                         user_agent='<platform>:<app ID>:<version string> (by /u/AllHailLelouch)')
    #this is the list of subreddits from http://redditmetrics.com/top
    m = pd.read_csv(r"C:\Users\Ian\Documents\CS 361\subreddits.txt", sep='\t');
    print(m)
    subreddit_list = m['subreddit']
    for i in subreddit_list:
        string = i + ', '
        for submission in reddit.subreddit(i).top(limit=50):
            string += submission.title + " "
        fd.write(string)
    fd.close()
