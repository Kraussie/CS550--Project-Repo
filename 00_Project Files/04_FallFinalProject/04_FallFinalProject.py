# Author: Nate K
# Date of Creation: 11/07/2019
# Date of Last Edit: 11/07/2019
# Fall Final Project
# SOURCES/USEFUL LINKS:

#PREREQUESITES:
#- NEED LIBRARY: "colorama"

#How to install "colorama":
#- CMND IN TERMINAL: "pip install colorama"

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 11/20/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME SETUP/UNIVERSAL FUNCTIONS
import random, os
from colorama import Fore, Back, Style

def clearTerminal():
	#clear terminal screen, from stackoverflow.com
	os.system('cls' if os.name == 'nt' else 'clear')

def enterContinue(nextSection):
	if nextSection == 0:
		input("\n\n>> Click [enter] to continue")
	else:
		input(print("\n\n>> Click [enter] to continue to the", nextSection,"\n>> "))
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME INTRO SCREEN
def gameWelcome():
	clearTerminal()
	print(Style.DIM+"*******************************\n*                             *\n*           "+Style.RESET_ALL+Fore.YELLOW+"WELCOME"+Style.RESET_ALL+Style.DIM+"           *\n*             "+Style.RESET_ALL+Fore.YELLOW+"TO"+Style.RESET_ALL+Style.DIM+"              *\n*        "+Style.RESET_ALL+Fore.YELLOW+"THE LONE WOLF"+Style.RESET_ALL+Style.DIM+"        *\n*                             *\n*         "+Style.RESET_ALL+"CREATED BY:"+Style.DIM+"         *\n*       "+Style.RESET_ALL+"NATE KRAUSS'20"+Style.DIM+"        *\n*                             *\n*******************************"+Style.RESET_ALL)
	enterContinue("Game Introduction")

def storyIntro():
	clearTerminal()
	storyIntroText = open("StorySoFar.txt","r")
	print(storyIntroText.read())
	enterContinue("Game Rules")
	storyRules()

def storyRules():
	clearTerminal()
	print("You keep a record of your adventure on the Action Chart.")
	enterContinue("Action Chart Selection")

	#COMBAT AND ENDURANCE SKILL SELECTION
	print("During your training as a Kai Lord you have developed fighting prowess — COMBAT SKILL and physical stamina — ENDURANCE. Before you set off on your adventure you need to measure how effective your training has been.")
	enterContinue(0)
	cSkill = random.randint(1,9) + 10 # combat skill
	eSkill = random.randint(1,9) + 20 # endurance skill
	print("You're combat skill and endurance have been randomly chosen to be:\n[COMBAT SKILL] =", cSkill,"\n[ENDURANCE] =", eSkill)
	enterContinue(0)
	print("If you are wounded in combat you will lose ENDURANCE points. If at any time your ENDURANCE points fall to zero or below, you are dead and the adventure is over. Lost ENDURANCE points can be regained during the course of the adventure, but your number of ENDURANCE points can never go above the number with which you start your adventure.")
	enterContinue(0)

	#KAI DISCIPLINES
	print("Over the centuries, the Kai monks have mastered the skills of the warrior. These skills are known as the Kai Disciplines, and they are taught to all Kai Lords. You have learnt only five of the skills listed below. The choice of which five skills these are, is for you to make. As all of the Disciplines may be of use to you at some point on your perilous quest, pick your five with care. The correct use of a Discipline at the right time can save your life.\n\n You may choose 5 Disciplines")

gameWelcome()
