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

    stateArray = 0;

    #Opening Stream
    stream_listener = StreamListener(stateArray)
    # stream_listener.initializeEmotionRanker()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    #Choose coordinate box for tweet locations or topic
    USA = [-167.695313,16.804541,-60.996094,72.019729]
    MN = [-96.372070,44.527843,-92.482910,47.665387]

    stream.filter(languages = ["en"], locations = USA)



if __name__ == "__main__":
    main()
