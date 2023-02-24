from asyncore import file_dispatcher
from audioop import bias
from operator import imod
from os import stat
from re import A
from random import randint

from pytest import Testdir
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
from Tests import LengthAgainstPerformanceTest, CustomConfirmationBiasLexRevision, RandomInGroupFavoritismMinRevision, RandomInGroupFavoritismLexRevision, RandomInGroupFavoritismConditioning, RandomAnchoringBiasMinRevisionWithResources, RandomAnchoringBiasMinRevision, RandomAnchoringBiasLexRevisionWithResources, RandomAnchoringBiasLexRevision, RandomAnchoringBiasConditioningWithResources, RandomAnchoringBiasConditioning, RandomFramingBiasMinRevision, RandomFramingBiasLexRevision, RandomFramingBiasConditioning, RandomConfirmationBiasMinRevision, RandomConfirmationBiasLexRevision, RandomConfirmationBiasConditioning, CustomAnchoringBiasMinRevision, CustomAnchoringBiasLexRevision, CustomAnchoringBiasConditioning, CustomFramingBiasMinRevision, CustomFramingBiasLexRevision, CustomConfirmationBiasConditioning, CustomConfirmationBiasConditioning, CustomConfirmationBiasMinRevision, CustomFramingBiasConditioning



if len(sys.argv) == 1:
    print("""Enter 1 to choose CustomConfirmationBiasConditioning
Enter 2 to choose CustomConfirmationBiasLexRevision
Enter 3 to choose CustomConfirmationBiasMinRevision
Enter 4 to choose CustomFramingBiasConditioning
Enter 5 to choose CustomFramingBiasLexRevision
Enter 6 to choose CustomFramingBiasMinRevision
Enter 7 to choose CustomAnchoringBiasConditioning
Enter 8 to choose CustomAnchoringBiasLexRevision
Enter 9 to choose CustomAnchoringBiasMinRevision
Enter 10 to choose RandomConfirmationBiasConditioning
Enter 11 to choose RandomConfirmationBiasLexRevision
Enter 12 to choose RandomConfirmationBiasMinRevision
Enter 13 to choose RandomFramingBiasConditioning
Enter 14 to choose RandomFramingBiasLexRevision
Enter 15 to choose RandomFramingBiasMinRevision
Enter 16 to choose RandomAnchoringBiasConditioning
Enter 17 to choose RandomAnchoringBiasConditioningWithResources
Enter 18 to choose RandomAnchoringBiasLexRevision
Enter 19 to choose RandomAnchoringBiasLexRevisionWithResources
Enter 20 to choose RandomAnchoringBiasMinRevision
Enter 21 to choose RandomAnchoringBiasMinRevisionWithResources
Enter 22 to choose RandomInGroupFavoritismConditioning
Enter 23 to choose RandomInGroupFavoritismLexRevision
Enter 24 to choose RandomInGroupFavoritismMinRevision""")
    testIndex = int(input("Give a number between 1 and 24 to choose a test case: "))
    if testIndex == 1:
        CustomConfirmationBiasConditioning.callTest()  
    elif testIndex == 2:
        CustomConfirmationBiasLexRevision.callTest()
    elif testIndex == 3:
        CustomConfirmationBiasMinRevision.callTest()
    elif testIndex == 4:
        CustomFramingBiasConditioning.callTest()
    elif testIndex == 5:
        CustomFramingBiasLexRevision.callTest()
    elif testIndex == 6:
        CustomFramingBiasMinRevision.callTest()
    elif testIndex == 7:
        CustomAnchoringBiasConditioning.callTest()
    elif testIndex == 8:
        CustomAnchoringBiasLexRevision.callTest()
    elif testIndex == 9:
        CustomAnchoringBiasMinRevision.callTest()
    elif testIndex == 10:
        RandomConfirmationBiasConditioning.callTest()
    elif testIndex == 11:
        RandomConfirmationBiasLexRevision.callTest()
    elif testIndex == 12:
        RandomConfirmationBiasMinRevision.callTest()
    elif testIndex == 13:
        RandomFramingBiasConditioning.callTest()
    elif testIndex == 14:
        RandomFramingBiasLexRevision.callTest()
    elif testIndex == 15:
        RandomFramingBiasMinRevision.callTest()
    elif testIndex == 16:
        RandomAnchoringBiasConditioning.callTest()
    elif testIndex == 17:
        RandomAnchoringBiasConditioningWithResources.callTest()
    elif testIndex == 18:
        RandomAnchoringBiasLexRevision.callTest()
    elif testIndex == 19:
        RandomAnchoringBiasLexRevisionWithResources.callTest()
    elif testIndex == 20:
        RandomAnchoringBiasMinRevision.callTest()
    elif testIndex == 21:
        RandomAnchoringBiasMinRevisionWithResources.callTest()
    elif testIndex == 22:
        RandomInGroupFavoritismConditioning.callTest()
    elif testIndex == 23:
        RandomInGroupFavoritismLexRevision.callTest()
    elif testIndex == 24:
        RandomInGroupFavoritismMinRevision.callTest() 
elif int(sys.argv[1]) == 1:
    CustomConfirmationBiasConditioning.callTest()
elif int(sys.argv[1]) == 2:
    CustomConfirmationBiasLexRevision.callTest()
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

#LengthAgainstPerformanceTest.callTest()
