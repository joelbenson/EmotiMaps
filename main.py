import json
import tweepy
from TwitterStreamer import StreamListener
from data import StateData

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
    NUM_TWEETS_BETWEEN_UPDATES = 10
    ROLLOVER = 30


    #Initialize data storage
    database = []
    for i in range(0, NUM_LOCATIONS):
        database.append(StateData(NUM_EMOTIONS, ROLLOVER))

    #Opening Stream
    stream_listener = StreamListener(database, NUM_TWEETS_BETWEEN_UPDATES)
    # stream_listener.initializeEmotionRanker()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    #Choose coordinate box for tweet locations or topic
    USA = [-167.695313,16.804541,-60.996094,72.019729]
    MN = [-96.372070,44.527843,-92.482910,47.665387]

    stream.filter(languages = ["en"], locations = USA)

    #print out emotion data
    i = 0
    for stateData in database:
        print("State: " + str(i))
        i = i+1
        print("Status Count: " + str(stateData.statusCount))
        #print(stateData.data[0:NUM_EMOTIONS])
        print("Average: " + str(StateData.getAverageEmotions(stateData)))
        print("")


if __name__ == "__main__":
    main()
