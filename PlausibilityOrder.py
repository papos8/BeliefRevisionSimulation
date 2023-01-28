from turtle import st
import States
from itertools import permutations
import random


class PlausibilityOrder():
    def __init__(self, arg) -> None:
        if not isinstance(arg, dict):
            self.order = dict()
            for i in range(len(arg.getStates())):
                self.order.update({i: []})
            for state in arg.getStates():
                key = random.choice([i for i in range(len(arg.getStates()))])
                self.order[key].append(state)
            self.worldsRelation = dict.fromkeys(
                list(arg.getStates()), [])
            emptyKeys = []
            print(self.order)
            print(self.worldsRelation)
            for i in range(len(arg.getStates())-1, -1, -1):
                for state in self.order[i]:
                    self.worldsRelation[state]
                    print("Worls rel")
                    print(self.worldsRelation)
                    # self.worldsRelation[state].append(
                    #   [helperState for helperState in self.order[i]])
                    helperList = self.worldsRelation[state]
                    self.worldsRelation = [
                        anotherState for anotherState in helperList]
        elif isinstance(arg, dict):
            self.order = arg

    def getOrder(self):
        return self.order

    def getWorldsRelation(self):
        return self.worldsRelation

    def updateOrder(self, newOrder):
        self.order = newOrder

    def updateWorldsRelation(self, newWorldsRelation):
        self.worldsRelation = newWorldsRelation

    def swapElements(self, element1, element2):
        self.order[self.order.index(element1)], self.order[self.order.index(
            element2)] = self.order[self.order.index(element2)], self.order[self.order.index(element1)]
