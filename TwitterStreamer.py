import json
import tweepy

consumer_key = "TC0gBTsiLpQK43kcVWLYwysr9"
consumer_secret = "A0GfMBG2O2IykxbaTNvqfvAUxQSmtjpNO2qaJgxd4di6mKlhWV"

access_token = "1535031613-v8wW2PEksDe8VPhdRXPwB58iOdpwpojMKABZKlK"
access_token_secret  = "v5LIWJLfXEzPUMni4HT2gatJMYviCdlx56nR9pIHmRj6N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):

        if not(status.text[0] == '@'):
            print(status.text)
            print(status.place.full_name)
            print(" ")
    def on_error(self, status_code):
        if status_code == 420:
            return False;

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(locations=[-96.899414,43.612217,-91.933594,47.694974])
