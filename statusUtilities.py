from stateUtilities import StateUtilities

class StatusUtilities():
        def displayStatus(status):
            try:
                print(status.text)
                print(status.place.full_name)
                print(status.created_at)
            except:
                return
        def writeStatusToFile(state, status):
            try:
                fileName = "StateTweets/" + state + ".txt"
                f = open(fileName,'a+')
                f.write(status.text + "\n")
                f.close()
            except:
                print("Emoji Tweet")

        def statusConditionsHold(status):
            notRetweet = not (status.text[0] == 'R') and not (status.text[1] =='T')
            notReply = not (status.text[0] == '@')
            try:
                validLocation = StateUtilities.checkValidState(StateUtilities.getState(status.place.full_name, status.user.location))
            except:
                validLocation = False
            return (notRetweet and notReply and validLocation)
