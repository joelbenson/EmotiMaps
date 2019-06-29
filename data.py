import numpy as np
from EmotionRanker import EmotionalRanker
from stateUtilities import StateUtilities

class StateData():
    def __init__(self, NUM_EMOTIONS, ROLLOVER):
        self.data = np.zeros((NUM_EMOTIONS, ROLLOVER))
        self.indexer = 0
        self.numEmotions = NUM_EMOTIONS
        self.rollover = ROLLOVER
        self.statusCount = 0

    def store(state, emotions):
        for emotion, value in emotions.items():
            state.data[EmotionalRanker.getEmotionIndex(emotion)][state.indexer] = value
        state.indexer = (state.indexer + 1) % state.rollover
        state.statusCount = state.statusCount + 1

    def getAverageEmotions(stateData):
        averages = []
        observationCount = min(stateData.statusCount, stateData.rollover)
        for emotion in range(0, stateData.numEmotions):
            averages.append(np.sum(stateData.data[emotion]/observationCount))

        return averages

    def getEmotionData(database, emotion):
        emotionIndex = EmotionalRanker.getEmotionIndex(emotion)
        emotionRankings = []
        for stateData in database:
            if stateData.statusCount > 0:
                emotionRankings.append(StateData.getAverageEmotions(stateData)[emotionIndex])
            else:
                emotionRankings.append(0)
        return emotionRankings

    def displayData(database):
        locationCount = 0
        for stateData in database:
            averages = StateData.getAverageEmotions(stateData)
            averages = ['%.2f'% elem for elem in averages]
            print("State: " + StateUtilities.getStateFromIndex(locationCount))
            locationCount = locationCount+1
            print("Status Count: " + str(stateData.statusCount))
            print("Averages: ")
            print(averages)
            print("")
