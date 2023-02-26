from cgi import print_arguments
import imp
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


def callTest():
    
    percentages = []
    for i in range(1,26):
        unbiasedCounter = 0
        for j in range(200):
            print("Test: " + str(j) )
            states = States.States(10)
            print("Actual world: " + str(states.getActualWorld()))
            
            obs = Observables(i,states)
            epistemicSpaceForUnbiased = EpistemicSpace(
                states, obs)
            agent = Agent(epistemicSpaceForUnbiased, "Unbiased", "Random")
            print("Observables: ")
            print(obs.getObservables())
            print("Initial plausibility order: ")
            print(agent.plausibilityOrder.getWorldsRelation())
            data = DataSequence.DataSequence(states,obs)
            print("Data sequence: ")
            print(data.getDataSequence())
            for i in range(len(data.getDataSequence())):
                epistemicSpaceForUnbiased = agent.minRevision(
                    epistemicSpaceForUnbiased, data.getDataSequence()[i])
            print("Final plausibility order: ")
            print(agent.plausibilityOrder.getWorldsRelation())
            if len(agent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(agent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                unbiasedCounter += 1
                print(agent.plausibilityOrder.getMostPlausibleWorlds())
                print("Identified")
            else:
                print(agent.plausibilityOrder.getMostPlausibleWorlds())
                print("Not")
        
        percentages.append(unbiasedCounter)

    
    newPercentages = [(item/200)*100 for item in percentages]
    
    print(newPercentages)
    xAxis = np.array(range(1,26))
    yAxis = np.array(newPercentages)

    plt.plot(xAxis,yAxis)
    plt.ylim([0,110])
    plt.xticks(range(1,26))

    plt.xlabel("Number of observables")
    plt.ylabel("Success Percentage")
    plt.title("Success percentage of unbiased lexicographic revision for 10 states")
    plt.show()
    