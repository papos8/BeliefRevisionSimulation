from os import stat
import States
import Obsevables
import Valuation
import Agent


class BiasedModel():
    def __init__(self, plausibilitySpace,  valuation: Valuation) -> None:
        self.plausibilitySpace = plausibilitySpace
        self.valuation = valuation


class EpistemicSpace():
    def __init__(self, states: States, observbles: Obsevables) -> None:
        self.states = states
        self.observables = observbles
