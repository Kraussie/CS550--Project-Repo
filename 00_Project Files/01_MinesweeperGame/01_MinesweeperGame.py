"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/14/2019
Minesweeper Game
SOURCES: 
- https://docs.python.org/3/library/sys.html
- https://stackoverflow.com/questions/26853453/how-to-ignore-an-indexerror-on-python
- https://stackoverflow.com/questions/24582233/python-flush-input-before-raw-input

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 10/14/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

Most of the code was originally created myself, but once we did some examples in class, I reformatted my code to fit the example code. This made the following work on my code much easier. I borrowed some functions like the os.system('clear') and the countdown321() from previous projects. I also borrowed my knowledge of colorama to color code various aspects of the minesweeper game. 

Using Ms. Healey's review of my draft game, I fixed many aspects of my game/code that was lacking. For example, I limited the size of the board and # of bombs; I moved the "main code" to the bottom of the code; I compartmentalized the "user guess" function; added a play again feature; and allowed the user to guess without entering "g".

"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random, colorama, os, time, termios
from colorama import Fore, Back, Style

# print board function
def printBoard(board):
	os.system('clear')

	#create new board for printing purposes, uses color
	colorBoard = board
	for row in range(1, yLen-1):
		for col in range(1, xLen-1):
			if colorBoard[row][col] == '⚐':
				colorBoard[row][col] = Fore.RED+'⚐'+Style.RESET_ALL
			elif colorBoard[row][col] == '█':
				colorBoard[row][col] = Style.DIM+'█'+Style.RESET_ALL

	for row in colorBoard[1:-1]:
		print(*row[1:-1])

