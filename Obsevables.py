from ast import arg
from http.client import ImproperConnectionState
from tkinter import N
import string
import random
import States


class Literals():
    def getLiterals():
        literals = set()
        for literal in string.ascii_uppercase:
            literals.add(literal)
            literals.add("~" + literal)


class Observables():
    def __init__(self, states) -> None:
        observables = set()
        for i in range(2**len(states)):
            pass
