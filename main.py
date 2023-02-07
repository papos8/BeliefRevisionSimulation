from curses import init_pair
from email.policy import strict
from errno import EL2NSYNC
from re import S
from sre_parse import State
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from random import randint
import kivy.lang.builder as kbui
import Agent
import Ball
from BiasedModel import PlausibilitySpace
from DataSequence import DataSequence
from Formula import Conjuction, Letter, Negation
from Obsevables import Observables
import States
import string
import random
from Valuation import Valuation

numberOfStates = int(input('How many possible worlds are there? '))
states = States.States(numberOfStates)

agent1 = Agent.Agent(states)
obs = Observables(states)
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("Worlds relation for agent 1")
print(agent1.plausibilityOrder.getWorldsRelation())
print("Observables")
print(obs.getObservables())
print("Most Plausible Worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
plSpace = PlausibilitySpace(states, obs)

'''
# Example for revising using condition
newSpace = agent1.conditioning(
    plSpace, input("What is the incoming information? "))
print("Agent's new plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
print("Agent's new worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("States after conditioning")
print(newSpace.states.getStates())
print("New observables")
print(newSpace.observables.getObservables())
anotherSpace = agent1.conditioning(
    newSpace, input("What is the incoming information? "))
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
print("Agent's new worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())

# Example for revising using lex revision
newSpace = agent1.lexRevision(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
anotherSpace = agent1.lexRevision(newSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for minimal revision
newSpace = agent1.minRevision(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
anotherSpace = agent1.minRevision(newSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for CB conditioning - create an example for
newSpace = agent1.confirmationBiasedConditioning(plSpace, input(
    "What is the incoming information? "))
print(agent1.stubbornnessDegree(obs.getObservables()))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for CB lex revision - create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.confirmationBiasedLexRevision(plSpace, input(
    "What is the incoming information? "))
print(agent1.stubbornnessDegree(obs.getObservables()))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for CB min revision - create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.confirmationBiasedMinRevision(plSpace, input(
    "What is the incoming information? "))
print(agent1.stubbornnessDegree(obs.getObservables()))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for FR conditioning- create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.framingBiasedConditioning(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for FR lex revision- create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.framingBiasedLexRevision(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())

# Example for FR min revision- create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.framingBiasedMinRevision(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
'''
# Example for AN conditioning - create an example for
print("Randomness is to strict to have results! Have to create custom examples")
newSpace = agent1.anchoringBiasedConditioning(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print("New worlds relation")
print(agent1.plausibilityOrder.getWorldsRelation())
print("New most plausible worlds")
print(agent1.plausibilityOrder.getMostPlausibleWorlds())
