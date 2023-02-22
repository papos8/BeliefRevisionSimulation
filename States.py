from os import stat
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
            self.actualWorld = random.sample(self.states, 1)[0]
        elif isinstance(arg, set):
            self.states = arg
            if len(arg) > 0:
                self.actualWorld = random.choice(tuple(arg))
            else:
                self.actualWorld = ""
        elif arg == "Custom":
            states = set()
            numberOfStates = int(input("How many possible worlds are there? "))
            for i in range(numberOfStates):
                state = input("Enter the name of the world: ")
                states.add(state)
            self.actualWorld = input("What is the actual world? ")
            self.states = states

    def getStates(self):
        return self.states

    def updateStates(self, newStates: set):
        self.states = newStates

    def getRandomState(self):
        randomState = random.choice(tuple(self.states))
        return randomState

    def getActualWorld(self):
        return self.actualWorld


class State():
    def __init__(self) -> None:
        pass
