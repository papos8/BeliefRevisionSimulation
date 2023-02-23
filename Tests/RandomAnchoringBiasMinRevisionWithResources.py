from random import randint
import Agent
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

def callTest():
    # Randomly created test for Anchoring Bias Minimal Revision with resources
    numberOfTests = 200
    file = open(
        "Randomly_Created_Tests/AnchoringBiasMinRevisionWithResources.txt", "w")
    file.write(
        "Compare unbiased minimal and anchoring bias minimal revision.\nIn these tests we also compare when the two methods idenitfy the actual world to see if anchoring bias minimal revision is faster than unbiased minimal revision.\n")
    file.write("These tests also include resources of the agents in order to see whether anchoring bias is good method as an heuristic.\n")
    file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
    file.write(str(numberOfTests) +
            " randomly created tests will be generated and the success percentage will be displayed in the end.\n")
    unbiasedSuccess = 0
    biasedSuccess = 0
    counterForTimeEqual = 0
    counterForTimeUnbiased = 0
    counterForTimeBiased = 0
    for i in range(numberOfTests):
        unbiasedCounter = 0
        biasedCounter = 0
        unbiasedBoolean = False
        biasedBoolean = False
        states = States.States(5)
        newStates = copy.deepcopy(states)
        obs = Observables(states)
        file.write("The given states are: " + (', '.join(str(state)
                                                        for state in states.getStates())) + "\n")
        file.write("The actual world is: " + states.getActualWorld() + "\n")
        file.write("The given observables are: ")
        for prop in obs.getObservables():
            file.write(prop + ":" + str(obs.getObservables()[prop]) + ", ")
        file.write("\n\n")
        epistemicSpaceForUnbiased = EpistemicSpace(
            states, obs)
        epistemicSpaceForBiased = EpistemicSpace(newStates, obs)

        # Create unbiased agent
        print("Create unbiased agent")
        unbiasedAgent = Agent.Agent(
            epistemicSpaceForUnbiased, "Unbiased", "Random")
        unbiasedAgent.updateResources(round(unbiasedAgent.resources, 2))
        # Create biased agent
        print("Create biased agent")
        biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                                "Anchoring", "Random")

        biasedAgent.plausibilityOrder.updateWorldsRelation(copy.deepcopy(
            unbiasedAgent.plausibilityOrder.getWorldsRelation()))
        biasedAgent.plausibilityOrder.updateMostPlausibleWorlds(copy.deepcopy(
            unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()))
        biasedAgent.updateResources(
            round(copy.deepcopy(unbiasedAgent.resources), 2))

        data = DataSequence.DataSequence(states, obs)

        file.write("The data sequence the agents received is: ")
        for prop in data.getDataSequence():
            file.write(prop + ", ")
        file.write("\n\n")

        file.write("Unbiased agent's initial plausibility order: ")
        for key in unbiasedAgent.plausibilityOrder.getWorldsRelation():
            file.write(
                key + ":" + str(unbiasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
        file.write("\n")
        file.write("Unbiased agent's stubbornness degrees: ")
        for key in unbiasedAgent.stubbornnessDegrees:
            file.write(
                key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
        file.write("\n")
        file.write("Unbiased agent's initial resources: " +
                str(unbiasedAgent.resources) + "\n")

        while unbiasedAgent.resources > 1:
            for i in range(len(data.getDataSequence())):
                epistemicSpaceForUnbiased = unbiasedAgent.minRevision(
                    epistemicSpaceForUnbiased, data.getDataSequence()[i])
                file.write("Unbiased agent's plausibility order after receiving " +
                        data.getDataSequence()[i] + ": ")
                for key in unbiasedAgent.plausibilityOrder.getWorldsRelation():
                    file.write(
                        key + ":" + str(unbiasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
                file.write("\n")
                if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                    unbiasedCounter += 1
                else:
                    unbiasedCounter = 0
                unbiasedAgent.resources = float(
                    unbiasedAgent.resources)/50
                file.write("Unbiased agent's resources: " +
                        str(unbiasedAgent.resources) + "\n")
                if unbiasedAgent.resources <= 1:
                    break

        if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1:
            file.write("Unbiased agent's most plausible world: " +
                    list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] + "\n")
            if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                file.write("Unbiased agent identified the actual world!\n\n")
                unbiasedSuccess += 1
                unbiasedBoolean = True
            else:
                file.write(
                    "Unbiased agent failed to identify the actual world!\n\n")
        else:
            file.write("Unbiased agent's most plausible worlds: " + ('-').join(str(world)
                                                                            for world in unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
            file.write("Unbiased agent failed to identify the actual world!\n\n")

        file.write("Biased agent's initial plausibility order: ")
        for key in biasedAgent.plausibilityOrder.getWorldsRelation():
            file.write(
                key + ":" + str(biasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
        file.write("\n")
        file.write("Biased agent's stubbornness degrees: ")
        for key in biasedAgent.stubbornnessDegrees:
            file.write(
                key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
        file.write("\n")
        file.write("Biased agent's initial resources: " +
                str(biasedAgent.resources) + "\n")

        while biasedAgent.resources > 1:
            for i in range(len(data.getDataSequence())):
                epistemicSpaceForBiased = biasedAgent.anchoringBiasedMinRevision(
                    epistemicSpaceForBiased, data.getDataSequence()[i])
                file.write("Biased agent's plausibility order after receiving " +
                        data.getDataSequence()[i] + ": ")
                for key in biasedAgent.plausibilityOrder.getWorldsRelation():
                    file.write(
                        key + ":" + str(biasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
                file.write("\n")
                if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                    biasedCounter += 1
                    biasedBoolean = True
                else:
                    biasedCounter = 0
                biasedAgent.resources = float(
                    biasedAgent.resources)/50
                file.write("Biased agent's resources: " +
                        str(biasedAgent.resources) + "\n")
                if biasedAgent.resources <= 1:
                    break

        file.write("\n")
        if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1:
            file.write("Biased agent's most plausible world: " +
                    list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] + "\n")
            if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                file.write("Biased agent identified the actual world!\n\n")
                biasedSuccess += 1
            else:
                file.write("Biased agent failed to identifiy the actual world!\n\n")
        else:
            file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                            for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
            file.write("Biased agent failed to identifiy the actual world!\n\n")

        if unbiasedBoolean and biasedBoolean:
            if biasedCounter > 0 and unbiasedCounter > 0 and biasedCounter < unbiasedCounter:
                counterForTimeBiased += 1
            elif biasedCounter > 0 and unbiasedCounter > 0 and biasedCounter > unbiasedCounter:
                counterForTimeUnbiased += 1
            elif biasedCounter > 0 and unbiasedCounter > 0 and biasedCounter == unbiasedCounter:
                counterForTimeEqual += 1
    file.write("Unbiased agent identified the actual world " +
            str((float(unbiasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
    file.write("Biased agent identified the actual world " +
            str(float(round((biasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")

    file.write(str(float(round(counterForTimeBiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
            "% of the identified worlds, biased agent identified the world faster than the unbiased.\n")
    file.write(str(float(round(counterForTimeUnbiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
            "% of the identified worlds, unbiased agent identified the world faster than the biased.\n")
    file.write(str(float(round(counterForTimeEqual/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
            "% of the identified worlds, the agents identified the actual world the same time.\n")
    file.close()
