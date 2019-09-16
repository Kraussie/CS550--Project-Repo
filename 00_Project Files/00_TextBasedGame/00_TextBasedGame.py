# Author: Nate K
# Date of Creation: 09/13/2019
# Date of Last Edit: 09/16/2019
# Text-Based Game Project
# SOURCES: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/26/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# SETUP FUNCTIONS
import os, string, time, random

def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear') #clear terminal screen

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME INSTRUCTIONS
def startInstructions(error_status):
	clearTerminal()
	if error_status == True:	
		print("ERROR: expecting 'yes' or 'yeah'\n\n")
		error_status = False
	print("Hello! Welcome to the Game of Memory. \nThis game will test the limits to which you can remember a series of characters.\nYou will see a character printed, and each level increases in difficulty.")
	startGame()

def startGame():
	instructions_UR = input("\n\nAre you ready to play?\n")
	if instructions_UR == "yes" or instructions_UR == "yeah":
		memoryPrint(1)
	else:
		startInstructions(True)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# MEMORY GAME
def memoryPrint(level):
	init_level = level
	level = init_level
	while (level > 0):
		clearTerminal()
		printChar = random.choice(string.ascii_letters) #print random character
		print(printChar)
		if init_level == level:
			printMemory = printChar #(1st time), store character into variable "printMemory"
		else: 
			printMemory = printMemory + printChar #(after 1st time), append character to variable "printMemory"
		
		time.sleep(1) #give 1 second of viewing time before clearing screen again
		clearTerminal() #clear terminal after showing character
		time.sleep(.5)
		level -= 1
	if level == 0:
		memoryCheck(printMemory, init_level)


def memoryCheck(printMemory, init_level):
	clearTerminal()
	memory_UR = input("Please input the characters in the exact order that they appeared:\n").replace(" ", "")

	if memory_UR == printMemory:
		print("\nCongrats! You've passed level", init_level,"\n\nAdvancing to level", init_level+1, "\nin 3...")
		time.sleep(1)
		print("2...")
		time.sleep(1)
		print("1...")
		time.sleep(1)
		memoryPrint(init_level + 1)
	else:
		print("I'm sorry, but you didn't remember the string correctly.\n\nThis is what it was supposed to look like:\n", printMemory)

		gameRetry_UR = input("Would you like to play again?\n")
		if gameRetry_UR == "yes" or gameRetry_UR == "yeah":
			print("Yay! Returnig to level 1...")
			memoryPrint(1)
		else:
			print("Thanks for playing! Have a good day.\nGAME CREATED BY: Nate Krauss '20")


# GAME START FUNCTION
startInstructions(False)


