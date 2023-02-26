from ast import arg
from http.client import ImproperConnectionState
import numbers
from os import stat_result
from tkinter import N
import string
import random
from tokenize import single_quoted
import States
import Valuation
from itertools import chain, combinations, count


class Observables():
    # Initiate observables based on the states
    # Randomly create propositions and their negation
    def __init__(self, *arg) -> None:
        if len(arg)==1 and isinstance(arg[0], dict):
            self.observables = arg[0]
        elif len(arg)==1 and arg[0] == "Custom":
            numberOfObservables = int(
                input("What is the number of observables? "))
            observables = dict()
            for i in range(numberOfObservables):
                obs = input("Enter the name of the proposition: ")
                observables.update({obs: set()})
            for key in set(observables.keys()):
                numberOfWorlds = int(
                    input("In how many worlds is proposition " + str(key) + " true? "))
                for i in range(numberOfWorlds):
                    world = input("Enter the world: ")
                    observables[key].add(world)
            self.observables = observables
        elif len(arg)==1 and not (isinstance(arg[0], dict)):
            self.observables = dict()
            worldSet = set()
            counter = 0
            while True:
                for proposition in string.ascii_uppercase:
                    setOfWorlds = random.choice(tuple(self.powerset(arg[0])))
                    self.observables.update(
                        {str(proposition): set(setOfWorlds)})
                    self.observables.update(
                        {str("~" + proposition): arg[0].getStates()-set(setOfWorlds)})
                    counter += 2
                    
                    if counter > 9:
                        break
                if counter > 5:
                    break
            # Exchange keys, values to make values of dict a set
            helper = {tuple(v): k for k, v in self.observables.items()}
            self.observables = {v: set(k) for k, v in helper.items()}
        elif len(arg) == 2 and isinstance(arg[0],int):
            if arg[0] <= 2*(len(arg[1].getStates())):
                self.observables = dict()
                worldSet = set()
                counter = 0
                while counter <=arg[0]:
                    for proposition in string.ascii_uppercase:
                        obsChecker = False
                        setOfWorlds = random.choice(tuple(self.powerset(arg[1])))
                        # Check for two propositions with the same value
                        for key in self.observables.keys():
                            if self.observables[key] == set(setOfWorlds) or self.observables[key]==arg[1].getStates()-set(setOfWorlds):
                                obsChecker = True
                        if obsChecker:
                            continue
                        else:
                            self.observables.update(
                                {str(proposition): set(setOfWorlds)})
                            self.observables.update(
                                {str("~" + proposition): arg[1].getStates()-set(setOfWorlds)})    
                            counter += 2
                            
                        if counter > arg[0]:
                            break
                # Exchange keys, values to make values of dict a set
                helper = {tuple(v): k for k, v in self.observables.items()}
                self.observables = {v: set(k) for k, v in helper.items()}
            else:
                self.observables = dict()
                worldSet = set()
                counter = 0
                while counter <= 2*(len(arg[1].getStates())):
                    for proposition in string.ascii_uppercase:
                        obsChecker = False
                        setOfWorlds = random.choice(tuple(self.powerset(arg[1])))
                        # Check for two propositions with the same value
                        for key in self.observables.keys():
                            if self.observables[key] == set(setOfWorlds) or self.observables[key]==arg[1].getStates()-set(setOfWorlds):
                                obsChecker = True
                        if obsChecker:
                            continue
                        else:
                            self.observables.update(
                                {str(proposition): set(setOfWorlds)})
                            self.observables.update(
                                {str("~" + proposition): arg[1].getStates()-set(setOfWorlds)})    
                            counter += 2
                            
                        if counter > 2*(len(arg[1].getStates())):
                            break
                # Exchange keys, values to make values of dict a set
                helper = {tuple(v): k for k, v in self.observables.items()}
                self.observables = {v: set(k) for k, v in helper.items()}

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
