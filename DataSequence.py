from itertools import permutations
import itertools
import string
from wsgiref.util import request_uri
import Obsevables
import States
import random


class DataSequence():
    def __init__(self, *arg) -> None:
        if len(arg) == 1 and arg == "Create":
            worlds = set()
            numberOfWorlds = int(input("How many possible worlds are there? "))
            for i in range(numberOfWorlds):
                world = input("Enter the name of the world: ")
                worlds.add(world)
            actualWorld = input("What is the actual world? ")
            if actualWorld not in worlds:
                worlds.add(actualWorld)
            self.length = int(input("Provide the sequence's length: "))
            self.dataSequenceDict = dict()
            self.dataSequence = []

            for i in range(self.length):
                key = input("Provide the name of the observable proposition: ")
                self.dataSequence.append(key)
                setLength = int(
                    input("In how many worlds is the proposition true? "))
                setOfworlds = set()
                for i in range(setLength):
                    world = input("Provide the name of the world: ")
                    setOfworlds.add(world)
                self.dataSequenceDict.update({key: setOfworlds})
            for proposition in self.dataSequence:
                self.dataSequenceDict.update(
                    {self.getNegation(proposition): worlds.difference(self.dataSequenceDict[proposition])})
            self.states = States.States(set(worlds))
            self.observables = Obsevables.Observables(self.dataSequenceDict)
        else:
            # Pass states as first argument and obs as second
            self.states = arg[0]
            self.observables = arg[1]
            self.dataSequence = []
            positiveProps = []
            for key in self.observables.getObservables().keys():
                if self.states.getActualWorld() in self.observables.getObservables()[key]:
                    positiveProps.append(key)
            lengthOfSequence = int(
                input("Provide the length of the data sequence. It should be greater or equal than " +
                      str(len(positiveProps)) + ": "))

            if lengthOfSequence == len(positiveProps):
                permutations = list(itertools.permutations(
                    positiveProps, lengthOfSequence))
                index = random.randint(1, len(permutations))
                self.dataSequence = permutations[index]
            elif lengthOfSequence > len(positiveProps):
                permutations = list(itertools.permutations(
                    positiveProps, len(positiveProps)))
                index = random.randint(1, len(permutations))
                helperData = permutations[index]
                for element in helperData:
                    self.dataSequence.append(element)
                for i in range(len(helperData), lengthOfSequence):
                    randomElement = random.choice(positiveProps)
                    self.dataSequence.append(randomElement)
            else:
                raise Exception(
                    "The length of the data sequence should be greater or equal than the number of observables true in the actual world!")

    def getDataSequenceDict(self):
        return self.dataSequenceDict

    def getDataSequence(self):
        return self.dataSequence

    def getStates(self):
        return self.states

    def getObservables(self):
        return self.observables

    # Check soundness of sequence
    def isSound(self, state: string):
        flag = True
        # Check if state is in the set of worlds that makes
        # each observable true
        for observable in self.dataSequence:
            if state not in self.dataSequence[observable]:
                flag = False
                break
        return flag

    # Check completeness of sequence
    def isComplete(self, state: string):
        flag = True
        # Check that if the state is in a observable,
        # then the observable is in the data sequence
        for observable in self.observables.getObservables().keys():
            if state in self.observables.getObservables()[observable] and observable not in self.dataSequence:
                flag = False
                break
        return flag

    # Function for creating custom data sequence
    def createRanddomDataSequence(self, observables, states, length):
        self.dataSequenceDict = dict()
        self.length = length
        for i in range(length):
            key = random.choice(
                tuple(observables.getObservables()))
            self.dataSequenceDict.update(
                {key: observables.getObservables()[key]})
        return self.dataSequenceDict

    def getNegation(self, proposition: string):
        if len(proposition) == 1:
            return str("~" + proposition)
        else:
            return proposition[1]
