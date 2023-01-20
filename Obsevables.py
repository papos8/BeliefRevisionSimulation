from tkinter import N
import States


class Observables():
    def __init__(self) -> None:
        states = States.States(numberOfStates=None)
        observables = set()
