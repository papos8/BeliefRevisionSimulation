from operator import imod
from tkinter import Widget
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from random import randint


class Agent(Widget):
    def __init__(self, SD, Resources):
        self.SD = SD
        self.Resources = Resources


class Player(Agent):
    def __init__(self, SD, Position):
        super().__init__(SD)
        self.Position = Position

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def reverse(self):
        pass

    def moveForward(self):
        pass
