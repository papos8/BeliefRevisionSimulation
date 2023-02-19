from os import stat
import States
import Obsevables
import Valuation
import Agent


class EpistemicSpace():
    def __init__(self, states: States, observbles: Obsevables) -> None:
        self.states = states
        self.observables = observbles
