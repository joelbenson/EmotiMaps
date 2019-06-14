import csv
import os

def get_emotion_of_tweet(tweet):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(THIS_FOLDER, 'anew1999-list.csv'), newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        
        dict_words = {row['Description'] : (row['Valence Mean'], row['Arousal Mean'], row['Dominance Mean']) for row in reader}

    tweet_word_list = tweet.split()
    tweet_valence = 0
    tweet_arousal= 0
    tweet_dominance= 0
    for word in tweet_word_list:
        if word in dict_words:
            tweet_valence += float(dict_words[word][0])
            tweet_arousal += float(dict_words[word][1] )
            tweet_dominance += float(dict_words[word][2])

    print("tweet: %s", tweet)
    print("valence: %d", tweet_valence)
    print("arousal: %d", tweet_arousal)
    print("dominance: ", tweet_dominance)