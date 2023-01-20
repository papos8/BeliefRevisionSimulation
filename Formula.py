
import random
import string
from tkinter.tix import Form


class Formula():
    def __init__(self) -> None:
        pass


class Letter(Formula):
    def __init__(self) -> None:
        super().__init__()

    def getLetter():
        return random.choice(string.ascii_uppercase)

    def getTruthValue(state):
        truthValues = {0, 1}
        return "true" if random.choice(tuple(truthValues)) == 1 else "false"


class Negation(Formula):
    def __init__(self) -> None:
        super().__init__()
