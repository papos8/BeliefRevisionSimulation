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


#### Custom Tests ####
'''
# Custom test for Confirmation Bias Conditioning
file = open("Custom_Tests/ConfirmationBiasConditioning.txt", "w")
file.write("Compare unbiased conditioning and confirmation bias condition.\n")
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
# Custom test for Confirmation Bias Lex Revision
file = open("Custom_Tests/ConfirmationBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and confirmation bias lexicographic revision.\n")
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
# Custom test for Confirmation Bias Min Revision
file = open("Custom_Tests/ConfirmationBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and confirmation bias minimal revision.\n")
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
# Custom test for Framing Bias Conditioning
file = open("Custom_Tests/FramingBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and framing bias conditioning.\n")
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
# Custom test for Framing Bias Lex Revision
file = open("Custom_Tests/FramingBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and framing bias lexicographic revision.\n")
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
# Custom test for Framing Bias Min Revision
file = open("Custom_Tests/FramingBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and framing bias minimal revision.\n")
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
# Custom test for Anchoring Bias Conditioning
file = open("Custom_Tests/AnchoringBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and anchoring bias conditioning.\n")
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
# Custom test for Anchoring Bias Lex Revision
file = open("Custom_Tests/AnchoringBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and anchoring bias lexicographic revision.\nAs anchoring bias lexicographic revision behaves as the unbiased minimal revision, we expect lexicographic revision to behave better than anchoring biased lexicographic revision.\n")
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
# Custom test for Anchoring Bias Min Revision
file = open("Custom_Tests/AnchoringBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and anchoring bias minimal revision.\nAs anchoring bias minimal revision behaves same as the unbiased minimal revision in normal cases, we expect to behave same in this example.\n")
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


#### Randomly Created Tests ####
numberOfTests = 200
'''
# Randomly created test for Confirmation Bias Conditioning
file = open("Randomly_Created_Tests/ConfirmationBiasConditioning.txt", "w")
file.write("Compare unbiased conditioning and confirmation bias condition.\n")
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
'''
'''
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
'''
'''
# Randomly created test for Confirmation Bias Minimal Revision
file = open("Randomly_Created_Tests/ConfirmationBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and confirmation bias minimal revision.\n")
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
file.close()
'''
'''
# Randomly created test for Framing Bias Conditioning
file = open("Randomly_Created_Tests/FramingBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and framing bias conditioning.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
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
                              "Framing", "Random")

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
            biasedSuccess += 1
        else:
            file.write("Biased agent failed to identifiy the actual world!\n\n")
    else:
        file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                         for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
        file.write("Biased agent failed to identifiy the actual world!\n\n")
