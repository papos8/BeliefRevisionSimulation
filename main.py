
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
from Obsevables import Observables
import States

numberOfStates = int(input('How many possible states are there? '))
states = States.States(numberOfStates)
print(states.getStates())
