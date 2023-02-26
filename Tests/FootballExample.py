from cgi import print_arguments
import imp
from os import stat
from random import randint
from Agent import *
from EpistemicSpace import EpistemicSpace
from DataSequence import DataSequence
from Obsevables import Observables
from PlausibilityOrder import PlausibilityOrder
import States
import string
import DataSequence
import random
from Valuation import Valuation
import Group
import json
import copy
import sys
import matplotlib.pyplot as plt
import numpy as np
from Player import *


def callTest():
    file = open("Custom_Tests/FootballExample.txt","w")
    file.write("Simple example to demonstrate the in-group communication.\n")
    file.write("""In this example we create 4 players, the captain, two midfielders and an attacking midfielder, 
which is considered to have the ball and need to turn left. Here we will only demonstrate how could weights affect
the decision, without taking into consideration the revision method used by the agent. However, we assign weights
to the agents to demonstrate how they affect decision-making. We use both fair unanimity and different weights.
In the latter case, the captain is assigned a higher weight than the rest, which are assigned equal weights. """)
    states = States.States("Custom")
    obs = Observables("Custom")
    file.write("The given states are: " + (', '.join(str(state)
            for state in states.getStates())) + "\n")
    file.write("The actual world is: " + states.getActualWorld() + "\n")
    file.write("The given observables are: ")
    for prop in obs.getObservables():
        file.write(prop + ":" + str(obs.getObservables()[prop]) + ", ")
    file.write("\n\n")
    eps = EpistemicSpace(states, obs)
    
    # Unanimity  
    numberOfTunrs = 0
    playerWeights = {"attackingMidfielder" : float(1/4), "captain" : float(1/4), "midfielder1" : float(1/4), "midfielder2" : float(1/4)}
    file.write("Player weights using fair unanimity are :\n")
    for player in playerWeights:
        file.write(player + ": " + str(playerWeights[player]) + ", ")    
    for i in range(100):
        setOfAgents = set()
        attackingMidfielder = Player(eps, "Confirmation", "Random")
        captain = Player(eps, "Confirmation", "Random")
        midfielder1 = Player(eps, "Confirmation", "Random")
        midfielder2 = Player(eps, "Confirmation", "Random")
        setOfAgents.add(captain)
        setOfAgents.add(attackingMidfielder)
        setOfAgents.add(midfielder1)
        setOfAgents.add(midfielder2)
        file.write("Attacking midfielder's stubbornness degrees: ")
        for key in attackingMidfielder.stubbornnessDegrees:
            file.write(key + ":" + str(attackingMidfielder.stubbornnessDegrees[key]) + ", ")
        file.write("\n")
        support = 0
        against = 0        
        dictOfPlayers = {"captain":captain,"attackingMidfielder":attackingMidfielder,"midfielder1":midfielder1,"midfielder2":midfielder2}
        for player in dictOfPlayers:   
            if dictOfPlayers[player].stubbornnessDegrees["P"]>1:
                support += playerWeights[player]
            elif dictOfPlayers[player].stubbornnessDegrees["~P"]>1:
                against += playerWeights[player]
        if support - against > float(attackingMidfielder.stubbornnessDegrees["P"]/4):
            #attackingMidfielder.turnLeft()
            file.write("Player turned left.\n")
            numberOfTunrs += 1
        else:
            file.write("The player has to pass back.\n")
    file.write("The agent turned left " + str(numberOfTunrs) + " times and passed back " + str(100-numberOfTunrs) + " times.\n")
        


    # Assign different weights
    numberOfTunrs = 0
    playerWeights = {"attackingMidfielder" : float(1/9), "captain" : float(2/3), "midfielder1" : float(1/9), "midfielder2" : float(1/9)}
    file.write("Player weights using fair unanimity are :\n")
    for player in playerWeights:
        file.write(player + ": " + str(playerWeights[player]) + ", ")
    for i in range(100):
        setOfAgents = set()
        attackingMidfielder = Player(eps, "Confirmation", "Random")
        captain = Player(eps, "Confirmation", "Random")
        midfielder1 = Player(eps, "Confirmation", "Random")
        midfielder2 = Player(eps, "Confirmation", "Random")
        setOfAgents.add(captain)
        setOfAgents.add(attackingMidfielder)
        setOfAgents.add(midfielder1)
        setOfAgents.add(midfielder2)
        file.write("Attacking midfielder's stubbornness degrees: ")
        for key in attackingMidfielder.stubbornnessDegrees:
            file.write(key + ":" + str(attackingMidfielder.stubbornnessDegrees[key]) + ", ")
        file.write("\n")

        support = 0
        against = 0        
        dictOfPlayers = {"captain":captain,"attackingMidfielder":attackingMidfielder,"midfielder1":midfielder1,"midfielder2":midfielder2}
        for player in dictOfPlayers:   
            if dictOfPlayers[player].stubbornnessDegrees["P"]>1:
                support += playerWeights[player]
            elif dictOfPlayers[player].stubbornnessDegrees["~P"]>1:
                against += playerWeights[player]

        if support - against > float(attackingMidfielder.stubbornnessDegrees["P"]/4):
            #attackingMidfielder.turnLeft()
            file.write("Player turned left.\n")
            numberOfTunrs += 1
        else:
            file.write("The player has to pass back.\n")
    
    file.write("The agent turned left " + str(numberOfTunrs) + " times and passed back " + str(100-numberOfTunrs) + " times.\n")
        
    file.close()