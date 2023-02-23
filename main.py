from asyncore import file_dispatcher
from audioop import bias
from operator import imod
from os import stat
from re import A
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
from Tests import RandomInGroupFavoritismMinRevision, RandomInGroupFavoritismLexRevision, RandomInGroupFavoritismConditioning, RandomAnchoringBiasMinRevisionWithResources, RandomAnchoringBiasMinRevision, RandomAnchoringBiasLexRevisionWithResources, RandomAnchoringBiasLexRevision, RandomAnchoringBiasConditioningWithResources, RandomAnchoringBiasConditioning, RandomFramingBiasMinRevision, RandomFramingBiasLexRevision, RandomFramingBiasConditioning, RandomConfirmationBiasMinRevision, RandomConfirmationBiasLexRevision, RandomConfirmationBiasConditioning, CustomAnchoringBiasMinRevision, CustomAnchoringBiasLexRevision, CustomAnchoringBiasConditioning, CustomFramingBiasMinRevision, CustomFramingBiasLexRevision, CustomConfirmationBiasConditioning, CustomConfirmationBiasConditioning, CustomConfirmationBiasMinRevision, CustomFramingBiasConditioning



if len(sys.argv) == 1:
    print("Give the number of the test you want run.")
elif int(sys.argv[1]) == 1:
    CustomConfirmationBiasConditioning.callTest()
elif int(sys.argv[1]) == 2:
    CustomConfirmationBiasConditioning.callTest()
elif int(sys.argv[1]) == 3:
    CustomConfirmationBiasMinRevision.callTest()
elif int(sys.argv[1]) == 4:
    CustomFramingBiasConditioning.callTest()
elif int(sys.argv[1]) == 5:
    CustomFramingBiasLexRevision.callTest()
elif int(sys.argv[1]) == 6:
    CustomFramingBiasMinRevision.callTest()
elif int(sys.argv[1]) == 7:
    CustomAnchoringBiasConditioning.callTest()
elif int(sys.argv[1]) == 8:
    CustomAnchoringBiasLexRevision.callTest()
elif int(sys.argv[1]) == 9:
    CustomAnchoringBiasMinRevision.callTest()
elif int(sys.argv[1]) == 10:
    RandomConfirmationBiasConditioning.callTest()
elif int(sys.argv[1]) == 11:
    RandomConfirmationBiasLexRevision.callTest()
elif int(sys.argv[1]) == 12:
    RandomConfirmationBiasMinRevision.callTest()
elif int(sys.argv[1]) == 13:
    RandomFramingBiasConditioning.callTest()
elif int(sys.argv[1]) == 14:
    RandomFramingBiasLexRevision.callTest()
elif int(sys.argv[1]) == 15:
    RandomFramingBiasMinRevision.callTest()
elif int(sys.argv[1]) == 16:
    RandomAnchoringBiasConditioning.callTest()
elif int(sys.argv[1]) == 17:
    RandomAnchoringBiasConditioningWithResources.callTest()
elif int(sys.argv[1]) == 18:
    RandomAnchoringBiasLexRevision.callTest()
elif int(sys.argv[1]) == 19:
    RandomAnchoringBiasLexRevisionWithResources.callTest()
elif int(sys.argv[1]) == 20:
    RandomAnchoringBiasMinRevision.callTest()
elif int(sys.argv[1]) == 21:
    RandomAnchoringBiasMinRevisionWithResources.callTest()
elif int(sys.argv[1]) == 22:
    RandomInGroupFavoritismConditioning.callTest()
elif int(sys.argv[1]) == 23:
    RandomInGroupFavoritismLexRevision.callTest()
elif int(sys.argv[1]) == 24:
    RandomInGroupFavoritismMinRevision.callTest()

