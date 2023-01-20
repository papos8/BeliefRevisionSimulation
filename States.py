import string
import random


class States():
    def __init__(self, numberOfStates):
        self.states = set()
        while not (len(self.states) == numberOfStates):
            self.states.add(random.choice(string.ascii_lowercase))

    def getStates(self):
        return self.states
