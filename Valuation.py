from re import I
from typing import Tuple, final
import States
import Obsevables
from itertools import chain, combinations


class Valuation():
    def __init__(self, observables: Obsevables) -> None:
        self.valuation = observables

    def getTruthValue(self, formula):
        return self.valuation.getObservables()[formula.getString()]
