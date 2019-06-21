import json
import tweepy
from EmotionRanker import EmotionalRanker

class StreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or tweepy.API()
        self.count = 0
        self.MAX_TWEETS = 50
        self.emotionalRanker = EmotionalRanker()
    def initializeEmotionRanker():
        self.emotionalRanker = EmotionalRanker()
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
            emotions = self.emotionalRanker.rank(status.text)
            #print out the emotions of the tweet_word_list
            for x, y in emotions.items():
                print(x, y)
            if (self.count > self.MAX_TWEETS):
                return False
            print(state)
            print(" ")
    def on_error(self, status_code):
        if status_code == 420:
            return False
