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
import colorama
from colorama import Fore, Back, Style

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
		print(Back.RED + "ERROR: expecting 'yes' or 'yeah'\n\n" + Style.RESET_ALL)
		error_status = False
	print("Hello! Welcome to the Game of Memory. \nThis game will test the limits to which you can remember a series of characters.\nYou will see a character printed, and each level increases in difficulty.")
	print(Back.RED + "\n\n**NOTICE: Be careful not to input any characters before you are prompted**" + Style.RESET_ALL)
	print("\n\nInstructions:\n> When prompted, enter the characters in the exact order they appeared\n> When inputting the string of chracters, be aware of capital/lower case letters (i.e. this game is CASE-SENSETIVE)")
	startGame()

def startGame():
	instructions_UR = input("\n\nAre you ready to play?\n>> ").lower()
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
		
		if init_level > 7:
			#random colors + even faster print start at level 4
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar] #sourced from stackoverflow
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			time.sleep(.25) #give 1 second of viewing time before clearing screen again
		elif init_level > 5:
			#random colors + faster print start at level 4
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar] #sourced from stackoverflow
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			time.sleep(.5) #give 1 second of viewing time before clearing screen again
		elif init_level > 3:
			#random colors start at level 4
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar] #sourced from stackoverflow
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			time.sleep(1) #give 1 second of viewing time before clearing screen again
		elif init_level >= 1:
			print(printChar)
			time.sleep(1) #give 1 second of viewing time before clearing screen again


		if init_level == level:
			printMemory = printChar #(1st time), store character into variable "printMemory"
		else: 
			printMemory = printMemory + printChar #(after 1st time), append character to variable "printMemory"
		
		clearTerminal() #clear terminal after showing character
		time.sleep(.5)
		level -= 1
	if level == 0:
		memoryCheck(printMemory, init_level)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# MEMORY CHECK - MEMORY GAME
def memoryCheck(printMemory, init_level):
	clearTerminal()
	input("Click return when you are ready to enter the string!\n[ENTER]")

	clearTerminal()
	memory_UR = input("Please input the characters in the exact order that they appeared:\n").replace(" ", "")

	if memory_UR == printMemory:
		print(Back.GREEN + "\nCongrats! You've passed level", init_level, Style.RESET_ALL + "\n\nAdvancing to level", init_level+1,"in:")
		countdown321()
		memoryPrint(init_level + 1)
	else:
		print(Back.RED + "I'm sorry, but you didn't remember the string correctly.", Style.RESET_ALL+ "\n\nThis is what you inputted:" + Style.RESET_ALL)
		print(memory_UR)
		print("This is what it was supposed to look like:")
		print(printMemory)

		gameRetry_UR = input("Would you like to play again?\n")
		if gameRetry_UR == "yes" or gameRetry_UR == "yeah":
			print("\n\nYay! Returnig to level 1...")
			countdown321()
			memoryPrint(1)
		else:
			print("\n\nThanks for playing! Have a good day.\nGAME CREATED BY: Nate Krauss '20")

# GAME START FUNCTION
startInstructions(False)

# PEER-REVIEW COMMENTS
# I think this was really good! Definitely appropriate difficulty... I didn't make it past level 4 but from looking at your code it looks like it gets even harder.
# The only trip-up I had was the sleep in between the beginning of the level and when "Please input..." appears. I accidentally entered the same character twice a few times.
# Maybe I'm just stupid (probably) but even so, might be cool to make the game idiot-proof
# - Chandler

"""
Spencer:
I am able to type as the letters appear
Once you enter your answer, could there be a pause for dramatic effect?
I like the colors tho NGL
Keep up the good work plz
Stan:
Cool game, I just hope it is a little easier to identify the x from the X, or o from the O.
Kate: 
I really like how your game is simple, but still challenging! One tiny thing I would maybe clarify in the instructions is that the answers need to be case-sensitive.
I didn't really get that until my 3rd time around, which is definitely my fault but hey, why not? I really like the colors and how the screen clears after every round
"""

