import Agent
import Valuation
import EpistemicSpace


class BiasedModel():
    def __init__(self, plausibilitySpace,  valuation: Valuation) -> None:
        self.plausibilitySpace = plausibilitySpace
        self.valuation = valuation


class PlausibilitySpace():
    def __init__(self, epistemicSpace: EpistemicSpace, agent: Agent) -> None:
        self.epistemicSpace = epistemicSpace
        self.agent = agent
