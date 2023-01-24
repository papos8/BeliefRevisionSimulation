import string
import random


class States():
    def __init__(self, arg) -> None:
        if isinstance(arg, int):
            self.states = set()
            # Create the set of states randomly
            # ASCII lowercase letters are used
            if arg > 26 or arg < 1:
                print("The number of states should be between 1 and 26!")
            else:
                while not (len(self.states) == arg):
                    self.states.add(random.choice(string.ascii_lowercase))
        elif isinstance(arg, set):
            self.states = arg

    def getStates(self):
        return self.states

    def updateStates(self, newStates: set):
        self.states = newStates

    def getRandomState(self):
        randomState = random.choice(tuple(self.states))
        return randomState


class State():
    def __init__(self) -> None:
        pass
