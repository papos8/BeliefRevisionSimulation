from ast import arg
from http.client import ImproperConnectionState
from os import stat_result
from tkinter import N
import string
import random
import States
import Valuation


class Observables():
    # Initiate observables based on the states
    # Randomly create propositions and their negation
    def __init__(self, states: States) -> None:
        self.observables = dict()
        worldSet = set()
        val = Valuation.Valuation()

        for proposition in string.ascii_uppercase:
            setOfWorlds = random.choice(tuple(val.powerset(states)))
            self.observables.update({str(proposition): set(setOfWorlds)})
            self.observables.update(
                {str("~" + proposition): states.getStates()-set(setOfWorlds)})

        # exchange keys, values
        helper = {tuple(v): k for k, v in self.observables.items()}
        self.observables = {v: set(k) for k, v in helper.items()}

    def getObservables(self):
        return self.observables

    def getSingleObservable(self):
        return self.observables[random.choice(tuple(string.ascii_uppercase))]

    def isNegation(self, proposition):
        return True if proposition[0] == "~" else False

    def getNegation(self, proposition):
        return str("~" + proposition)
