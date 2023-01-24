from operator import imod
from tkinter import Widget
from typing import Dict
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from Obsevables import Observables
import States
from random import randint, random, uniform


class Agent():
    def __init__(self) -> None:
        self.resources = uniform(0.0, 100.0)

    # Framing function to return a subset of
    # a proposition
    def framingFunction(self, observables: dict):
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
        for proposition in observables:
            # Make agents stubborn towards positive propositions
            # as it doesn't really matter if it's the actual
            # proposition or its negation
            if proposition[0] == "~":
                if dictOfDegress[proposition[1]] > 1:
                    dictOfDegress[proposition] = 0
            stubbornnessDegree = randint(1, 5)
            dictOfDegress.update({proposition: stubbornnessDegree})

    def conditioning(self, states: States, observables: Observables):
        pass

    def lexRevision(self, states: States, observables: Observables):
        pass

    def minRevision(self, states: States, observables: Observables):
        pass

    def confirmationBiasedConditioning(self, states: States, observables: Observables):
        pass

    def confirmationBiasedLexRevision(self, states: States, observables: Observables):
        pass

    def confirmationBiasedMinRevision(self, states: States, observables: Observables):
        pass

    def framingBiasedConditioning(self, states: States, observables: Observables):
        pass

    def framingBiasedLexRevision(self, states: States, observables: Observables):
        pass

    def framingBiasedMinRevision(self, states: States, observables: Observables):
        pass

    def anchoringBiasedConditioning(self, states: States, observables: Observables):
        pass

    def anchoringBiasedLexRevision(self, states: States, observables: Observables):
        pass

    def anchoringBiasedMinRevision(self, states: States, observables: Observables):
        pass

    def inGroupFavoritismConditioning(self, states: States, observables: Observables):
        pass

    def inGroupFavoritismLexRevision(self, states: States, observables: Observables):
        pass

    def inGroupFavoritismMinRevision(self, states: States, observables: Observables):
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
