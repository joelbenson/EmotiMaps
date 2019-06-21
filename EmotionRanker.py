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
    

    # print("tweet: ", tweet, end='')
    # for i in range(0,len(emotions)):
    #     print(str(emotions[i]) + ":" + str(tweet_emotions_score[i]), end=' ')


# def get_emotion_of_tweet(tweet):
#     THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

#     emotions = ["anger", "anticipation", "disgust", "fear", "joy", "negative", "positive", "sadness", "surprise", "trust"]
    
#     # populate word_emotions_dictionary
#     with open('EmotionRankings.csv', newline= '') as csvfile:
#         reader = csv.DictReader(csvfile)
#         word_emotions_dictionary = {row['word'] : (int(row["anger"]), int(row["anticipation"]), int(row["disgust"]), int(row["fear"]), int(row["joy"]), int(row["negative"]), int(row["positive"]), int(row["sadness"]), int(row["surprise"]), int(row["trust"])) for row in reader}

#     # add the emotional score of each word in tweet to overall tweet_emotions_score
#     tweet_emotions_score = [0] * 10
#     tweet_word_list = tweet.split()
#     for word in tweet_word_list:
#         if word in word_emotions_dictionary:
#             tweet_emotions_score = [sum(x) for x in zip(tweet_emotions_score, word_emotions_dictionary[word])]

#     print("tweet: ", tweet, end='')
#     for i in range(0,len(emotions)):
#         print(str(emotions[i]) + ":" + str(tweet_emotions_score[i]), end=' ')
#     print()
#     print()
