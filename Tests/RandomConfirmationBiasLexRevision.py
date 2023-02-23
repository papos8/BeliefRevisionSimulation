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
    numberOfTests = 200
    # Randomly created test for Confirmation Bias Lexicographic Revision
    file = open("Randomly_Created_Tests/ConfirmationBiasLexRevision.txt", "w")
    file.write(
        "Compare unbiased lexicographic and confirmation bias lexicographic revision.\n")
    file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
    file.write(str(numberOfTests) + \
            " randomly created tests will be generated and the success percentage will be displayed in the end.\n")
    unbiasedSuccess = 0
    biasedSuccess = 0
    for i in range(numberOfTests):
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
        # Create biased agent
        print("Create biased agent")
        biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                                "Confirmation", "Random")

        biasedAgent.plausibilityOrder.updateWorldsRelation(copy.deepcopy(
            unbiasedAgent.plausibilityOrder.getWorldsRelation()))
        biasedAgent.plausibilityOrder.updateMostPlausibleWorlds(copy.deepcopy(
            unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()))

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
        for i in range(len(data.getDataSequence())):
            epistemicSpaceForUnbiased = unbiasedAgent.lexRevision(
                epistemicSpaceForUnbiased, data.getDataSequence()[i])
            file.write("Unbiased agent's plausibility order after receiving " +
                    data.getDataSequence()[i] + ": ")
            for key in unbiasedAgent.plausibilityOrder.getWorldsRelation():
                file.write(
                    key + ":" + str(unbiasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
            file.write("\n")
        if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1:
            file.write("Unbiased agent's most plausible world: " +
                    list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] + "\n")
            if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
                file.write("Unbiased agent identified the actual world!\n\n")
                unbiasedSuccess += 1
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
        for i in range(len(data.getDataSequence())):
            epistemicSpaceForBiased = biasedAgent.confirmationBiasedLexRevision(
                epistemicSpaceForBiased, data.getDataSequence()[i])
            file.write("Biased agent's plausibility order after receiving " +
                    data.getDataSequence()[i] + ": ")
            for key in biasedAgent.plausibilityOrder.getWorldsRelation():
                file.write(
                    key + ":" + str(biasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
            file.write("\n")
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
    file.write("Unbiased agent identified the actual world " +
            str((float(unbiasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
    file.write("Biased agent identified the actual world " +
            str(float(round((biasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
    file.write("Biased agent identified " +
            str(float(round((biasedSuccess/unbiasedSuccess)*100, 2))) +
            "% of the identifiable cases (actual worlds).\n")
    file.close()
