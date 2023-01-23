
from pstats import StatsProfile
import random
from socketserver import ForkingMixIn
import string
from tkinter.tix import Form
from States import States


class Formula():
    def __init__(self) -> None:
        pass

    def getString(self):
        pass

    def getTruthValue(self):
        pass


class Letter(Formula):
    def __init__(self) -> None:
        super().__init__()
        self.letter = str(random.choice(tuple(string.ascii_uppercase)))

    def getString(self):
        return self.letter

    def getTruthValue(self, state: States):
        truthValues = {0, 1}
        truthValue = "true" if random.choice(
            tuple(truthValues)) == 1 else "false"
        return truthValue


class Negation(Formula):
    def __init__(self, Formula) -> None:
        super().__init__()

    def getString(self, Formula: Formula):
        return "~" + Formula.getString()

    def getTruthValue(self, state: States):
        truthValues = {0, 1}
        truthValue = "true" if random.choice(
            tuple(truthValues)) == 1 else "false"
        return truthValue


class Conjuction(Formula):
    def __init__(self, FirstFormula: Formula, SecondFormula: Formula) -> None:
        super().__init__()
        self.FirstFormula = FirstFormula
        self.SecondFormula = SecondFormula

    def getString(self):
        return "(" + self.FirstFormula.getString() + "/\\" + self.SecondFormula.getString() + ")"

    def getTruthValue(self, state: States):
        if self.FirstFormula.getTruthValue(state) == "true" and self.SecondFormula.getTruthValue(state) == "true":
            return "true"
        else:
            return "false"
