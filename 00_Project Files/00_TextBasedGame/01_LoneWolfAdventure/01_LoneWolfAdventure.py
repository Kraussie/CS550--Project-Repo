# Author: Nate K
# Date of Creation: 09/18/2019
# Date of Last Edit: 09/18/2019
# Text-Based Game Project
# SOURCES: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/26/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME SETUP
import random, os

def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear') #clear terminal screen, from stackoverflow.com

def initStory():
	cSkill = random.randint(1,9) + 10 # combat skill
	eSkill = random.randint(1,9) + 20 # endurance skill
	# kaiDiscipline = ?, need to figure out how to store kai discipline selection
	# weapons = ?, how to store weaposn
	meals = 1
	backpackSize = meals #max items in backpack = 8 items, including meals
	goldCrowns = random.randint(1,9) # rand amnt of money, max = 50 crowns
	# find one random item, store in inventory

class Backpack():
	def __init__(self, name, combatAdd, endAdd):
		self.name = name
		self.combatAdd = combatAdd
		self.endAdd = endAdd

class SpecialItemsInv():
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

class KaiSkills():
	def __init__(self, name, desc, combatAdd, endAdd)
		self.name = name
		self.desc = desc
		self.combatAdd = combatAdd
		self.endAdd = endAdd

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# STORY SETUP
def storyIntro():
	#print the intro to the Lone Wolf Book
	clearTerminal()
	storyIntroText = open("StorySoFar.txt","r")
	print(storyIntroText.read())

def gameRules():

def equipSelection():
	print("You are dressed in the green tunic and cloak of a Kai initiate. You have little with you to arm yourself for survival.")
	print("All you possess is an Axe and a Backpack containing 1 Meal. Hanging from your waist is a leather pouch containing Gold Crowns.")
	print("You discover amongst the smoking ruins of the monastery, a Map of Sommerlund showing the capital city of Holmgard and the land of Durenor, far to the east. You place the Map inside your tunic for safety.")
	print("\n\n\nYou also find one of the following:\n1) Sword (Weapons)\n2) Helmet (Special Items. This adds 2 Endurance points to ")