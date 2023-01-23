from operator import imod
from tkinter import Widget
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
        self.stubDegree = randint(1, 10)
        self.resources = uniform(0.0, 100.0)

    def framingFunction(self, proposition: Observables):
        return

    def conditioning():
        pass

    def lexRevision():
        pass

    def minRevision():
        pass

    def biasedConditioning():
        pass

    def biasedLexRevision():
        pass

    def biasedMinRevision():
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
