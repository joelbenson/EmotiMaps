from stateUtilities import StateUtilities

class StatusUtilities():
        def writeStatusToFile(state, status):
            print(status.text)
            print(status.id_str)
            print(status.created_at)
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
                validLocation = len(StateUtilities.getState(status.place.full_name, status.user.location)) == 2
            except:
                validLocation = False
            return (notRetweet and notReply and validLocation)
