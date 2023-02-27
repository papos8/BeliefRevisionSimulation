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
    for i in range(3,26):
        unbiasedCounter = 0    
        
        for j in range(200):
            print("Test: " + str(j) )
            states = States.States(3)
            obs = Observables(5,states)
            print("Actual world: " + str(states.getActualWorld()))
    
            epistemicSpaceForUnbiased = EpistemicSpace(
                states, obs)
            agent = Agent(epistemicSpaceForUnbiased, "Confirmation", "Random")
            print("Observables: ")
            print(obs.getObservables())
            print("Initial plausibility order: ")
            print(agent.plausibilityOrder.getWorldsRelation())
            data = DataSequence.DataSequence(i,states,obs)
            print("Data sequence: ")
            print(data.getDataSequence())
            for i in range(len(data.getDataSequence())):
                epistemicSpaceForUnbiased = agent.confirmationBiasedLexRevision(
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
    xAxis = np.array(range(3,26))
    yAxis = np.array(newPercentages)

    plt.plot(xAxis,yAxis)
    plt.ylim([0,110])
    plt.xticks(range(3,26))

    plt.xlabel("Length of data sequence")
    plt.ylabel("Success Percentage")
    #plt.title("Success percentage of confirmation-biased lexicographic revision for 3 states and different lengths of data sequences.")
    plt.show()
    