import Agent


class Player(Agent.Agent):
    def __init__(self, epistemicSpace, typeOfbias, typeOfAgent):
        super().__init__(epistemicSpace, typeOfbias, typeOfAgent)
        self.position = (0, 0)
        self.epistemiceSpace = epistemicSpace
        self.typeOfAgent = typeOfAgent
        self.typeOfBias = typeOfbias
        
    def turnLeft(self):
        print("Player turned left!")

    def turnRight(self):
        print("Player turned right!")

    def reverse(self):
        print("Player reversed!")

    def moveForward(self):
        print("Player moved forward!")
