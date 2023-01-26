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
print(obs.getObservables())
plSpace = PlausibilitySpace(states, obs, agent1)
# Example for revising using condition
'''
newSpace = agent1.conditioning(
    plSpace, input("What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print(newSpace.states.getStates())
print(newSpace.observables.getObservables())
'''

# Example for revising using lex revision
'''
newSpace = agent1.lexRevision(plSpace, input(
    "What is the incoming information? "))
print("Agent's plausibility order:")
print(agent1.plausibilityOrder.getOrder())
print(newSpace.states.getStates())
print(newSpace.observables.getObservables())
'''
