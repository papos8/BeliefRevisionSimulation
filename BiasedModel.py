import States
import Obsevables
import Valuation
import Agent


class BiasedModel():
    def __init__(self, states: States, observables: Obsevables, agents: Agent-set, valuation: Valuation) -> None:
        self.states = states
        self.observables = observables
        self.agents = agents
        self.valuation = valuation
