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
    
    for i in range(1,20):
        unbiasedCounter = 0
        for j in range(10):
            print("Test: " + str(j) )
            states = States.States(3)
            print(states.getActualWorld())
            
            obs = Observables(7,states)
            epistemicSpaceForUnbiased = EpistemicSpace(
                states, obs)
            unbiasedAgent = Agent(epistemicSpaceForUnbiased, "Confirmation", "Random")
            print(obs.getObservables())
            print(unbiasedAgent.plausibilityOrder.getWorldsRelation())
            data = DataSequence.DataSequence(states,obs)
            print(data.getDataSequence())
            for i in range(len(data.getDataSequence())):
                epistemicSpaceForUnbiased = unbiasedAgent.anchoringBiasedLexRevision(
                    epistemicSpaceForUnbiased, data.getDataSequence()[i])
                
            if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                unbiasedCounter += 1
                print(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())
                print("Identified")
            else:
                print(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())
                print("Not")
        
        percentages.append(unbiasedCounter)

    
    newPercentages = [(item/200)*100 for item in percentages]
    
    print(newPercentages)
    xAxis = np.array(range(1,20))
    yAxis = np.array(newPercentages)

    plt.plot(xAxis,yAxis)
    plt.ylim([0,110])
    plt.xticks(range(1,20))

    plt.xlabel("Number of observables")
    plt.ylabel("Success Percentage")
    plt.title("Success percentage of anchoring bias lexicographic revision for 5 states")
    plt.show()
    exit()