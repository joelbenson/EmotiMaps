from stateUtilities import StateUtilities

class StatusUtilities():
        def writeStatusToFile(state, text):
            try:
                fileName = "StateTweets/" + state + ".txt"
                f = open(fileName,'a+')
                f.write(text + "\n")
                f.close()
            except:
                print("Emoji Tweet")

        def statusConditionsHold(status):
            notRetweet = not (status.text[0] == 'R') and not (status.text[1] =='T')
            notReply = not (status.text[0] == '@')
            try:
                validLocation = len(StateUtilities.getState(status.place.full_name, status.user.location)) == 2
            except:
                validLocation = False
            return (notRetweet and notReply and validLocation)
