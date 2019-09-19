# Author: Nate K
# Date of Creation: 09/18/2019
# Date of Last Edit: 09/18/2019
# Text-Based Game Project
# SOURCES: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/26/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME SETUP
import random

def initStory():
	cSkill = random.randint(1,9) + 10 # combat skill
	eSkill = random.randint(1,9) + 20 # endurance skill
	# kaiDiscipline = ?, need to figure out how to store kai discipline selection
	# weapons = ?, how to store weaposn
	meals = 1
	backpackSize = 8 #max items in backpack = 8 items, including meals
	goldCrowns = random.randint(1,9) # rand amnt of money, max = 50 crowns
	# find one random item, store in inventory

class Item(object):
	def __init__(self, name, combatAdd, endAdd)

class kaiDiscripline(discipline):
	def __init__(self, name, combatAdd, endAdd)