print(unbiasedSuccess)
print(biasedSuccess)
file.write("Unbiased agent identified the actual world " +
           str((float(unbiasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
file.write("Biased agent identified the actual world " +
           str(float(round((biasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
file.write("Biased agent identified " +
           str(float(round((biasedSuccess/unbiasedSuccess)*100, 2))) +
           "% of the identifiable cases (actual worlds).\n")
file.close()
'''
'''
# Randomly created test for Framing Bias Lexicographic Revision
file = open("Randomly_Created_Tests/FramingBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and framing bias lexicographic revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
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
                              "Framing", "Random")

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
'''
'''
# Randomly created test for Framing Bias Minimal Revision
file = open("Randomly_Created_Tests/FramingBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and framing bias minimal revision.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
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
                              "Framing", "Random")

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
            biasedSuccess += 1
        else:
            file.write("Biased agent failed to identifiy the actual world!\n\n")
    else:
        file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                         for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
        file.write("Biased agent failed to identifiy the actual world!\n\n")
print(unbiasedSuccess)
print(biasedSuccess)
file.write("Unbiased agent identified the actual world " +
           str((float(unbiasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
file.write("Biased agent identified the actual world " +
           str(float(round((biasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
file.close()
'''

'''
# Randomly created test for Anchoring Bias Conditioning
file = open("Randomly_Created_Tests/AnchoringBiasConditioning.txt", "w")
file.write(
    "Compare unbiased conditioning and anchoring bias conditioning.\nIn these tests we also compare when the two methods idenitfy the actual world to see if anchoring bias conditioning is faster than unbiased conditionin.\n")
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
    # Create biased agent
    print("Create biased agent")
    biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                              "Anchoring", "Random")

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
        epistemicSpaceForUnbiased = unbiasedAgent.conditioning(
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
    for i in range(len(data.getDataSequence())):
        epistemicSpaceForBiased = biasedAgent.anchoringBiasedConditioning(
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
file.write("Biased agent identified " +
           str(float(round((biasedSuccess/unbiasedSuccess)*100, 2))) +
           "% of the identifiable cases (actual worlds).\n\n")

file.write(str(float(round(counterForTimeBiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, biased agent identified the world faster than the unbiased.\n")
file.write(str(float(round(counterForTimeUnbiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, unbiased agent identified the world faster than the biased.\n")
file.write(str(float(round(counterForTimeEqual/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, the agents identified the actual world the same time.\n")
file.close()
'''

'''
# Randomly created test for Anchoring Bias Lexicographic Revision
file = open("Randomly_Created_Tests/AnchoringBiasLexRevision.txt", "w")
file.write(
    "Compare unbiased lexicographic and anchoring bias lexicographic revision.\nIn these tests we also compare when the two methods idenitfy the actual world to see if anchoring bias lexicographic revision is faster than unbiased lexicographci revision.\n")
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
    # Create biased agent
    print("Create biased agent")
    biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                              "Anchoring", "Random")

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
        if len(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(unbiasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
            unbiasedCounter += 1
        else:
            unbiasedCounter = 0
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
    for i in range(len(data.getDataSequence())):
        epistemicSpaceForBiased = biasedAgent.anchoringBiasedLexRevision(
            epistemicSpaceForBiased, data.getDataSequence()[i])
        file.write("Biased agent's plausibility order after receiving " +
                   data.getDataSequence()[i] + ": ")
        for key in biasedAgent.plausibilityOrder.getWorldsRelation():
            file.write(
                key + ":" + str(biasedAgent.plausibilityOrder.getWorldsRelation()[key]) + ", ")
        file.write("\n")
        if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
            biasedCounter += 1
        else:
            biasedCounter = 0
    file.write("\n")
    if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1:
        file.write("Biased agent's most plausible world: " +
                   list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] + "\n")
        if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
            file.write("Biased agent identified the actual world!\n\n")
            biasedSuccess += 1
            biasedBoolean = True
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
file.write("Biased agent identified " +
           str(float(round((biasedSuccess/unbiasedSuccess)*100, 2))) +
           "% of the identifiable cases (actual worlds).\n\n")

file.write(str(float(round(counterForTimeBiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, biased agent identified the world faster than the unbiased.\n")
file.write(str(float(round(counterForTimeUnbiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, unbiased agent identified the world faster than the biased.\n")
file.write(str(float(round(counterForTimeEqual/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, the agents identified the actual world the same time.\n")
file.close()
'''
'''
# Randomly created test for Anchoring Bias Minimal Revision
file = open("Randomly_Created_Tests/AnchoringBiasMinRevision.txt", "w")
file.write(
    "Compare unbiased minimal and anchoring bias minimal revision.\nIn these tests we also compare when the two methods idenitfy the actual world to see if anchoring bias minimal revision is faster than unbiased minimal revision.\n")
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
    biasedBoolean = False
    unbiasedBoolean = False
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
                              "Anchoring", "Random")

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
        else:
            biasedCounter = 0
    file.write("\n")
    if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1:
        file.write("Biased agent's most plausible world: " +
                   list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] + "\n")
        if len(biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) == 1 and list(biasedAgent.plausibilityOrder.getMostPlausibleWorlds())[0] == states.getActualWorld():
            file.write("Biased agent identified the actual world!\n\n")
            biasedSuccess += 1
            biasedBoolean = True
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
file.write("Biased agent identified " +
           str(float(round((biasedSuccess/unbiasedSuccess)*100, 2))) +
           "% of the identifiable cases (actual worlds).\n\n")

file.write(str(float(round(counterForTimeBiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, biased agent identified the world faster than the unbiased.\n")
file.write(str(float(round(counterForTimeUnbiased/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, unbiased agent identified the world faster than the biased.\n")
file.write(str(float(round(counterForTimeEqual/(counterForTimeBiased+counterForTimeEqual+counterForTimeUnbiased)*100, 2))) +
           "% of the identified worlds, the agents identified the actual world the same time.\n")
file.close()
'''
'''
# Randomly created test for In-Group Favoritism Conditioning
file = open("Randomly_Created_Tests/InGroupFavoritismConditioning.txt", "w")
file.write(
    "Compare confirmation bias conditioning and in-group favoritism conditioning.\nWe include these tests to see how group membership affects a biased agent.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
           " randomly created tests will be generated and the success percentage will be displayed in the end.\n")
biasedSuccess = 0
inGroupBiasedSuccess = 0
setOfAgents = set()
groupOfAgents = Group.Group(setOfAgents, 3)
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
        epistemicSpaceForUnbiased, "Confirmation", "Random")
    # Create biased agent
    print("Create biased agent")
    biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                              "Confirmation", "Random")
    groupOfAgents.addAgent(biasedAgent)
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
        epistemicSpaceForUnbiased = unbiasedAgent.confirmationBiasedConditioning(
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
            biasedSuccess += 1
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
        epistemicSpaceForBiased = biasedAgent.inGroupFavoritismConditioning(
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
            inGroupBiasedSuccess += 1
        else:
            file.write("Biased agent failed to identifiy the actual world!\n\n")
    else:
        file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                         for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
        file.write("Biased agent failed to identifiy the actual world!\n\n")
print(biasedSuccess)
print(inGroupBiasedSuccess)
file.write("Unbiased agent identified the actual world " +
           str((float(biasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
file.write("Biased agent identified the actual world " +
           str(float(round((inGroupBiasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
file.close()
'''

'''
# Randomly created test for In-Group Favoritism Lexicographic Revision
file = open("Randomly_Created_Tests/InGroupFavoritismLexRevision.txt", "w")
file.write(
    "Compare confirmation bias lexicographic and in-group favoritism lexicographic revision.\nWe include these tests to see how group membership affects a biased agent.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
           " randomly created tests will be generated and the success percentage will be displayed in the end.\n")
biasedSuccess = 0
inGroupBiasedSuccess = 0
setOfAgents = set()
groupOfAgents = Group.Group(setOfAgents, 3)
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
        epistemicSpaceForUnbiased, "Confirmation", "Random")
    # Create biased agent
    print("Create biased agent")
    biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                              "Confirmation", "Random")
    groupOfAgents.addAgent(biasedAgent)
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
        epistemicSpaceForUnbiased = unbiasedAgent.confirmationBiasedLexRevision(
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
            biasedSuccess += 1
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
        epistemicSpaceForBiased = biasedAgent.inGroupFavoritismLexRevision(
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
            inGroupBiasedSuccess += 1
        else:
            file.write("Biased agent failed to identifiy the actual world!\n\n")
    else:
        file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                         for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
        file.write("Biased agent failed to identifiy the actual world!\n\n")
print(biasedSuccess)
print(inGroupBiasedSuccess)
file.write("Unbiased agent identified the actual world " +
           str((float(biasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
file.write("Biased agent identified the actual world " +
           str(float(round((inGroupBiasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
file.close()
'''
'''
# Randomly created test for In-Group Favoritism Minimal Revision
file = open("Randomly_Created_Tests/InGroupFavoritismMinRevision.txt", "w")
file.write(
    "Compare confirmation bias minimal and in-group favoritism minimal revision.\nWe include these tests to see how group membership affects a biased agent.\n")
file.write("""First states and observables are created and then the plausibility orders of the agents.\nThe two agents have the same plausibility orders, but different stubbornness degrees. \n\n""")
file.write(str(numberOfTests) +
           " randomly created tests will be generated and the success percentage will be displayed in the end.\n")
biasedSuccess = 0
inGroupBiasedSuccess = 0
setOfAgents = set()
groupOfAgents = Group.Group(setOfAgents, 3)
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
        epistemicSpaceForUnbiased, "Confirmation", "Random")
    # Create biased agent
    print("Create biased agent")
    biasedAgent = Agent.Agent(epistemicSpaceForBiased,
                              "Confirmation", "Random")
    groupOfAgents.addAgent(biasedAgent)
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
        epistemicSpaceForUnbiased = unbiasedAgent.confirmationBiasedMinRevision(
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
            biasedSuccess += 1
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
        epistemicSpaceForBiased = biasedAgent.inGroupFavoritismMinRevision(
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
            inGroupBiasedSuccess += 1
        else:
            file.write("Biased agent failed to identifiy the actual world!\n\n")
    else:
        file.write("Biased agent's most plausible worlds: " + ('-').join(str(world)
                                                                         for world in biasedAgent.plausibilityOrder.getMostPlausibleWorlds()) + "\n")
        file.write("Biased agent failed to identifiy the actual world!\n\n")
print(biasedSuccess)
print(inGroupBiasedSuccess)
file.write("Unbiased agent identified the actual world " +
           str((float(biasedSuccess/numberOfTests)*100)) + "% of the cases.\n")
file.write("Biased agent identified the actual world " +
           str(float(round((inGroupBiasedSuccess/numberOfTests)*100, 2))) + "% of the cases.\n")
file.close()
'''
