from re import I
from typing import Tuple, final
import States
import Obsevables
from itertools import chain, combinations


class Valuation():
    def __init__(self) -> None:
        pass

    # Create the powerset of all the states to be used
    # for observables, as O is subset of P(S)
    def powerset(self, states: States):
        s = list(states.getStates())
        powerset = set(chain.from_iterable(combinations(s, r)
                       for r in range(len(s)+1)))

        newPowerSet = set()
        finalPowerSet = set()
        for i in powerset:
            newPowerSet.add(frozenset(self.tupleToSet(i)))

        for i in newPowerSet:
            finalPowerSet.add(frozenset(i))

        return finalPowerSet

    def getTruthValues(self, states: States, observables: Obsevables):
        truthValues = dict()
        for ob in observables:
            for state in states:
                pass

    def tupleToSet(self, tuple: Tuple):
        newSet = set()
        for i in tuple:
            newSet.add(i)
        return newSet
