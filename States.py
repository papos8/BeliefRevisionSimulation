import string
import random


class States():
    def __init__(self, numberOfStates=None) -> None:
        if numberOfStates:
            self.states = set()
            # Create the set of states randomly
            # ASCII lowercase letters are used
            if numberOfStates > 26 or numberOfStates < 1:
                print("The number of states should be between 0 and 26!")
            else:
                while not (len(self.states) == numberOfStates):
                    self.states.add(random.choice(string.ascii_lowercase))

    def getStates(self):
        return self.states

    def getRandomState(self):
        randomState = random.choice(tuple(self.states))
        return randomState


class State():
    def __init__(self) -> None:
        pass
