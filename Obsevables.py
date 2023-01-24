from ast import arg
from http.client import ImproperConnectionState
from os import stat_result
from tkinter import N
import string
import random
from tokenize import single_quoted
import States
import Valuation
from itertools import chain, combinations


class Observables():
    # Initiate observables based on the states
    # Randomly create propositions and their negation
    def __init__(self, arg) -> None:
        if not (isinstance(arg, dict)):
            self.observables = dict()
            worldSet = set()

            for proposition in string.ascii_uppercase:
                setOfWorlds = random.choice(tuple(self.powerset(arg)))
                self.observables.update({str(proposition): set(setOfWorlds)})
                self.observables.update(
                    {str("~" + proposition): arg.getStates()-set(setOfWorlds)})

            # Exchange keys, values to make values of dict a set
            helper = {tuple(v): k for k, v in self.observables.items()}
            self.observables = {v: set(k) for k, v in helper.items()}
        elif isinstance(arg, dict):
            self.observables = arg

    def getObservables(self):
        return self.observables

    def updateObservables(self, newObservables: dict):
        self.observables = newObservables

    def getSingleObservable(self):
        key = random.choice(tuple(self.observables.keys()))
        singleObs = dict()
        singleObs.update({key: frozenset(self.observables[key])})
        # Exchange keys, values to make values of dict a set
        helper = {tuple(v): k for k, v in singleObs.items()}
        singleObs = {v: set(k) for k, v in helper.items()}
        return singleObs

    def isNegation(self, proposition):
        return True if proposition[0] == "~" else False

    def getNegation(self, proposition):
        return str("~" + proposition)

    # Create the powerset of all the states to be used
    # for observables, as O is subset of P(S)
    def powerset(self, states: States):
        s = list(states.getStates())
        powerset = set(chain.from_iterable(combinations(s, r)
                       for r in range(len(s)+1)))

        newPowerSet = set()
        finalPowerSet = set()
        for i in powerset:
            newPowerSet.add(frozenset(self.tupleToSet(i)))

        for i in newPowerSet:
            finalPowerSet.add(frozenset(i))

        return finalPowerSet

    def tupleToSet(self, tuple: tuple):
        newSet = set()
        for i in tuple:
            newSet.add(i)
        return newSet
