from os import stat
import States
import Obsevables
import Valuation
import Agent
from BiasedModel import EpistemicSpace


class BiasedModel():
    def __init__(self, plausibilitySpace,  valuation: Valuation) -> None:
        self.plausibilitySpace = plausibilitySpace
        self.valuation = valuation


class PlausibilitySpace():
    def __init__(self, epistemicSpace: EpistemicSpace, agent: Agent) -> None:
        self.epistemicSpace = epistemicSpace
        self.agent = agent


class EpistemicSpace():
    def __init__(self, states: States, observbles: Obsevables) -> None:
        self.states = states
        self.observables = observbles
