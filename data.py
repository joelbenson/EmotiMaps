import numpy as np

class EmotionalData():
    def __init__(self, NUM_LOCATIONS):
        self.data = np.zeros((NUM_LOCATIONS,), dtype = StateData)

class StateData():
    def __init__(self, NUM_EMOTIONS = 10, ROLLOVER = 10):
        self.stateData = np.zeros((NUM_EMOTIONS, ROLLOVER))
