from email.policy import strict
import imp
from operator import imod
import string
from tkinter import Widget
from typing import Dict
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from Obsevables import Observables
from BiasedModel import PlausibilitySpace
import States
from random import randint, random, uniform


class Agent():
    def __init__(self) -> None:
        self.resources = uniform(0.0, 100.0)
        self.bias = ""

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

    def conditioning(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def lexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def minRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def confirmationBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def confirmationBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def confirmationBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def framingBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def framingBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def framingBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def anchoringBiasedConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def anchoringBiasedLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def anchoringBiasedMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def inGroupFavoritismConditioning(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def inGroupFavoritismLexRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass

    def inGroupFavoritismMinRevision(self, plausibilitySpace: PlausibilitySpace, proposition: set):
        pass


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
