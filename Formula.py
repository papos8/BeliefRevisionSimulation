
import random
import string
from tkinter.tix import Form


class Formula():
    def __init__(self) -> None:
        pass


class Letter(Formula):
    def __init__(self) -> None:
        super().__init__()

    def letter():
        return random.choice(string.ascii_uppercase)


class Negation(Formula):
    def __init__(self) -> None:
        super().__init__()
