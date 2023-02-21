from turtle import TurtleGraphicsError
import Agent


class Group():
    def __init__(self, agents: set, adaptiveFactor) -> None:
        self.agents = agents
        self.adaptiveFactor = adaptiveFactor

    def addAgent(self, agent):
        self.agents.add(agent)
