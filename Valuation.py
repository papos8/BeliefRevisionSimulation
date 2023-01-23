import States
import Obsevables


class Valuation():
    def __init__(self) -> None:
        pass

    def getTruthValues(self, states: States, obs: Obsevables):
        truthValues = {}
        for ob in obs:
            for state in states:
                pass
