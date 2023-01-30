from email.policy import strict
from hashlib import new
from http.client import NETWORK_AUTHENTICATION_REQUIRED
import imp
from lib2to3.pgen2.token import PLUS
from operator import imod, neg
import re
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
from random import randint, random, uniform


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
                newValue = random.sample(value, randint(
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
        if self.bias != "Unbiased":
            for proposition in observables:
                # Make agents stubborn towards positive propositions
                # as it doesn't really matter if it's the actual
                # proposition or its negation
                if proposition[0] == "~":
                    if dictOfDegress[proposition[1]] > 1:
                        dictOfDegress[proposition] = 0
                stubbornnessDegree = randint(1, 5)
                dictOfDegress.update({proposition: stubbornnessDegree})
        else:
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
        newPlSpace = PlausibilitySpace(newStates, newObservables, self)
        return newPlSpace
    '''
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
        positiveOrder, negativeOrder = dict()
        for key in self.plausibilityOrder.getOrder().keys():
            positiveOrder.update({key: []})
            negativeOrder.update({key: []})
        for state in plausibilitySpace.states.getStates()
        [state for state in self.plausibilityOrder.getOrder(
        ) if state in list(plausibilitySpace.observables.getObservables()[proposition])]

        negativeOrder = [state for state in self.plausibilityOrder.getOrder(
        ) if state in list(plausibilitySpace.observables.getObservables()[self.getNegation(proposition)])]
        print("Positive order: ")
        print(positiveOrder)
        print("Negative order: ")
        print(negativeOrder)

        # In essence, new plausibility order is the concatenation of
        # the positive and negative ones, as lexicographic takes the
        # states related to the incoming world to the front of the
        # order
        self.plausibilityOrder.updateOrder(list(positiveOrder + negativeOrder))

        return PlausibilitySpace(plausibilitySpace.states, newObservables, self)
    '''

    def minRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def confirmationBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def confirmationBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def confirmationBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def framingBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def framingBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def framingBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def anchoringBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def anchoringBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

    def anchoringBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: string):
        pass

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
