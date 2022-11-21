class Agent:
    def __init__(self, SD, Resources):
        self.SD = SD
        self.Resources = Resources


class Player(Agent):
    def __init__(self, SD, Position):
        super().__init__(SD)
        self.Position = Position
