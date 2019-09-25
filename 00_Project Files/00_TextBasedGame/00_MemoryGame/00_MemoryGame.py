"""
Author: Nate K
Date of Creation: 09/13/2019
Date of Last Edit: 09/25/2019
Text-Based Game Project
SOURCES: 
- https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
- https://stackoverflow.com/questions/46425645/python-make-every-character-line-random-color-print
- https://stackoverflow.com/questions/24582233/python-flush-input-before-raw-input

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 09/26/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

I separately coded the game itself and the beginning sequence of the game from eachother in order to organize the code better before bringing the two together.

Once each stage was completed separately, I was able to seemlessly combine the two. Some debugging was needed, but after enough time, all the kinks of the program were worked out.

I had one main goal after completing the game: adding color to the output text. It took awhile to find the correct library, but I finally figured out how to install colorama and how to use the library properly.

One of the biggest issues that I encountered was early user-input that was used to cheat the game. Users were able to type the letters that they were supposed to memorize immediately, and when prompted to enter the string, they could just press [enter] without actually remembering the string. This also took awhile to figure out but I found a stackoverflow block of code that was useful in flushing the user-input.
"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# SETUP FUNCTIONS
import os, string, time, random,sys, termios
import colorama
from colorama import Fore, Back, Style

#clear terminal screen, from stackoverflow.com
def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear')

#countdown function used many times throughout the game
def countdown321(): 
	print("3...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("1...")
	time.sleep(1)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME INITIALIZATION/INSTRUCTIONS
def startInstructions(error_status):
	clearTerminal()

	#if something other than yes was entered when prompted
	if error_status == True:
		#"Back.YELLOW" sets the background of the text to yellow, "Style.RESET_ALL" is used to reset the text backgruond color before printing other text
		print(Back.YELLOW + "ERROR: expecting 'y' or 'yes' or 'yeah'\n\n" + Style.RESET_ALL)
		error_status = False

	#game instructions
	print("Hello! Welcome to the Game of Memory. \nThis game will test the limits to which you can remember a series of characters.\nYou will see a character printed, and each level increases in difficulty.")
	print("\n\nInstructions:\n> When prompted, enter the characters in the exact order they appeared\n> When inputting the string of chracters, be aware of capital/lower case letters (i.e. this game is CASE-SENSETIVE)")
	startGame()

#prompt for user, ready to play?
def startGame():
	instructions_UR = input("\n\nAre you ready to play?\n>> ").lower().replace(" ", "")
	if instructions_UR == "yes" or instructions_UR == "yeah" or instructions_UR == "y" or instructions_UR == "ye":
		print("\nGame starting in:")
		countdown321()
		memoryPrint(1)
	else:
		startInstructions(True)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# PRINT - MEMORY GAME
def memoryPrint(level):
	#level variable used to print X number of letters
	init_level = level 

	#print # of letters according to level #
	while (level > 0):
		clearTerminal()

		#print random character, from stackoverflow.com
		printChar = random.choice(string.ascii_letters)
		
		if init_level > 7:
			#random colors + even faster print start at level 8, sourced from stackoverflow
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar]
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			#give .25 second of viewing time before clearing screen again
			time.sleep(.25)
		elif init_level > 5:
			#random colors + faster print start at level 4
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar]
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			time.sleep(.5)
		elif init_level > 3:
			#random colors start at level 4
			colors = list(vars(colorama.Fore).values())
			colored_chars = [random.choice(colors) + printChar]
			print(random.choice(colors) + printChar + Style.RESET_ALL)
			time.sleep(1)
		elif init_level >= 1:
			print(printChar)
			time.sleep(1)


		if init_level == level:
			#(1st time), store character into variable "printMemory"
			printMemory = printChar
		else: 
			#(after 1st time), append character to variable "printMemory"
			printMemory = printMemory + printChar
		
		#clear terminal after showing character
		clearTerminal()
		time.sleep(.5)
		level -= 1
	if level == 0:
		#send printMemory + init_level to memoryCheck function
		memoryCheck(printMemory, init_level)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# MEMORY CHECK - MEMORY GAME
def memoryCheck(printMemory, init_level):
	#flush user-input, sourced from stackoverflow
	termios.tcflush(sys.stdin, termios.TCIOFLUSH)
	clearTerminal()

	#user inputs memorized string
	memory_UR = input("Please input the characters in the exact order that they appeared:\n").replace(" ", "")

	#user inputs string correctly!
	if memory_UR == printMemory:
		#"Back.GREEN" is used to set the background of the text green
		print(Back.GREEN + "\nCongrats! You've passed level", init_level, Style.RESET_ALL + "\n\nAdvancing to level", init_level+1,"in:")
		countdown321()
		memoryPrint(init_level + 1)
	#user inputs string incorrectly!
	else:
		print(Back.YELLOW + "I'm sorry, but you didn't remember the string correctly.", Style.RESET_ALL+ "\n\nThis is what you inputted:" + Style.RESET_ALL)
		print(memory_UR)
		print("This is what it was supposed to look like:")
		print(printMemory)

		gameRetry_UR = input("Would you like to play again?\n").lower().strip()
		if gameRetry_UR == "yes" or gameRetry_UR == "yeah":
			print("\n\nYay! Returnig to level 1...")
			countdown321()
			memoryPrint(1)
		else:
			print("\n\nThanks for playing! Have a good day.\nGAME CREATED BY: Nate Krauss '20")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME START FUNCTION
startInstructions(False)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
'''
PEER-REVIEW COMMENTS


CHANDLER: I think this was really good! Definitely appropriate difficulty... I didn't make it past level 4 but from looking at your code it looks like it gets even harder. The only trip-up I had was the sleep in between the beginning of the level and when "Please input..." appears. I accidentally entered the same character twice a few times. Maybe I'm just stupid (probably) but even so, might be cool to make the game idiot-proof
RESPONSE: The trip-up that you have referenced happens easily and can actually be used to cheat the game. However, I have found a way to flush the user-input before they are prompted to enter the memorized string.

SPENCER: I am able to type as the letters appear. Once you enter your answer, could there be a pause for dramatic effect? I like the colors tho NGL. Keep up the good work plz
RESPONSE: Yes, you are able to type the letters as they appear and will always be able to do that. However, user-input is now flushed as stated before. I like the idea of the pause, but I would rather prefer the user to have the instant-gratification of winning the round/level. 

STAN: Cool game, I just hope it is a little easier to identify the x from the X, or o from the O.
RESPONSE: I like the difficulty it adds to the game, just makes it harder for the user!

KATE: I really like how your game is simple, but still challenging! One tiny thing I would maybe clarify in the instructions is that the answers need to be case-sensitive. I didn't really get that until my 3rd time around, which is definitely my fault but hey, why not? I really like the colors and how the screen clears after every round
RESPONSE: Thanks for the advice! I added your comment to the game instructions at the beginning of the game. 

'''