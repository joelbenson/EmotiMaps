import json
import tweepy
from EmotionRanker import get_emotion_of_tweet

class StreamListener(tweepy.StreamListener):
    def writeStatusToFile(state, text):
        fileName = state + ".txt"
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
    def on_status(self, status):
        if not(status.text[0] == '@'):
            print(status.text)
            state = StreamListener.getState(status.place.full_name)
            try:
                StreamListener.writeStatusToFile(state, status.text)
            except:
                print("emoji tweet")
            print(state)
            print(" ")
    def on_error(self, status_code):
        if status_code == 420:
            return False
