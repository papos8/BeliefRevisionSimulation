from asyncio.proactor_events import _ProactorBasePipeTransport
from re import S
import string
from tkinter import Widget
from tkinter.tix import DirTree
from turtle import pos
from typing import Dict
from xmlrpc.client import ProtocolError
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from Obsevables import Observables
from BiasedModel import PlausibilitySpace
from PlausibilityOrder import PlausibilityOrder
import States
from random import randint, random, uniform, choice, sample


class Agent():
    def __init__(self, states: States) -> None:
        self.resources = uniform(0.0, 100.0)
        self.bias = "Unbiased"
        self.plausibilityOrder = PlausibilityOrder(states)

    # Framing function to return a subset of
    # a proposition
    def framingFunction(self, observables: dict):
        ''' If agent is under framing bias we use the
        framing function. Otherwise, observables
        are returned without change '''
        if self.bias == "Framing":
            for proposition in observables:
                value = observables[proposition]
                # Here the subset is taken completely random
                # This may affect the results
                newValue = sample(value, randint(
                    0, len(observables[proposition])))
                observables[proposition] = newValue

        return observables

    # Function that return a dictionary of a proposition and
    # the stubbornness degree of the agent towards this
    # proposition
    def stubbornnessDegree(self, observables: dict):
        dictOfDegress = dict()
        ''' If the agent is not unbiased a random integer
        between 1 and 5 is assigned as stubbornness degree
        to every observable proposition. Otherwise, the degree
        is 1 for every observable proposition '''
        if self.bias == "Confirmation":
            for proposition in observables:
                dictOfDegress.update({proposition: 0})
            for proposition in observables:
                if self.getNegation(proposition) in observables and dictOfDegress[self.getNegation(proposition)] > 0:
                    continue
                else:
                    dictOfDegress[proposition] = randint(1, 5)
        elif self.bias == "Unbiased":
            for proposition in observables:
                dictOfDegress.update({proposition: 1})
        return dictOfDegress

    # Implement conditioning based on the definitions
    def conditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Unbiased"
        # Create new set S
        helperStates = plausibilitySpace.states.getStates()
        newStates = plausibilitySpace.observables.getObservables()[proposition]
        plausibilitySpace.states.updateStates(
            plausibilitySpace.states.getStates().intersection(newStates))
        newStates = States.States(newStates)
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact
        newObservables = dict()
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        # Stubbornnes Degree is applied as well,
        # but should return 1 for every observable
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                newValue = framedObservables[observable].intersection(
                    framedObservables[proposition])
                if len(newValue) > 0:
                    newObservables.update({observable: newValue})
        newObservables = Observables(newObservables)
        # Update plaus order to have only the new states
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
            if state in self.plausibilityOrder.getMostPlausibleWorlds():
                self.plausibilityOrder.getMostPlausibleWorlds().remove(state)
        self.plausibilityOrder = PlausibilityOrder(
            self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
        newPlSpace = PlausibilitySpace(
            states=newStates, observbles=newObservables)
        return newPlSpace

    def lexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Unbiased"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)
        # Create two helper state orders
        # Posittive and negative
        positiveOrder = dict()
        negativeOrder = dict()
        for key in plausibilitySpace.states.getStates():  # Initialize orders
            positiveOrder.update({key: []})
            negativeOrder.update({key: []})
        for state in plausibilitySpace.states.getStates():  # Create orders' keys
            if state not in plausibilitySpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
            if state in plausibilitySpace.observables.getObservables()[proposition]:
                negativeOrder.pop(state)
        for key in positiveOrder.keys():                # Create positive order values
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in plausibilitySpace.states.getStates():
                if state not in plausibilitySpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        for key in negativeOrder.keys():                # Create negative order values
            negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in plausibilitySpace.states.getStates():
                if state in plausibilitySpace.observables.getObservables()[proposition] and state in negativeOrder[key]:
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
        return PlausibilitySpace(plausibilitySpace.states, newObservables)

    def minRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Unbiased"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)
        positiveOrder = dict()
        positiveOrderHelper = dict()
        negativeOrder = dict()
        for key in plausibilitySpace.states.getStates():            # Initialize orders
            positiveOrder.update({key: []})
            negativeOrder.update({key: []})
            positiveOrderHelper.update({key: []})
        for state in plausibilitySpace.states.getStates():          # Create keys for orders
            if state not in plausibilitySpace.observables.getObservables()[proposition]:
                positiveOrder.pop(state)
            if state in plausibilitySpace.observables.getObservables()[proposition]:
                negativeOrder.pop(state)
        for key in positiveOrder.keys():                             # Create pos order
            positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in plausibilitySpace.states.getStates():
                if state not in plausibilitySpace.observables.getObservables()[proposition] and state in positiveOrder[key]:
                    positiveOrder[key].remove(state)
        posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
        maxLen = 0
        for key in positiveOrder.keys():
            maxLen = max(maxLen, len(positiveOrder[key]))
        for key in positiveOrder.keys():
            if len(positiveOrder[key]) == maxLen and key in plausibilitySpace.observables.getObservables()[proposition]:
                posPlausibleInProp.add(key)

        for key in plausibilitySpace.states.getStates():
            if key not in posPlausibleInProp:
                positiveOrderHelper.pop(key)
        for key in negativeOrder.keys():                            # Create neg order
            negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in plausibilitySpace.states.getStates():
                if state in plausibilitySpace.observables.getObservables()[proposition] and state in negativeOrder[key]:
                    negativeOrder[key].remove(state)

        for key in positiveOrderHelper.keys():                      # Create posHelper order
            positiveOrderHelper[key] = self.plausibilityOrder.getWorldsRelation()[
                key]
            for state in plausibilitySpace.states.getStates():
                if state in plausibilitySpace.observables.getObservables()[proposition] and state in positiveOrderHelper[key] and state not in posPlausibleInProp:
                    positiveOrderHelper[key].remove(state)
        print(positiveOrderHelper)
        for positiveState in positiveOrderHelper.keys():            # Add the 'negative' worlds to positive
            for negativeState in negativeOrder.keys():
                positiveOrderHelper[positiveState].append(negativeState)
            for anotherState in set(positiveOrder.keys()).difference(positiveOrderHelper.keys()):
                positiveOrderHelper[positiveState].append(anotherState)
        positiveOrderHelper.update(negativeOrder)
        self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
            posPlausibleInProp)

        return PlausibilitySpace(plausibilitySpace.states, newObservables)

    def confirmationBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Confirmation"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)
        # Initialize memory for times the information has come
        timesOfIncomingInfo = dict()
        for obs in plausibilitySpace.observables.getObservables():
            timesOfIncomingInfo.update({obs: 0})

        if timesOfIncomingInfo[proposition] >= stubbornnessDegrees[proposition]:
            self.conditioning(plausibilitySpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in stubbornnessDegrees.keys():
                if stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)

            if proposition in stubbornProp:
                helperStates = plausibilitySpace.states.getStates()
                newStates = plausibilitySpace.states.getStates()
                # Create a set of worls that are in the stub props
                for observable in stubbornnessDegrees.keys():
                    if stubbornnessDegrees[observable] > 0:
                        for state in plausibilitySpace.states.getStates():
                            if state in plausibilitySpace.observables.getObservables()[observable]:
                                newStates = newStates.intersection(
                                    plausibilitySpace.observables.getObservables()[observable])

                plausibilitySpace.states.updateStates(
                    plausibilitySpace.states.getStates().intersection(newStates))
                newStates = States.States(newStates)
                newObservables = dict()
                framedObservables = self.framingFunction(
                    plausibilitySpace.observables.getObservables())
                for observable in framedObservables:
                    newValue = framedObservables[observable].intersection(
                        framedObservables[proposition])
                    if len(newValue) > 0:
                        newObservables.update({observable: newValue})
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
                self.plausibilityOrder = PlausibilityOrder(
                    self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
                newPlSpace = PlausibilitySpace(
                    states=newStates, observbles=newObservables)
                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0
                return newPlSpace
            else:
                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0
                return plausibilitySpace

    def confirmationBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Confirmation"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)
        # Initialize memory for times the information has come
        timesOfIncomingInfo = dict()
        for obs in plausibilitySpace.observables.getObservables():
            timesOfIncomingInfo.update({obs: 0})

        if timesOfIncomingInfo[proposition] >= stubbornnessDegrees[proposition]:
            self.lexRevision(plausibilitySpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in stubbornnessDegrees.keys():
                if stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)

            if proposition in stubbornProp:
                # Orders that will help creating the new world relation
                # A world relation is consider an order
                positiveOrder = dict()
                negativeOrder = dict()
                intersectionSet = stubbornProp.intersection(
                    plausibilitySpace.observables.getObservables()[proposition])
                negativeIntersectionSet = stubbornProp.intersection(
                    plausibilitySpace.observables.getObservables()[self.getNegation(proposition)])
                for key in plausibilitySpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                for state in plausibilitySpace.states.getStates():  # Create orders' keys - Delete the unwanted
                    if state not in intersectionSet:
                        positiveOrder.pop(state)
                    if state not in negativeIntersectionSet:
                        negativeOrder.pop(state)
                for key in positiveOrder.keys():                # Create positive order values
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state not in intersectionSet and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                for key in negativeOrder.keys():                # Create negative order values
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state not in plausibilitySpace.observables.getObservables()[proposition] and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                # New worldsRelation
                for positiveState in positiveOrder.keys():      # Create new worlds relation
                    for negativeState in negativeOrder.keys():
                        positiveOrder[positiveState].append(negativeState)
                positiveOrder.update(negativeOrder)
                print(positiveOrder)
                print(negativeOrder)
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
                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0
                return PlausibilitySpace(plausibilitySpace.states, newObservables)
            else:
                # Create new orders to help with the new worlds relation
                # The new orders will hold only the stubborn prop as the incoming
                # Information is a contradiction and the agent revise only the stubborn env
                positiveOrder = dict()
                negativeOrder = dict()
                for key in plausibilitySpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                for state in plausibilitySpace.states.getStates():  # Create orders' keys - Delete the unwanted
                    if state not in self.getIntersection(stubbornProp):
                        positiveOrder.pop(state)
                    if state in self.getIntersection(stubbornProp):
                        negativeOrder.pop(state)
                for key in positiveOrder.keys():                # Create positive order values
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                for key in negativeOrder.keys():                # Create negative order values
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state in self.getIntersection(stubbornProp) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)
                # New worldsRelation
                for positiveState in positiveOrder.keys():      # Create new worlds relation
                    for negativeState in negativeOrder.keys():
                        positiveOrder[positiveState].append(negativeState)
                positiveOrder.update(negativeOrder)
                print(positiveOrder)
                print(negativeOrder)
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

                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0
                return PlausibilitySpace(plausibilitySpace.states, newObservables)

    def confirmationBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Confirmation"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)
        # Initialize memory for times the information has come
        timesOfIncomingInfo = dict()
        for obs in plausibilitySpace.observables.getObservables():
            timesOfIncomingInfo.update({obs: 0})

        if timesOfIncomingInfo[proposition] >= stubbornnessDegrees[proposition]:
            self.minRevision(plausibilitySpace, proposition)
        else:
            stubbornProp = set()  # Set to store the proposition the agent is stub towards
            for prop in stubbornnessDegrees.keys():
                if stubbornnessDegrees[prop] > 1:
                    stubbornProp.add(prop)

            if proposition in stubbornProp:
                positiveOrder = dict()
                negativeOrder = dict()
                postiveHelperOrder = dict()
                for key in plausibilitySpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                    postiveHelperOrder.update({key: []})
                for state in plausibilitySpace.states.getStates():          # Create keys for orders
                    # For the sake of completeness,
                    # As proposition is already there
                    if state not in self.getIntersection(stubbornProp).intersection(proposition):
                        positiveOrder.pop(state)
                for key in positiveOrder.keys():                             # Create pos order
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp).interesection(proposition) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
                maxLen = 0
                for key in positiveOrder.keys():
                    maxLen = max(maxLen, len(positiveOrder[key]))
                for key in positiveOrder.keys():
                    if len(positiveOrder[key]) == maxLen and key in self.getIntersection(stubbornProp).intersection(proposition):
                        posPlausibleInProp.add(key)
                for key in plausibilitySpace.states.getStates():
                    if key not in posPlausibleInProp:
                        postiveHelperOrder.pop(key)
                for key in negativeOrder.keys():                            # Create neg order
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state in self.getIntersection(stubbornProp).intersection(proposition) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                for key in postiveHelperOrder.keys():                      # Create posHelper order
                    postiveHelperOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state in self.getIntersection(stubbornProp).intersection(proposition) and state in postiveHelperOrder[key] and state not in posPlausibleInProp:
                            postiveHelperOrder[key].remove(state)

                for positiveState in postiveHelperOrder.keys():            # Add the 'negative' worlds to positive
                    for negativeState in negativeOrder.keys():
                        postiveHelperOrder[positiveState].append(negativeState)
                    for anotherState in set(positiveOrder.keys()).difference(postiveHelperOrder.keys()):
                        postiveHelperOrder[positiveState].append(anotherState)
                postiveHelperOrder.update(negativeOrder)
                self.plausibilityOrder.updateMostPlausibleWorlds(           # The most plausible worlds are the most plaus in p
                    posPlausibleInProp)

                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0

                return PlausibilitySpace(plausibilitySpace.states, newObservables)
            else:
                positiveOrder = dict()
                negativeOrder = dict()
                postiveHelperOrder = dict()
                for key in plausibilitySpace.states.getStates():            # Initialize orders
                    positiveOrder.update({key: []})
                    negativeOrder.update({key: []})
                    postiveHelperOrder.update({key: []})
                for state in plausibilitySpace.states.getStates():          # Create keys for orders
                    if state not in self.getIntersection(stubbornProp):
                        positiveOrder.pop(state)
                for key in positiveOrder.keys():                             # Create pos order
                    positiveOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state not in self.getIntersection(stubbornProp) and state in positiveOrder[key]:
                            positiveOrder[key].remove(state)
                posPlausibleInProp = set()  # Set to store the most plausible worlds in a proposition
                maxLen = 0
                for key in positiveOrder.keys():
                    maxLen = max(maxLen, len(positiveOrder[key]))
                for key in positiveOrder.keys():
                    if len(positiveOrder[key]) == maxLen and key in self.getIntersection(stubbornProp):
                        posPlausibleInProp.add(key)
                for key in plausibilitySpace.states.getStates():
                    if key not in posPlausibleInProp:
                        postiveHelperOrder.pop(key)
                for key in negativeOrder.keys():                            # Create neg order
                    negativeOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
                        if state in self.getIntersection(stubbornProp) and state in negativeOrder[key]:
                            negativeOrder[key].remove(state)

                for key in postiveHelperOrder.keys():                      # Create posHelper order
                    postiveHelperOrder[key] = self.plausibilityOrder.getWorldsRelation()[
                        key]
                    for state in plausibilitySpace.states.getStates():
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

                timesOfIncomingInfo[proposition] = timesOfIncomingInfo[proposition] + 1
                # Update stubbornness degree
                if timesOfIncomingInfo[proposition] == stubbornnessDegrees[self.getNegation(proposition)]:
                    stubbornnessDegrees[proposition] = timesOfIncomingInfo[proposition]
                    stubbornnessDegrees[self.getNegation(proposition)] = 0

                return PlausibilitySpace(plausibilitySpace.states, newObservables)

    def framingBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Framing"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)

        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        stubbornnessDegrees = self.stubbornnessDegree(
            framedObservables)
        print(framedObservables)
        newObservables = Observables(framedObservables)
        # Create new set S
        helperStates = plausibilitySpace.states.getStates()
        newStates = set(framedObservables[proposition])
        plausibilitySpace.states.updateStates(
            plausibilitySpace.states.getStates().intersection(newStates))
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
            if state in self.plausibilityOrder.getMostPlausibleWorlds():
                self.plausibilityOrder.getMostPlausibleWorlds().remove(state)
        self.plausibilityOrder = PlausibilityOrder(
            self.plausibilityOrder.getOrder(), self.plausibilityOrder.getWorldsRelation(), self.plausibilityOrder.getMostPlausibleWorlds())
        newPlSpace = PlausibilitySpace(
            states=newStates, observbles=newObservables)
        return newPlSpace

    def framingBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Framing"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)

    def framingBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.bias = "Framing"
        # Update the observables
        # Framing function is applied, but there should return
        # observables intact (For the sake of completeness)
        stubbornnessDegrees = self.stubbornnessDegree(
            plausibilitySpace.observables.getObservables())
        framedObservables = self.framingFunction(
            plausibilitySpace.observables.getObservables())
        for observable in framedObservables:
            if stubbornnessDegrees[observable] == 1:
                continue
        newObservables = Observables(framedObservables)

    def anchoringBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def anchoringBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def anchoringBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        self.minRevision(plausibilitySpace, proposition)

    def inGroupFavoritismConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def inGroupFavoritismLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def inGroupFavoritismMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

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
        newSet = set()
        newSet = choice(tuple(propositions))
        for proposition in propositions:
            newSet = newSet.intersection(proposition)
        return newSet


class Player(Agent):
    def __init__(self):
        super().__init__()
        self.position = (0, 0)

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def reverse(self):
        pass

    def moveForward(self):
        pass
