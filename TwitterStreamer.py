import json
import tweepy
from EmotionRanker import get_emotion_of_tweet

class StreamListener(tweepy.StreamListener):
    count = 0
    MAX_TWEETS = 50
    def writeStatusToFile(state, text):
        fileName = "StateTweets/" + state + ".txt"
        f = open(fileName,'a+')
        f.write(text + "\n")
        f.close()
    def getState(place):
        state = 'x'
        tuple = place.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state
        return "NAS"
    #Executed for each tweet
    def on_status(self, status):
        #Do not account for reply threads
        if not(status.text[0] == '@'):
            #print to command line
            print(status.text)
            #get state location of tweet
            state = StreamListener.getState(status.place.full_name)
            #Write tweet to correct state file and
            #don't break if tweet contains emoji
            try:
                StreamListener.writeStatusToFile(state, status.text)
            except:
                print("emoji tweet")
            #get dictionary of emotions from the tweet
            #dict emotions = get_emotion_of_tweet(status.text)
            #print out the emotions of the tweet_word_list
            #for x, y in dict.items():
            #    print(x, y)
            if (StreamListener.count > StreamListener.MAX_TWEETS):
                return False
            print(state)
            print(" ")
    def on_error(self, status_code):
        if status_code == 420:
            return False
