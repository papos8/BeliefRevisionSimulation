
from email.policy import strict
from gettext import lgettext
from operator import imod
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
from Formula import Conjuction, Letter, Negation
from Obsevables import Observables
import States
import string

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


obs = Observables()
print(obs.createObservables(states))
