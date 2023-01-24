from os import stat
import States
import Obsevables
import Valuation
import Agent


class BiasedModel():
    def __init__(self, plausibilitySpace,  valuation: Valuation) -> None:
        self.plausibilitySpace = plausibilitySpace
        self.valuation = valuation


class PlausibilitySpace():
    def __init__(self, states: States, observbles: Obsevables, agent: Agent) -> None:
        self.states = states
        self.observables = observbles
        self.agent = agent
