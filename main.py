from email.policy import strict
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
print(states.getStates())

lit = Letter()
neg = Negation(lit)

print(lit.getString())
print(lit.getTruthValue(list(states.getStates())[0]))

print(neg.getString(lit))
print(neg.getTruthValue(list(states.getStates())[0]))


con = Conjuction(lit, lit)
print(con.getString())
print(con.getTruthValue(list(states.getStates())[0]))


agent1 = Agent.Agent(states)
print(agent1.bias)
print(agent1.resources)
print(agent1.plausibilityOrder.getOrder())
obs = Observables(states)
print(obs.getObservables())
plSpace = PlausibilitySpace(states, obs, agent1)
agent1.conditioning(plSpace, input("What is the incoming information?"))
print(states.getStates())
