import string
import random


class States():
    def __init__(self, numberOfStates) -> None:
        self.states = set()
        if numberOfStates > 26 or numberOfStates < 1:
            print("The number of states should be between 0 and 26!")
        else:
            while not (len(self.states) == numberOfStates):
                self.states.add(random.choice(string.ascii_lowercase))

    def getStates(self):
        return self.states