#countdown function
def countdown321(): 
	print("3...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("1...")
	time.sleep(1)
	#flush user-input, sourced from stackoverflow
	termios.tcflush(sys.stdin, termios.TCIOFLUSH)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME INTRO [IN-COMPLETE]
def gameIntro():
	os.system('clear')
	print(Style.DIM+"*************************\n*                       *\n*      "+Style.RESET_ALL+Fore.YELLOW+"WELCOME TO:"+Style.RESET_ALL+Style.DIM+"      *\n*     "+Style.RESET_ALL+Style.BRIGHT+Fore.RED+"*MINESWEEPER*"+Style.RESET_ALL+Style.DIM+"     *\n*                       *\n*    "+Style.RESET_ALL+"BY: NATE K '20"+Style.RESET_ALL+Style.DIM+"     *\n*                       *\n*                       *\n*************************\n\n\n"+Style.RESET_ALL)
	input("Press [enter] to start the game\n>> ")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOARD SETUP [COMPLETE]
def boardSetup(board):
	# add zeroes to field
	for r in range(1, yLen-1):
		for c in range(1, xLen-1):
			board[r][c] = 0
	
	# randomly place bombs within playing field
	for i in range(numBombs):
		# random coords selection
		x = random.randint(1, xLen-2)
		y = random.randint(1, yLen-2)

		# if random coords are already a bomb, create a new set of coords
		while board[y][x] == '*':
			x = random.randint(1, xLen-2)
			y = random.randint(1, yLen-2)

		# change coord into a bomb
		board[y][x] = '*'

		# continue to next function, add 1 to nearby grid areas
		bombSurroundCount(x, y, board)

# *+*+*+*+*+*+*+*+*+*+*+
# COUNT NEIGHBOR BOMBS [COMPLETE]
def bombSurroundCount(x,y,board):
	# add 1 to all the grid areas surrounding a placed bomb
	for r in range(y-1, y+2):
		for c in range(x-1, x+2):
			if board[r][c] != '*' and board[r][c] != '#':
				board[r][c] += 1

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# ACCEPT USER INPUT [IN-COMPLETE]
def userGuess(solBoard, userBoard):
	# var to keep track of # of bombs found
	unopenedCells = 0

	while 1 == 1:
		# display current user display board
		printBoard(userBoard)

		# error checking if coordinates aren't entered correctly
		try:
			# user inputs coords: example is '4 3 flag'
			urGUESS = input("\n\n\nPlease enter your guess coordinates (ex: X Y [f]):\n>> ").split(" ")
			urXguess = int(urGUESS[0])
			urYguess = int(urGUESS[1])
		except ValueError:
			print(Fore.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL+"\nReturning to the game in...")
			countdown321()
			continue
		except IndexError:
			print(Fore.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL+"\nReturning to the game in...")
			countdown321()
			continue

		# error checking if flag argument isn't found
		try:
			# user can flag coordinates if they suspect a bomb is at those coords
			if urGUESS[2] == 'f' or urGUESS[2] == 'flag':
				userFlag(userBoard,urYguess,urXguess)
		except IndexError:
			# if a flag argument isn't found, continue
			if solBoard[urYguess][urXguess] == '*':
				os.system('clear')
				print(Fore.RED+"YOU BLEW UP!!!"+Style.RESET_ALL)
				playAgainUR = input("\n\n\nWould you like to play again?\n>> ")
				if playAgainUR == "yes" or playAgainUR == "yeah" or playAgainUR == "y":
					playGame()
				else:
					print("\nWell...thanks for playing!")
					break
			else:
				guessCheck(userBoard,solBoard,urYguess,urXguess)

		#check number of unopened cells
		for row in range(1, yLen-1):
			for col in range(1, xLen-1):
				if userBoard[row][col] == '⚐' and solBoard[row][col] == '*':
					unopenedCells += 1
				if userBoard[row][col] == Style.DIM+'█'+Style.RESET_ALL:
					unopenedCells += 1
		
		# win condition check at end of each round, if # of unopened cells is = to the number of bombs, user has won the game
		if unopenedCells == numBombs:
			printBoard(userBoard)
			print("\n\n\n"+Back.GREEN+"CONGRATULATIONS! YOU WON!"+Style.RESET_ALL)
			playAgainUR = input("\n\n\nWould you like to play again?\n>> ")
			if playAgainUR == "yes" or playAgainUR == "yeah" or playAgainUR == "y":
				playGame()
			else:
				print("\nWell...thanks for playing!")
				break
		else:
			# reset the number of unopened cells if win condition is not satisfied
			unopenedCells = 0

def userFlag(userBoard,urYguess,urXguess):
	if userBoard[urYguess][urXguess] == Fore.RED+'⚐'+Style.RESET_ALL:
		userBoard[urYguess][urXguess] = '█'
	elif userBoard[urYguess][urXguess] != Fore.RED+'⚐'+Style.RESET_ALL:
		userBoard[urYguess][urXguess] = '⚐'

def guessCheck(userBoard,solBoard,urYguess,urXguess):
	# if coord selection is = 0, then continue to display surrounding blocks
	if solBoard[urYguess][urXguess] == 0:
		userBoard[urYguess][urXguess] = solBoard[urYguess][urXguess]
						
		# REVEAL ALL ZEROES CONNECTED TO X,Y GUESS [NEW]
		revealLater = [[urYguess,urXguess]]
		while len(revealLater) > 0:
			# remove first value in revealLater list and store in 'revealCoord' var
			revealCoord = revealLater.pop(0)

			for r in range(revealCoord[0]-1, revealCoord[0]+2):
				for c in range(revealCoord[1]-1,revealCoord[1]+2):
					# if zero around X,Y guess = 0, add to reveal Later list
					if solBoard[r][c] == 0 and userBoard[r][c] != solBoard[r][c] and solBoard[r][c] != '*' and solBoard != '#':
						revealLater.append([r,c])

					userBoard[r][c] = solBoard[r][c]
	# if coord selection isn't = 0, only display that specific block
	else:
		userBoard[urYguess][urXguess] = solBoard[urYguess][urXguess]

def playGame():
	# create the solution and user display boards
	solBoard = [['#']*xLen for i in range(yLen)]
	userBoard = [['█' for x in range(xLen)] for y in range(yLen)]
	
	gameIntro()
	boardSetup(solBoard)
	userGuess(solBoard,userBoard)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME START
try:
	# accept cmnd line arguments when running program, sourced from python.org
	xLen = int(sys.argv[1]) + 2
	yLen = int(sys.argv[2]) + 2
	numBombs = int(sys.argv[3])

	# board check
	if int(sys.argv[1])*int(sys.argv[2]) <= numBombs:
		print(Fore.RED+"ERROR, there are too many bombs being placed on the field"+Style.RESET_ALL)
	elif xLen >= 52 or yLen >= 52:
		print(Fore.RED+"ERROR, the max field perimeter is 50x50"+Style.RESET_ALL)
	else:
		playGame()
except IndexError:
	# deal with error when first running the program, likely due to forgetting the arguments or inputting arguments incorectly, sourced/researched from stackoverflow.com; Back.RED and Style.RESET_ALL changes the error text to red to make it easier to see for the user
	print(Fore.RED+"ERROR, Please enter a valid width, height, and number of bombs"+Style.RESET_ALL)