import States
from itertools import permutations
import random


class PlausibilityOrder():
    def __init__(self, states: States) -> None:
        self.order = []
        index = random.choice(
            range(len(list(permutations(list(states.getStates()))))))
        self.order = list(list(permutations(list(states.getStates())))[index])

    def getOrder(self):
        return self.order

    def updateOrder(self, newOrder):
        self.order = newOrder
