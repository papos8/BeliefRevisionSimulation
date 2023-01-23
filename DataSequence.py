import Obsevables
import States
import random


class DataSequence():
    def __init__(self, observables: Obsevables, state: States, length: int) -> None:
        self.dataSequence = set()
        for i in range(length):
            self.dataSequence.add(random.choice(tuple(observables)))

    def isSound(self, state: States):
        pass

    def isComplete(self, state: States):
        pass
