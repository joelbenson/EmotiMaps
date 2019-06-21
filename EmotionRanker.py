import csv
import os
from operator import add

class EmotionalRanker:
    emotional_directory = {}
    emotions = ["anger", "anticipation", "disgust", "fear", "joy", "negative", "positive", "sadness", "surprise", "trust"]

    def __init__(self):
        # THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        with open('EmotionRankings.csv', newline= '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.emotional_directory.update({row['word'] : (int(row["anger"]), int(row["anticipation"]), int(row["disgust"]), int(row["fear"]), int(row["joy"]), int(row["negative"]), int(row["positive"]), int(row["sadness"]), int(row["surprise"]), int(row["trust"]))})
 
    def rank(self, tweet):
        tweet_emotions_score = [0] * 10
        tweet_word_list = tweet.split()
        for word in tweet_word_list:
            if word in self.emotional_directory:
                tweet_emotions_score = [sum(x) for x in zip(tweet_emotions_score, self.emotional_directory[word])]

        return dict(zip(self.emotions, tweet_emotions_score))
        