import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# followed tutorial from https://www.kaggle.com/cclark/simple-content-based-recommendation-engine

def train(data_file):
    data_set = pd.read_csv(data_file)
    tfidf_matrix = TfidfVectorizer(analyzer='word', ngram_range=(1,1), stop_words='english', sublinear_tf=True) # may want to remove sublinlear_tf and change min_df to 1: right now only unigrams
    tfidf_fit = tfidf_matrix.fit_transform(data_set['description'])
    similarities = cosine_similarity(tfidf_fit, tfidf_fit)

    most_similar = {}  # dictionary that maps twitter/subreddit to most similar subreddits/similarity score

    for index, row in data_set.iterrows():
        reverse_sorted_indices = similarities[index].argsort()
        sorted_indices = reverse_sorted_indices[::-1] # sorted by indixes of items most similar to items least similar (document itself will always be number 1)
        similar_subreddits = []
        for idx in sorted_indices:
            item_score = (data_set['name'][idx], similarities[index][idx])
            similar_subreddits.append(item_score)
        most_similar[row['name']] = similar_subreddits[1:] # don't include itself

    return most_similar

results = train("items.csv")
recs = results["Baby sunshade top"][:5]
for rec in recs:
    print("Recommended: " + rec[0] + " (score:" + str(rec[1]) + ")")
