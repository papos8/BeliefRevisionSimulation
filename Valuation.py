from re import I
from typing import Tuple, final
from Formula import Formula
import States
import Obsevables
from itertools import chain, combinations


class Valuation():
    def __init__(self, observables: Obsevables) -> None:
        self.valuation = observables

    def getTruthValue(self, formula: Formula):
        return self.valuation.getObservables()[formula.getString()]
