from operator import truth
from re import I
from typing import Tuple, final
import States
import Obsevables
from itertools import chain, combinations


class Valuation():
    def __init__(self, observables: Obsevables, state) -> None:
        self.valuation = observables
        self.state = state

    def getTruthValues(self, observables, state):
        truthValues = dict()
        for obs in observables.keys():
            truthValues.update({obs: False})
        for obs in observables.keys():
            if state in observables[obs]:
                observables[obs] = True
        return truthValues

    def getTruthValue(self, formula, state):
        # Function to evaluate a complex formula on
        # a given state.
        pass
