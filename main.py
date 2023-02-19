from asyncore import file_dispatcher
from audioop import bias
from os import stat
from re import A
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from random import randint
import kivy.lang.builder as kbui
import Agent
import Ball
from EpistemicSpace import EpistemicSpace
from DataSequence import DataSequence
from Formula import Conjuction, Letter, Negation
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

'''
# Custom test for Confirmation Biased Conditioning
file = open("Custom_Tests/ConfirmationBiasConditioning.txt", "w")
file.write("Compare unbiased conditioning and confirmation biased condition.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Confirmation", "Custom")
data = DataSequence.DataSequence(states, obs)
print(unbiasedAgent)
print(biasedAgent)
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.conditioning(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.confirmationBiasedConditioning(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''

'''
# Custom test for Confirmation Biased Lex Revision
file = open("Custom_Tests/ConfirmationBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and confirmation biased lexicographic revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Confirmation", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Confirmation Biased Min Revision
file = open("Custom_Tests/ConfirmationBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and confirmation biased minimal revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Confirmation", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.minRevision(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.confirmationBiasedMinRevision(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Framing Biased Conditioning
file = open("Custom_Tests/FramingBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and framing biased conditioning.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Framing", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.conditioning(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.framingBiasedConditioning(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Framing Biased Lex Revision
file = open("Custom_Tests/FramingBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and framing biased lexicographic revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Framing", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.framingBiasedLexRevision(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Framing Biased Min Revision
file = open("Custom_Tests/FramingBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and framing biased minimal revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Framing", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.minRevision(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.framingBiasedMinRevision(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Anchoring Biased Conditioning
file = open("Custom_Tests/AnchoringBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and anchoring biased conditioning.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Anchoring", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.conditioning(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.anchoringBiasedConditioning(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
'''
# Custom test for Anchoring Biased Lex Revision
file = open("Custom_Tests/AnchoringBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and anchoring biased lexicographic revision.\nAs anchoring biased lexicographic revision behaves as the unbiased minimal revision, we expect lexicographic revision to behave better than anchoring biased lexicographic revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Anchoring", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.anchoringBiasedLexRevision(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''

'''
# Custom test for Anchoring Biased Min Revision
file = open("Custom_Tests/AnchoringBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and anchoring biased minimal revision.\nAs they behave the same, this example is included for the sake of completeness.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders and same stubbornness degrees. \n\n""")
states = States.States("Create")
newStates = copy.deepcopy(states)
obs = Observables("Create")
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
unbiasedAgent = Agent.Agent(epistemicSpaceForUnbiased, "Unbiased", "Custom")
# Create biased agent
print("Create biased agent")
biasedAgent = Agent.Agent(epistemicSpaceForBiased, "Anchoring", "Custom")
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
    file.write(key + ":" + str(unbiasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForUnbiased = unbiasedAgent.minRevision(
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
    else:
        file.write("Unbiased agent failed to identify the actual world!\n\n")
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
    file.write(key + ":" + str(biasedAgent.stubbornnessDegrees[key]) + ", ")
file.write("\n")
for i in range(len(data.getDataSequence())):
    epistemicSpaceForBiased = biasedAgent.anchoringBiasedMinRevision(
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
    else:
        file.write("Biased agent failed to identifiy the actual world!\n\n")
else:
    file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
               for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
    file.write("Biased agent failed to identifiy the actual world!\n\n")
file.close()
'''
