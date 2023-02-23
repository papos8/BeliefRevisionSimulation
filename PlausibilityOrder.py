from turtle import st
import States
from itertools import permutations
import random


class PlausibilityOrder():
    def __init__(self, *arg) -> None:
        if len(arg) == 1:
            self.order = dict()
            # worldsRelation dictionary holds states as keys
            # and lists of states as values
            # For a key the value list contains all the states
            # that are less plausible than the key
            # Use this so we can compute the set of most plausible worlds
            self.worldsRelation = dict()
            for i in range(len(arg[0].getStates())):
                self.order.update({i: []})
            for state in arg[0].getStates():
                key = random.choice(
                    [i for i in range(len(arg[0].getStates()))])
                self.order[key].append(state)
                self.worldsRelation.update({state: []})
            # Create worlds relation
            for i in range(len(arg[0].getStates())-2, -1, -1):
                for state in self.order[i]:
                    self.worldsRelation[state].append(
                        [helperState for i in range(i+1, len(arg[0].getStates())) for helperState in self.order[i] if helperState != state])
                    helperList = self.worldsRelation[state]
                    self.worldsRelation[state] = [
                        element for anotherList in helperList for element in anotherList]
            # Create set of most plausible worlds
            maxLen = 0
            self.mostPlausibleWorlds = set()
            for key in self.worldsRelation.keys():
                maxLen = max(maxLen, len(self.worldsRelation[key]))
            for key in self.worldsRelation.keys():
                if len(self.worldsRelation[key]) == maxLen:
                    self.mostPlausibleWorlds.add(key)
        elif len(arg) == 2 and arg[0] == "Custom":
            print("Create plausibility order for worlds: " +
                  (', ').join(str(s) for s in arg[1].getStates()))
            self.worldsRelation = dict()
            self.mostPlausibleWorlds = set()
            for state in arg[1].getStates():
                self.worldsRelation.update({state: set()})
            for key in arg[1].getStates():
                numberOfWorlds = int(
                    input("How many worlds are less plausible than " + key + ": "))
                for j in range(numberOfWorlds):
                    world = input("Enter the name of the wolrd: ")
                    self.worldsRelation[key].add(world)

            maxLen = 0
            for key in self.worldsRelation.keys():  # Find most plausible worlds for both positive and negative cases
                maxLen = max(maxLen, len(self.worldsRelation[key]))
            for key in self.worldsRelation.keys():
                if len(self.worldsRelation[key]) == maxLen:
                    self.mostPlausibleWorlds.add(key)
            self.order = self.worldsRelation
        elif len(arg) == 3:
            self.order = arg[0]
            self.worldsRelation = arg[1]
            self.mostPlausibleWorlds = arg[2]

    def getOrder(self):
        return self.order

    def getWorldsRelation(self):
        return self.worldsRelation

    def updateOrder(self, newOrder):
        self.order = newOrder

    def getMostPlausibleWorlds(self):
        return self.mostPlausibleWorlds

    def updateMostPlausibleWorlds(self, newMostPlausibleWorlds):
        self.mostPlausibleWorlds = newMostPlausibleWorlds

    def updateWorldsRelation(self, newWorldsRelation):
        self.worldsRelation = newWorldsRelation

    def swapElements(self, element1, element2):
        self.order[self.order.index(element1)], self.order[self.order.index(
            element2)] = self.order[self.order.index(element2)], self.order[self.order.index(element1)]
