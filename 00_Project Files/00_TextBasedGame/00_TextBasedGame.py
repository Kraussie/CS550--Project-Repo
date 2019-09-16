# Author: Nate K
# Date of Creation: 09/13/2019
# Date of Last Edit: 09/16/2019
# Text-Based Game Project
# SOURCES: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/26/2019

# I began programming this program in two different files initally.
# I wanted to separate the initalization part of the game from the game itself in order to organize the code a lot better before combining the two. 
# Once each stage was completed separately, I was able to seemlessly combine the two. Some debugging was needed, but after enough time, all the kinks of the program were worked out.

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# SETUP FUNCTIONS
import os, string, time, random

def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear') #clear terminal screen, from stackoverflow.com

def countdown321():
	print("3...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("1...")
	time.sleep(1)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# GAME INITIALIZATION/INSTRUCTIONS
def startInstructions(error_status):
	clearTerminal()
	if error_status == True:	
		print("ERROR: expecting 'yes' or 'yeah'\n\n")
		error_status = False
	print("Hello! Welcome to the Game of Memory. \nThis game will test the limits to which you can remember a series of characters.\nYou will see a character printed, and each level increases in difficulty.")
	print("\n\n**NOTICE: Be careful not to input any characters before you are prompted**")
	startGame()

def startGame():
	instructions_UR = input("\n\nAre you ready to play?\n")
	if instructions_UR == "yes" or instructions_UR == "yeah":
		print("\nGame starting in:")
		countdown321()
		memoryPrint(1)
	else:
		startInstructions(True)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PRINT - MEMORY GAME
def memoryPrint(level):
	init_level = level
	level = init_level
	while (level > 0):
		clearTerminal()
		printChar = random.choice(string.ascii_letters) #print random character, from stackoverflow.com
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

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# MEMORY CHECK - MEMORY GAME
def memoryCheck(printMemory, init_level):
	clearTerminal()
	memory_UR = input("Please input the characters in the exact order that they appeared:\n").replace(" ", "")

	if memory_UR == printMemory:
		print("\nCongrats! You've passed level", init_level,"\n\nAdvancing to level", init_level+1,"in:")
		countdown321()
		memoryPrint(init_level + 1)
	else:
		print("I'm sorry, but you didn't remember the string correctly.\n\nThis is what you inputted:")
		print(memory_UR)
		print("This is what it was supposed to look like:")
		print(printMemory)

		gameRetry_UR = input("Would you like to play again?\n")
		if gameRetry_UR == "yes" or gameRetry_UR == "yeah":
			print("\n\nYay! Returnig to level 1...")
			memoryPrint(1)
		else:
			print("\n\nThanks for playing! Have a good day.\nGAME CREATED BY: Nate Krauss '20")

# GAME START FUNCTION
startInstructions(False)


