import json
import tweepy
from EmotionRanker import get_emotion_of_tweet

consumer_key = "TC0gBTsiLpQK43kcVWLYwysr9"
consumer_secret = "A0GfMBG2O2IykxbaTNvqfvAUxQSmtjpNO2qaJgxd4di6mKlhWV"

access_token = "1535031613-v8wW2PEksDe8VPhdRXPwB58iOdpwpojMKABZKlK"
access_token_secret  = "v5LIWJLfXEzPUMni4HT2gatJMYviCdlx56nR9pIHmRj6N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def writeStatusToFile(state, text):
        fileName = state + ".txt"
        f = open(fileName,'a+')
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


# stream_listener = StreamListener()
# stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
# stream.filter(locations=[-167.695313,16.804541,-60.996094,72.019729])

with open("CA.txt", "r") as f:
    for line in f: 
        get_emotion_of_tweet(line)


