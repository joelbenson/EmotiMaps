import json
import tweepy
from TwitterStreamer import StreamListener

def main():
    #Access to Twitter API
    consumer_key = "TC0gBTsiLpQK43kcVWLYwysr9"
    consumer_secret = "A0GfMBG2O2IykxbaTNvqfvAUxQSmtjpNO2qaJgxd4di6mKlhWV"
    access_token = "1535031613-v8wW2PEksDe8VPhdRXPwB58iOdpwpojMKABZKlK"
    access_token_secret  = "v5LIWJLfXEzPUMni4HT2gatJMYviCdlx56nR9pIHmRj6N"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Opening Stream
    stream_listener = StreamListener()
    # stream_listener.initializeEmotionRanker()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    #Choose coordinate box for tweet locations
    stream.filter(locations=[-167.695313,16.804541,-60.996094,72.019729])

    #with open("CA.txt", "r") as f:
    #    for line in f:
    #        get_emotion_of_tweet(line)


if __name__ == "__main__":
    main()
