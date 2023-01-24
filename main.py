
from email.policy import strict
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

obs = Observables(states)
for ob in obs.getObservables():
    print(ob)
