from ast import arg
from http.client import ImproperConnectionState
from tkinter import N
import string
import random
import States


class Observables():
    def __init__(self) -> None:
        self.observables = dict()
        worldSet = set()
        for proposition in string.ascii_uppercase:
            self.observables.update({str(proposition): worldSet})
            self.observables.update({str("~" + proposition): worldSet})

    def getObservables(self):
        return self.observables

    def getSingleObservable(self):
        return self.observables[random.choice(tuple(string.ascii_uppercase))]

    def isNegation(self, proposition):
        return True if proposition[0] == "~" else False

    def getNegation(self, proposition):
        return str("~" + proposition)

    def createObservables(self, states: States):
        for proposition in self.observables:
            for state in states.getStates():
                if (not (self.isNegation(proposition))):
                    if (not (state in self.observables[self.getNegation(proposition)])):
                        self.observables[proposition].add(state)
                elif (self.isNegation(proposition)):
                    if (not (state in self.observables[proposition[1]])):
                        self.observables[self.getNegation(
                            proposition)].add(state)

        return self.observables
