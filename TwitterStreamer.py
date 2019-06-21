import json
import tweepy
from emoji import UNICODE_EMOJI
import collections

def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)

def most_c(s):
    return (collections.Counter(s).most_common(4))

consumer_key = "TC0gBTsiLpQK43kcVWLYwysr9"
consumer_secret = "A0GfMBG2O2IykxbaTNvqfvAUxQSmtjpNO2qaJgxd4di6mKlhWV"

access_token = "1535031613-v8wW2PEksDe8VPhdRXPwB58iOdpwpojMKABZKlK"
access_token_secret  = "v5LIWJLfXEzPUMni4HT2gatJMYviCdlx56nR9pIHmRj6N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    emoji1 = "U+1F600"
    
    def writeStatusToFile(state, text):
        fileName = state + ".txt"
        f = open(fileName,'a+')
        f.write(text + "\n -------------------------------- \n")
        f.close()
    
#    def countEmojis(state):
#        fileName = state + ".txt"
#        f = open(fileName,'a+')
#        for i in
#            f.read()
#        f.close()
    def addEmojis(emojiList):
        fileName = "countEmoji.txt"
        f = open(fileName,'a+')
        array_length = len(emojiList)
        for i in range(array_length):
            f.write(emojiList[i])
        f.close()

        fileName = "testEmoji.txt"
        f = open(fileName,'a+')
        s = f.read()
        s = "🏀🏀🏀🏀😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆🙄😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂💣💣"
        mc = most_c(s)
        print(mc)

    def getState(place):
        state = 'x'
        tuple = place.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state;
        return "NAS"
    
    def on_status(self, status):
        emojiList = ['']
        if not(status.text[0] == '@'):
            text = status.text
            state = StreamListener.getState(status.place.full_name)
            StreamListener.writeStatusToFile(state, status.text)
            
#            fileName = "emoji-data.txt"
#            f = open(fileName, 'r')
#            f.read()
            splitText = text.split()

            for i in splitText:
                if (is_emoji(i)):
                    emojiList.append(i)
                    #print(i)
            StreamListener.addEmojis(emojiList)
#            f.close()
#            print(text)
#            print(state)
#            print(" "),.csm, m,,mm,zmZX kjjkb.

    def on_error(self, status_code):
        if status_code == 420:
            return False


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(locations=[-123.750000,28.304381,-67.675781,48.806863])

#fileName = "testEmoji.txt"
#fileName = "countEmoji.txt"
#f = open(fileName,'a+')
#s = f.read()
#mc = most_common(s)
#print(mc)

