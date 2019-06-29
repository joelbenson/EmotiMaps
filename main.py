import json
import tweepy
from TwitterStreamer import StreamListener
from stateUtilities import StateUtilities
from data import StateData
from visualizer import Visualizer

def main():
    #Access to Twitter API
    consumer_key = "TC0gBTsiLpQK43kcVWLYwysr9"
    consumer_secret = "A0GfMBG2O2IykxbaTNvqfvAUxQSmtjpNO2qaJgxd4di6mKlhWV"
    access_token = "1535031613-v8wW2PEksDe8VPhdRXPwB58iOdpwpojMKABZKlK"
    access_token_secret  = "v5LIWJLfXEzPUMni4HT2gatJMYviCdlx56nR9pIHmRj6N"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Constant Variables
    NUM_LOCATIONS = 51
    NUM_EMOTIONS = 10
    NUM_TWEETS_BETWEEN_UPDATES = 250
    ROLLOVER = 100 #number of most recent tweets used to calculate averages

    DISPLAY_TWEETS = True
    WRITE_TWEETS_TO_FILE = False

    LOCATIONS = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    EMOTIONS = ["anger", "anticipation", "disgust", "fear", "joy", "negative", "positive", "sadness", "surprise", "trust"]

    #Initialize data storage
    database = []
    for i in range(0, NUM_LOCATIONS):
        database.append(StateData(NUM_EMOTIONS, ROLLOVER))

    #Opening Stream
    stream_listener = StreamListener(database, NUM_TWEETS_BETWEEN_UPDATES, DISPLAY_TWEETS, WRITE_TWEETS_TO_FILE)
    # stream_listener.initializeEmotionRanker()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    #Choose coordinate box for tweet locations or topic
    USA = [-167.695313,16.804541,-60.996094,72.019729]
    MN = [-96.372070,44.527843,-92.482910,47.665387]

    while (True):
        #filter through the tweets of given language and location
        stream.filter(languages = ["en"], locations = USA)

        #print out emotion data
        StateData.displayData(database)

        #Visualize state data
        Visualizer.visualizeData(database, EMOTIONS, LOCATIONS)

if __name__ == "__main__":
    main()
