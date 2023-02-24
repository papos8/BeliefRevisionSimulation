import string
from tkinter import Widget
from tkinter.tix import DirTree
from tokenize import String
from turtle import pos
from typing import Dict
from xmlrpc.client import ProtocolError
from Obsevables import Observables
from EpistemicSpace import EpistemicSpace
from PlausibilityOrder import PlausibilityOrder
import States
import math
from random import randint, random, uniform, choice, sample
import copy


class Agent():
    def __init__(self, epistemicSpace: EpistemicSpace, typeOfBias: string, typeOfAgent: string) -> None:
        self.resources = uniform(0.0, 100.0)
        self.bias = typeOfBias
        self.typeOfAgent = typeOfAgent
        if typeOfAgent == "Custom":
            self.plausibilityOrder = PlausibilityOrder(
                "Custom", epistemicSpace.states)
        else:
            self.plausibilityOrder = PlausibilityOrder(epistemicSpace.states)
        self.observables = epistemicSpace.observables
        self.timesOfIncomingInfo = dict()
        for obs in self.observables.getObservables():
            self.timesOfIncomingInfo.update({obs: 0})
        self.isInGroup = False
        self.stubbornnessDegrees = self.stubbornnessDegree(
            epistemicSpace.observables.getObservables())
        self.calledByCBConditioning = False
        self.calledByCBCLexRevision = False
        self.calledByCBMinRevision = False

    # Framing function to return a subset of
    # a proposition

    def framingFunction(self, observables: dict):
        ''' If agent is under framing bias we use the
        framing function. Otherwise, observables
        are returned without change '''
        newObservables = {}
        if self.typeOfAgent == "Custom":
            # Create custom framed observables
            for key in observables.keys():
                newObservables.update({key: set()})
            for proposition in observables.keys():
                numberOfFramedWorlds = int(
                    input("How many worlds where " + str(proposition) + " will the agent receive? "))
                for i in range(numberOfFramedWorlds):
                    world = input("Enter the name of the world: ")
                    newObservables[proposition].add(world)
            return newObservables
        else:
            for key in observables.keys():
                newObservables.update({key: set()})

            for proposition in observables:
                value = observables[proposition]
                # Here the subset is taken completely random
                # This may affect the results
                newValue = sample(value, randint(
                    0, len(observables[proposition])))
                newObservables.update({proposition: newValue})

            for key in observables.keys():
                newObservables[key] = set(newObservables[key])
            if self.bias == "Framing":
                return newObservables
            else:
                return observables

    # Function that return a dictionary of a proposition and
    # the stubbornness degree of the agent towards this
    # proposition
    def stubbornnessDegree(self, observables: dict):
        dictOfDegress = dict()
        if self.typeOfAgent == "Custom":
            for prop in set(self.observables.getObservables().keys()):
                stub = int(
                    input("What is the stubbornness degree of " + prop + ": "))
                dictOfDegress.update({prop: stub})
            return dictOfDegress
        else:
            ''' If the agent is not unbiased a random integer
            between 1 and 5 is assigned as stubbornness degree
            to every observable proposition. Otherwise, the degree
            is 1 for every observable proposition '''
            if self.bias == "Confirmation":
                if self.isInGroup == True:
                    for proposition in observables:
                        dictOfDegress.update({proposition: 0})
                    for proposition in observables:
                        if self.getNegation(proposition) in observables and dictOfDegress[self.getNegation(proposition)] > 1:
                            continue
                        else:
                            dictOfDegress[proposition] = math.ceil(
                                randint(1, 5)/self.group.adaptiveFactor)
                else:
                    for proposition in observables:
                        dictOfDegress.update({proposition: 1})
                    for proposition in observables:
                        if self.getNegation(proposition) in observables and dictOfDegress[self.getNegation(proposition)] > 1:
                            continue
                        else:
                            dictOfDegress[proposition] = randint(1, 5)
            elif self.bias == "Unbiased":
                for proposition in observables:
                    dictOfDegress.update({proposition: 1})
            return dictOfDegress

    def addedToGroup(self, group: set):
        self.group = group
        self.isInGroup = True

    # Implement conditioning based on the definitions
    def conditioning(self, epistemicSpace: EpistemicSpace, proposition: string):
        # Create new set S
        helperStates = epistemicSpace.states.getStates()
        newStates = epistemicSpace.observables.getObservables()[proposition]

        epistemicSpace.states.updateStates(
            epistemicSpace.states.getStates().intersection(newStates))

        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        # Update plaus order to have only the new states
        statesToRemove = helperStates.difference(
            epistemicSpace.states.getStates())

        for state in statesToRemove:
            for key in self.plausibilityOrder.getOrder().keys():
                if state in self.plausibilityOrder.getOrder()[key]:
                    self.plausibilityOrder.getOrder()[key].remove(state)
            for anotherState in epistemicSpace.states.getStates():
                if state in self.plausibilityOrder.getWorldsRelation()[anotherState]:
                    self.plausibilityOrder.getWorldsRelation()[
                        anotherState].remove(state)
            self.plausibilityOrder.getWorldsRelation().pop(state)
            if state in self.plausibilityOrder.getMostPlausibleWorlds():
                self.plausibilityOrder.getMostPlausibleWorlds().remove(state)
        if len(self.plausibilityOrder.getMostPlausibleWorlds()) == 0:
            maxLen = 0
            # Create the set of most plaus worlds
            newMostPlausibleWorlds = set()
            for key in self.plausibilityOrder.getWorldsRelation().keys():
                maxLen = max(maxLen, len(
                    self.plausibilityOrder.getWorldsRelation()[key]))
            for key in self.plausibilityOrder.getWorldsRelation().keys():
                if len(self.plausibilityOrder.getWorldsRelation()[key]) == maxLen:
                    newMostPlausibleWorlds.add(key)
            self.plausibilityOrder.updateMostPlausibleWorlds(
                newMostPlausibleWorlds)
            self.plausibilityOrder = PlausibilityOrder(
                self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
        newSpace = EpistemicSpace(
            epistemicSpace.states, epistemicSpace.observables)
        if self.calledByCBConditioning == True:
            if self.stubbornnessDegrees[proposition] == 1:
                if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                    self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                    self.stubbornnessDegrees[self.getNegation(proposition)] = 1
        return newSpace

    def lexRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        # Create two helper state orders
        # Posittive and negative
        positiveOrder = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():  # Initialize orders
            positiveOrder.update({key: set()})
            negativeOrder.update({key: set()})
        for state in epistemicSpace.states.getStates():  # Create orders' keys
            if state not in epistemicSpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
            if state in epistemicSpace.observables.getObservables()[proposition]:
                negativeOrder.pop(state)
        for key in positiveOrder.keys():                # Create positive order values
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        for key in negativeOrder.keys():                # Create negative order values
            negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in epistemicSpace.observables.getObservables()[proposition] and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)
        # New worldsRelation
        for positiveState in positiveOrder.keys():      # Create new worlds relation
            for negativeState in negativeOrder.keys():
                positiveOrder[positiveState].append(negativeState)
        positiveOrder.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrder)
        maxLen = 0
        # Create the set of most plaus worlds
        newMostPlausibleWorlds = set()
        for key in self.plausibilityOrder.getWorldsRelation().keys():
            maxLen = max(maxLen, len(
                self.plausibilityOrder.getWorldsRelation()[key]))
        for key in self.plausibilityOrder.getWorldsRelation().keys():
            if len(self.plausibilityOrder.getWorldsRelation()[key]) == maxLen:
                newMostPlausibleWorlds.add(key)
        self.plausibilityOrder.updateMostPlausibleWorlds(
            newMostPlausibleWorlds)
        self.plausibilityOrder.updateOrder(self.wordlsRelationToOrder(
            self.plausibilityOrder.getWorldsRelation()))
        if self.calledByCBCLexRevision == True:
            if self.stubbornnessDegrees[proposition] == 1:
                if self.timesOfIncomingInfo[proposition] > self.stubbornnessDegrees[self.getNegation(proposition)]:
                    self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                    self.stubbornnessDegrees[self.getNegation(proposition)] = 1
        return EpistemicSpace(epistemicSpace.states, newObservables)

    def minRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        worldsRelationHelper = copy.deepcopy(
            self.plausibilityOrder.getWorldsRelation())
        positiveOrder = dict()
        positiveOrderHelper = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: set()})
            positiveOrderHelper.update({key: set()})
        for state in epistemicSpace.states.getStates():          # Create keys for orders
            if state not in epistemicSpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in epistemicSpace.observables.getObservables()[proposition]:
                posPlausibleInProp.add(key)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                negativeOrder.update({key: set()})
        for key in negativeOrder.keys():                            # Create neg order
            negativeOrder[key] = worldsRelationHelper[
                key]
            for state in epistemicSpace.states.getStates():
                if state in posPlausibleInProp and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                positiveOrderHelper.pop(key)

        for key in positiveOrderHelper.keys():                      # Create posHelper order
            positiveOrderHelper[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrderHelper[key] and state not in posPlausibleInProp:
                    positiveOrderHelper[key].remove(state)
        for positiveState in positiveOrderHelper.keys():            # Add the 'negative' worlds to positive
            for negativeState in negativeOrder.keys():
                positiveOrderHelper[positiveState].append(negativeState)
            for anotherState in set(positiveOrder.keys()).difference(positiveOrderHelper.keys()):
                positiveOrderHelper[positiveState].append(anotherState)
        positiveOrderHelper.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrderHelper)
        self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
            posPlausibleInProp)
        if self.calledByCBMinRevision == True:
            if self.stubbornnessDegrees[proposition] == 1:
                if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                    self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                    self.stubbornnessDegrees[self.getNegation(
                        proposition)] = 1
        return EpistemicSpace(epistemicSpace.states, newObservables)

    def confirmationBiasedConditioning(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        self.timesOfIncomingInfo[proposition] += 1
        if self.timesOfIncomingInfo[proposition] >= self.stubbornnessDegrees[self.getNegation(proposition)]:
            self.calledByCBConditioning = True
            return self.conditioning(epistemicSpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in self.stubbornnessDegrees.keys():
                if self.stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)
            if proposition in stubbornProp:
                helperStates = set(epistemicSpace.states.getStates())
                newStates = set()
                newStates = epistemicSpace.states.getStates()

                # Create a set of worls that are in the stub props
                for observable in self.stubbornnessDegrees.keys():
                    if self.stubbornnessDegrees[observable] > 1:
                        for state in epistemicSpace.states.getStates():
                            if state in epistemicSpace.observables.getObservables()[observable]:
                                newStates = newStates.intersection(
                                    epistemicSpace.observables.getObservables()[observable])
                epistemicSpace.states.updateStates(
                    epistemicSpace.states.getStates().intersection(newStates))
                newStates = States.States(newStates)
                newObservables = dict()

                for observable in epistemicSpace.observables.getObservables():
                    newValue = epistemicSpace.observables.getObservables()[observable].intersection(
                        epistemicSpace.observables.getObservables()[proposition])
                    if len(newValue) > 0:
                        newObservables.update({observable: newValue})
                    else:
                        newObservables.update({observable: set()})
                newObservables = Observables(newObservables)
                statesToRemove = helperStates.difference(newStates.getStates())
                for state in statesToRemove:
                    for key in self.plausibilityOrder.getOrder().keys():
                        if state in self.plausibilityOrder.getOrder()[key]:
                            self.plausibilityOrder.getOrder()[
                                key].remove(state)
                    for anotherState in newStates.getStates():
                        if state in self.plausibilityOrder.getWorldsRelation()[anotherState]:
                            self.plausibilityOrder.getWorldsRelation()[
                                anotherState].remove(state)
                    self.plausibilityOrder.getWorldsRelation().pop(state)
                    if state in self.plausibilityOrder.getMostPlausibleWorlds():
                        self.plausibilityOrder.getMostPlausibleWorlds().remove(state)
                self.plausibilityOrder.updateWorldsRelation(
                    self.plausibilityOrder.getWorldsRelation())
                newPlSpace = EpistemicSpace(
                    states=newStates, observbles=newObservables)
                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1
                return newPlSpace
            else:
                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1
                return epistemicSpace

    def confirmationBiasedLexRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        print(self.timesOfIncomingInfo)
        self.timesOfIncomingInfo[proposition] += 1
        if self.timesOfIncomingInfo[proposition] >= self.stubbornnessDegrees[self.getNegation(proposition)]:
            self.calledByCBCLexRevision = True
            return self.lexRevision(epistemicSpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in self.stubbornnessDegrees.keys():
                if self.stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)

            if proposition in stubbornProp:
                # Orders that will help creating the new world relation
                # A world relation is consider an order
                positiveOrder = dict()
                negativeOrder = dict()
                intersectionSet = stubbornProp.intersection(
                    epistemicSpace.observables.getObservables()[proposition])
                negativeIntersectionSet = stubbornProp.intersection(
                    epistemicSpace.observables.getObservables()[self.getNegation(proposition)])
                for key in epistemicSpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                for state in epistemicSpace.states.getStates():  # Create orders' keys - Delete the unwanted
                    if state not in intersectionSet:
                        positiveOrder.pop(state)
                    if state not in negativeIntersectionSet:
                        negativeOrder.pop(state)
                for key in positiveOrder.keys():                # Create positive order values
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state not in intersectionSet and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                for key in negativeOrder.keys():                # Create negative order values
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state not in epistemicSpace.observables.getObservables()[proposition] and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                # New worldsRelation
                for positiveState in positiveOrder.keys():      # Create new worlds relation
                    for negativeState in negativeOrder.keys():
                        positiveOrder[positiveState].add(negativeState)
                positiveOrder.update(negativeOrder)
                self.plausibilityOrder.updateWorldsRelation(positiveOrder)
                maxLen = 0
                # Create the set of most plaus worlds
                newMostPlausibleWorlds = set()
                for key in self.plausibilityOrder.getWorldsRelation().keys():
                    maxLen = max(maxLen, len(
                        self.plausibilityOrder.getWorldsRelation()[key]))
                for key in self.plausibilityOrder.getWorldsRelation().keys():
                    if len(self.plausibilityOrder.getWorldsRelation()[key]) == maxLen:
                        newMostPlausibleWorlds.add(key)
                self.plausibilityOrder.updateMostPlausibleWorlds(
                    newMostPlausibleWorlds)
                self.plausibilityOrder.updateOrder(self.wordlsRelationToOrder(
                    self.plausibilityOrder.getWorldsRelation()))

                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1
                return EpistemicSpace(epistemicSpace.states, epistemicSpace.observables)
            else:
                # Create new orders to help with the new worlds relation
                # The new orders will hold only the stubborn prop as the incoming
                # Information is a contradiction and the agent revise only the stubborn env
                positiveOrder = dict()
                negativeOrder = dict()
                for key in epistemicSpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                for state in epistemicSpace.states.getStates():  # Create orders' keys - Delete the unwanted
                    if state not in self.getIntersection(stubbornProp):
                        positiveOrder.pop(state)
                    if state in self.getIntersection(stubbornProp):
                        negativeOrder.pop(state)
                for key in positiveOrder.keys():                # Create positive order values
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                for key in negativeOrder.keys():                # Create negative order values
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state in self.getIntersection(stubbornProp) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                # New worldsRelation
                for positiveState in positiveOrder.keys():      # Create new worlds relation
                    for negativeState in negativeOrder.keys():
                        positiveOrder[positiveState].add(negativeState)
                positiveOrder.update(negativeOrder)

                self.plausibilityOrder.updateWorldsRelation(positiveOrder)
                maxLen = 0
                # Create the set of most plaus worlds
                newMostPlausibleWorlds = set()
                for key in self.plausibilityOrder.getWorldsRelation().keys():
                    maxLen = max(maxLen, len(
                        self.plausibilityOrder.getWorldsRelation()[key]))
                for key in self.plausibilityOrder.getWorldsRelation().keys():
                    if len(self.plausibilityOrder.getWorldsRelation()[key]) == maxLen:
                        newMostPlausibleWorlds.add(key)
                self.plausibilityOrder.updateMostPlausibleWorlds(
                    newMostPlausibleWorlds)
                self.plausibilityOrder.updateOrder(self.wordlsRelationToOrder(
                    self.plausibilityOrder.getWorldsRelation()))

                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1
                return EpistemicSpace(epistemicSpace.states, newObservables)

    def confirmationBiasedMinRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())

        self.timesOfIncomingInfo[proposition] += 1
        if self.timesOfIncomingInfo[proposition] >= self.stubbornnessDegrees[self.getNegation(proposition)]:
            self.calledByCBMinRevision = True
            return self.minRevision(epistemicSpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in self.stubbornnessDegrees.keys():
                if self.stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)

            if proposition in stubbornProp:
                positiveOrder = dict()
                negativeOrder = dict()
                postiveHelperOrder = dict()
                for key in epistemicSpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: set()})
                    postiveHelperOrder.update({key: set()})
                for state in epistemicSpace.states.getStates():          # Create keys for orders
                    # For the sake of completeness,
                    # As proposition is already there
                    if state not in self.getIntersection(stubbornProp).intersection(self.observables.getObservables()[proposition]):
                        positiveOrder.pop(state)
                for key in positiveOrder.keys():                             # Create pos order
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp).intersection(self.observables.getObservables()[proposition]) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
                maxLen = 0
                for key in positiveOrder.keys():
                    maxLen = max(maxLen, len(positiveOrder[key]))
                for key in positiveOrder.keys():
                    if len(positiveOrder[key]) == maxLen and key in self.getIntersection(stubbornProp).intersection(self.observables.getObservables()[proposition]):
                        posPlausibleInProp.add(key)
                for key in epistemicSpace.states.getStates():
                    if key not in posPlausibleInProp:
                        postiveHelperOrder.pop(key)

                for state in epistemicSpace.states.getStates():
                    if state not in posPlausibleInProp:
                        negativeOrder.update({state: set()})
                for key in negativeOrder.keys():                            # Create neg order
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state in self.getIntersection(stubbornProp).intersection(posPlausibleInProp) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                for key in postiveHelperOrder.keys():                      # Create posHelper order
                    postiveHelperOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state in self.getIntersection(stubbornProp).intersection(self.observables.getObservables()[proposition]) and state in postiveHelperOrder[key] and state not in posPlausibleInProp:
                            postiveHelperOrder[key].remove(state)

                for positiveState in postiveHelperOrder.keys():            # Add the 'negative' worlds to positive
                    for negativeState in negativeOrder.keys():
                        postiveHelperOrder[positiveState].append(negativeState)
                    for anotherState in set(positiveOrder.keys()).difference(postiveHelperOrder.keys()):
                        postiveHelperOrder[positiveState].append(anotherState)
                postiveHelperOrder.update(negativeOrder)
                self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                    posPlausibleInProp)

                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1

                return EpistemicSpace(epistemicSpace.states, newObservables)
            else:
                positiveOrder = dict()
                negativeOrder = dict()
                postiveHelperOrder = dict()
                for key in epistemicSpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    postiveHelperOrder.update({key: []})
                for state in epistemicSpace.states.getStates():          # Create keys for orders
                    if state not in self.getIntersection(stubbornProp):
                        positiveOrder.pop(state)
                for key in positiveOrder.keys():                             # Create pos order
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
                maxLen = 0
                for key in positiveOrder.keys():
                    maxLen = max(maxLen, len(positiveOrder[key]))
                for key in positiveOrder.keys():
                    if len(positiveOrder[key]) == maxLen and key in self.getIntersection(stubbornProp):
                        posPlausibleInProp.add(key)
                for key in epistemicSpace.states.getStates():
                    if key not in posPlausibleInProp:
                        postiveHelperOrder.pop(key)

                for state in epistemicSpace.states.getStates():
                    if state not in posPlausibleInProp:
                        negativeOrder.update({state: []})

                for key in negativeOrder.keys():                            # Create neg order
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if (state in self.getIntersection(stubbornProp) or state in posPlausibleInProp) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                for key in postiveHelperOrder.keys():                      # Create posHelper order
                    postiveHelperOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in epistemicSpace.states.getStates():
                        if state in self.getIntersection(stubbornProp) and state in postiveHelperOrder[key] and state not in posPlausibleInProp:
                            postiveHelperOrder[key].remove(state)

                for positiveState in postiveHelperOrder.keys():            # Add the 'negative' worlds to positive
                    for negativeState in negativeOrder.keys():
                        postiveHelperOrder[positiveState].append(negativeState)
                    for anotherState in set(positiveOrder.keys()).difference(postiveHelperOrder.keys()):
                        postiveHelperOrder[positiveState].append(anotherState)
                postiveHelperOrder.update(negativeOrder)
                self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                    posPlausibleInProp)

                # Update stubbornness degree
                if self.stubbornnessDegrees[proposition] == 1:
                    if self.timesOfIncomingInfo[proposition] == self.stubbornnessDegrees[self.getNegation(proposition)]:
                        self.stubbornnessDegrees[proposition] = self.timesOfIncomingInfo[proposition]
                        self.stubbornnessDegrees[self.getNegation(
                            proposition)] = 1

                return EpistemicSpace(epistemicSpace.states, newObservables)

    def framingBiasedConditioning(self, epistemicSpace: EpistemicSpace, proposition: string):
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        realObs = copy.deepcopy(self.observables.getObservables())
        framedObservables = self.framingFunction(
            self.observables.getObservables())
        # Create new set S
        helperStates = set()
        for state in epistemicSpace.states.getStates():
            helperStates.add(state)

        newStates = framedObservables[proposition]
        epistemicSpace.states.updateStates(
            epistemicSpace.states.getStates().intersection(newStates))
        statesToRemove = helperStates.difference(
            epistemicSpace.states.getStates())
        newStates = States.States(epistemicSpace.states.getStates())
        for state in statesToRemove:
            for key in self.plausibilityOrder.getOrder().keys():
                if state in self.plausibilityOrder.getOrder()[key]:
                    self.plausibilityOrder.getOrder()[key].remove(state)
            for anotherState in newStates.getStates():
                if state in self.plausibilityOrder.getWorldsRelation()[anotherState]:
                    self.plausibilityOrder.getWorldsRelation()[
                        anotherState].remove(state)
            if state in self.plausibilityOrder.getWorldsRelation():
                self.plausibilityOrder.getWorldsRelation().pop(state)
            if state in self.plausibilityOrder.getMostPlausibleWorlds():
                self.plausibilityOrder.getMostPlausibleWorlds().remove(state)
        self.plausibilityOrder = PlausibilityOrder(
            self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
        newPlSpace = EpistemicSpace(
            states=epistemicSpace.states, observbles=realObs)
        return newPlSpace

    def framingBiasedLexRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        self.bias = "Framing"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        standardObservables = Observables(
            epistemicSpace.observables.getObservables())

        framedObservables = self.framingFunction(
            epistemicSpace.observables.getObservables())

        newObservables = Observables(framedObservables)
        # Create two helper state orders
        # Posittive and negative
        positiveOrder = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():  # Initialize orders
            positiveOrder.update({key: []})
            negativeOrder.update({key: []})
        for state in epistemicSpace.states.getStates():  # Create orders' keys
            if state not in newObservables.getObservables()[proposition]:
                positiveOrder.pop(state)
            if state in newObservables.getObservables()[proposition]:
                negativeOrder.pop(state)
        for key in positiveOrder.keys():                # Create positive order values
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in newObservables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        for key in negativeOrder.keys():                # Create negative order values
            negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in newObservables.getObservables()[proposition] and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)
        # New worldsRelation
        for positiveState in positiveOrder.keys():      # Create new worlds relation
            for negativeState in negativeOrder.keys():
                positiveOrder[positiveState].append(negativeState)
        positiveOrder.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrder)
        maxLen = 0
        # Create the set of most plaus worlds
        newMostPlausibleWorlds = set()
        for key in self.plausibilityOrder.getWorldsRelation().keys():
            maxLen = max(maxLen, len(
                self.plausibilityOrder.getWorldsRelation()[key]))
        for key in self.plausibilityOrder.getWorldsRelation().keys():
            if len(self.plausibilityOrder.getWorldsRelation()[key]) == maxLen:
                newMostPlausibleWorlds.add(key)
        self.plausibilityOrder.updateMostPlausibleWorlds(
            newMostPlausibleWorlds)
        self.plausibilityOrder.updateOrder(self.wordlsRelationToOrder(
            self.plausibilityOrder.getWorldsRelation()))

        return EpistemicSpace(epistemicSpace.states, newObservables)

    def framingBiasedMinRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        self.bias = "Framing"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        framedObservables = self.framingFunction(
            epistemicSpace.observables.getObservables())

        worldsRelationHelper = copy.deepcopy(
            self.plausibilityOrder.getWorldsRelation())

        newObservables = Observables(framedObservables)
        positiveOrder = dict()
        positiveOrderHelper = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: []})
            positiveOrderHelper.update({key: []})
        for state in epistemicSpace.states.getStates():          # Create keys for orders
            if state not in framedObservables[proposition]:
                positiveOrder.pop(state)
        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in framedObservables[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in framedObservables[proposition]:
                posPlausibleInProp.add(key)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                negativeOrder.update({key: []})

        for key in negativeOrder.keys():                            # Create neg order
            negativeOrder[key] = worldsRelationHelper[
                key]
            for state in epistemicSpace.states.getStates():
                if state in posPlausibleInProp and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)

        for key in positiveOrderHelper.keys():                      # Create posHelper order
            positiveOrderHelper[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in framedObservables[proposition] and state in positiveOrderHelper[key] and state not in posPlausibleInProp:
                    positiveOrderHelper[key].remove(state)
        for positiveState in positiveOrderHelper.keys():            # Add the 'negative' worlds to positive
            for negativeState in negativeOrder.keys():
                positiveOrderHelper[positiveState].append(negativeState)
            for anotherState in set(positiveOrder.keys()).difference(positiveOrderHelper.keys()):
                positiveOrderHelper[positiveState].append(anotherState)
        positiveOrderHelper.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrderHelper)
        if len(posPlausibleInProp) > 0:
            self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                posPlausibleInProp)
        else:
            maxLen = 0
            newPlausibleWordls = set()
            for key in positiveOrder.keys():
                maxLen = max(maxLen, len(positiveOrderHelper[key]))
            for key in positiveOrderHelper.keys():
                if len(positiveOrderHelper[key]) == maxLen and key in framedObservables[proposition]:
                    newPlausibleWordls.add(key)
            if len(newPlausibleWordls) > 0:
                self.plausibilityOrder.updateMostPlausibleWorlds(
                    newPlausibleWordls)
            else:
                maxLen = 0
                newPlausibleWordls = set()
                for key in positiveOrder.keys():
                    maxLen = max(maxLen, len(positiveOrderHelper[key]))
                for key in positiveOrderHelper.keys():
                    if len(positiveOrderHelper[key]) == maxLen and key in framedObservables[proposition]:
                        newPlausibleWordls.add(key)
                if len(newPlausibleWordls) > 0:
                    self.plausibilityOrder.updateMostPlausibleWorlds(
                        newPlausibleWordls)
        return EpistemicSpace(epistemicSpace.states, newObservables)

    def anchoringBiasedConditioning(self, epistemicSpace: EpistemicSpace, proposition: string):
        helperStates = epistemicSpace.states.getStates()
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        positiveOrder = dict()
        for key in epistemicSpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: []})

        for state in epistemicSpace.states.getStates():          # Create keys for orders
            if state not in epistemicSpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)

        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in epistemicSpace.observables.getObservables()[proposition]:
                posPlausibleInProp.add(key)
        newStates = epistemicSpace.states.getStates()
        newStates = newStates.intersection(posPlausibleInProp)
        newStates = States.States(newStates)
        statesToRemove = helperStates.difference(newStates.getStates())
        for state in statesToRemove:
            for key in self.plausibilityOrder.getOrder().keys():
                if state in self.plausibilityOrder.getOrder()[key]:
                    self.plausibilityOrder.getOrder()[key].remove(state)
            for anotherState in newStates.getStates():
                if state in self.plausibilityOrder.getWorldsRelation()[anotherState]:
                    self.plausibilityOrder.getWorldsRelation()[
                        anotherState].remove(state)
            self.plausibilityOrder.getWorldsRelation().pop(state)
        if len(posPlausibleInProp) > 1:
            anchWorld = choice(tuple(posPlausibleInProp))
            self.plausibilityOrder.updateMostPlausibleWorlds(anchWorld)
        else:
            self.plausibilityOrder.updateMostPlausibleWorlds(
                posPlausibleInProp)
        self.plausibilityOrder = PlausibilityOrder(
            self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
        newPlSpace = EpistemicSpace(
            states=newStates, observbles=newObservables)
        return newPlSpace

    def anchoringBiasedLexRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        worldsRelationHelper = copy.deepcopy(
            self.plausibilityOrder.getWorldsRelation())
        positiveOrder = dict()
        positiveOrderHelper = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: set()})
            positiveOrderHelper.update({key: set()})
        for state in epistemicSpace.states.getStates():          # Create keys for orders
            if state not in epistemicSpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in epistemicSpace.observables.getObservables()[proposition]:
                posPlausibleInProp.add(key)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                negativeOrder.update({key: set()})
        for key in negativeOrder.keys():                            # Create neg order
            negativeOrder[key] = worldsRelationHelper[
                key]
            for state in epistemicSpace.states.getStates():
                if state in posPlausibleInProp and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                positiveOrderHelper.pop(key)

        for key in positiveOrderHelper.keys():                      # Create posHelper order
            positiveOrderHelper[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrderHelper[key] and state not in posPlausibleInProp:
                    positiveOrderHelper[key].remove(state)
        for positiveState in positiveOrderHelper.keys():            # Add the 'negative' worlds to positive
            for negativeState in negativeOrder.keys():
                positiveOrderHelper[positiveState].append(negativeState)
            for anotherState in set(positiveOrder.keys()).difference(positiveOrderHelper.keys()):
                positiveOrderHelper[positiveState].append(anotherState)
        positiveOrderHelper.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrderHelper)
        if len(posPlausibleInProp) > 1:
            anchWorld = choice(tuple(posPlausibleInProp))
            self.plausibilityOrder.updateMostPlausibleWorlds(anchWorld)
        else:
            self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                posPlausibleInProp)
        return EpistemicSpace(epistemicSpace.states, newObservables)

    def anchoringBiasedMinRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        newObservables = Observables(
            epistemicSpace.observables.getObservables())
        worldsRelationHelper = copy.deepcopy(
            self.plausibilityOrder.getWorldsRelation())
        positiveOrder = dict()
        positiveOrderHelper = dict()
        negativeOrder = dict()
        for key in epistemicSpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: []})
            positiveOrderHelper.update({key: []})
        for state in epistemicSpace.states.getStates():          # Create keys for orders
            if state not in epistemicSpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state not in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in epistemicSpace.observables.getObservables()[proposition]:
                posPlausibleInProp.add(key)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                negativeOrder.update({key: []})
        for key in negativeOrder.keys():                            # Create neg order
            negativeOrder[key] = worldsRelationHelper[
                key]
            for state in epistemicSpace.states.getStates():
                if state in posPlausibleInProp and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)

        for key in epistemicSpace.states.getStates():
            if key not in posPlausibleInProp:
                positiveOrderHelper.pop(key)

        for key in positiveOrderHelper.keys():                      # Create posHelper order
            positiveOrderHelper[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in epistemicSpace.states.getStates():
                if state in epistemicSpace.observables.getObservables()[proposition] and state in positiveOrderHelper[key] and state not in posPlausibleInProp:
                    positiveOrderHelper[key].remove(state)
        for positiveState in positiveOrderHelper.keys():            # Add the 'negative' worlds to positive
            for negativeState in negativeOrder.keys():
                positiveOrderHelper[positiveState].append(negativeState)
            for anotherState in set(positiveOrder.keys()).difference(positiveOrderHelper.keys()):
                positiveOrderHelper[positiveState].append(anotherState)
        positiveOrderHelper.update(negativeOrder)
        self.plausibilityOrder.updateWorldsRelation(positiveOrderHelper)
        if len(posPlausibleInProp) > 1:
            anchWorld = choice(tuple(posPlausibleInProp))
            self.plausibilityOrder.updateMostPlausibleWorlds(anchWorld)
        else:
            self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                posPlausibleInProp)
        return EpistemicSpace(epistemicSpace.states, newObservables)

    def inGroupFavoritismConditioning(self, epistemicSpace: EpistemicSpace, proposition: string):
        self.isInGroup = True
        return self.confirmationBiasedConditioning(epistemicSpace, proposition)

    def inGroupFavoritismLexRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        self.isInGroup = True
        return self.confirmationBiasedLexRevision(epistemicSpace, proposition)

    def inGroupFavoritismMinRevision(self, epistemicSpace: EpistemicSpace, proposition: string):
        self.isInGroup = True
        return self.confirmationBiasedMinRevision(epistemicSpace, proposition)

    def getNegation(self, proposition: string):
        if len(proposition) == 1:
            return str("~" + proposition)
        else:
            return proposition[1]

    # Function to overcome the exception thrown
    # by the built in function index()
    def newIndex(self, list, element):
        if element in list:
            return list.index(element)
        else:
            return 0

    def wordlsRelationToOrder(self, worldsRelation):
        maxLen = 0
        order = dict()
        for key in worldsRelation.keys():
            maxLen = max(maxLen, len(worldsRelation[key]))
        for i in range(maxLen):
            order.update({i: []})
        for i in range(maxLen):
            for state in worldsRelation:
                if len(worldsRelation[state]) == i:
                    order[i].append(state)
        return order

    def getIntersection(self, propositions):
        newList = []
        newSet = set()
        for proposition in propositions:
            for element in self.observables.getObservables()[proposition]:
                newList.append(element)

        for element in newList:
            if newList.count(element) > 1:
                newSet.add(element)

        return newSet

    def updateResources(self, resources):
        self.resources = resources
