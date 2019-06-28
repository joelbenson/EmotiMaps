import numpy as np
from EmotionRanker import EmotionalRanker

class StateData():
    def __init__(self, NUM_EMOTIONS, ROLLOVER):
        self.data = np.zeros((NUM_EMOTIONS, ROLLOVER))
        self.indexer = 0
        self.numEmotions = NUM_EMOTIONS
        self.rollover = ROLLOVER
        self.statusCount = 0

    def store(state, emotions):
        for emotion, value in emotions.items():
            print(emotion, value)
            state.data[EmotionalRanker.getEmotionIndex(emotion)][state.indexer] = value
        state.indexer = (state.indexer + 1) % state.rollover
        state.statusCount = state.statusCount + 1
        print("Data stored")

    def getAverageEmotions(stateData):
        averages = []
        observationCount = min(stateData.statusCount, stateData.rollover)
        for emotion in range(0, stateData.numEmotions):
            averages.append(np.sum(stateData.data[emotion]/observationCount))

        averages = ['%.2f' % elem for elem in averages]
        
        return averages
