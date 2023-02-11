import string
import Obsevables
import States
import random


class DataSequence():
    def __init__(self) -> None:
        self.length = int(input("Provide the sequence's length: "))
        self.dataSequenceDict = dict()
        self.dataSequence = []
        for i in range(self.length):
            key = input("Provide the name of the observable proposition: ")
            self.dataSequence.append(key)
            worlds = set()
            setLength = int(
                input("In how many worlds is the proposition true? "))
            for i in range(setLength):
                world = input("Provide the name of the world: ")
                worlds.add(world)
            self.dataSequenceDict.update({key: worlds})

    def getDataSequenceDict(self):
        return self.dataSequenceDict

    def getDataSequence(self):
        return self.dataSequence

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
        for observable in self.observables.getObservables():
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
