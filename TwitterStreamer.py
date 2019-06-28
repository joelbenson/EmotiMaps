import json
import tweepy
import keyboard
from EmotionRanker import EmotionalRanker
from stateUtilities import StateUtilities
from statusUtilities import StatusUtilities
from data import StateData

class StreamListener(tweepy.StreamListener):

    def __init__(self, database, maxTweets, api=None):
        self.api = api or tweepy.API()
        self.count = 0
        self.MAX_TWEETS = maxTweets
        self.emotionalRanker = EmotionalRanker()
        self.database = database

    def on_status(self, status):
        #Do not account for reply threads or retweets
        if StatusUtilities.statusConditionsHold(status):
            #get state location of tweet
            state = StateUtilities.getState(status.place.full_name, status.user.location)
            #Write tweet to correct state file
            StatusUtilities.writeStatusToFile(state, status)
            #get dictionary of emotions from the tweet
            emotions = self.emotionalRanker.rank(status.text)
            #store emotions in data object
            StateData.store(self.database[StateUtilities.getStateIndex(state)], emotions)
            #print out the emotions of the tweet_word_list
            if (self.count > self.MAX_TWEETS):
                return False
            self.count = self.count + 1
            print(status.place.full_name)
            print(" ")

    def on_error(self, status_code):
        if status_code == 420:
            return False
