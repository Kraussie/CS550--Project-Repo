"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/07/2019
Minesweeper Game
SOURCES: 
- https://docs.python.org/3/library/sys.html
- https://stackoverflow.com/questions/26853453/how-to-ignore-an-indexerror-on-python

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 10/07/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random, colorama, os
from colorama import Fore, Back, Style

try:
	# accept cmnd line arguments when running program, sourced from python.org
	xLen = int(sys.argv[1]) + 2
	yLen = int(sys.argv[2]) + 2
	numBombs = int(sys.argv[3])

	# create the solution and user display boards
	solBoard = [[0]*xLen for i in range(yLen)]
	userBoard = [['█' for x in range(xLen)] for y in range(yLen)]
except IndexError:
	# deal with error when first running the program, likely due to forgetting the arguments or inputting arguments incorectly, sourced/researched from stackoverflow.com; Back.RED and Style.RESET_ALL changes the error text to red to make it easier to see for the user
	print(Back.RED+"ERROR, Please enter a valid width, height, and number of bombs"+Style.RESET_ALL)

# print board function
def printBoard(board):
	os.system('clear')
	for row in board[1:-1]:
		print(*row[1:-1])

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOARD SETUP
def boardSetup(board):
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
# COUNT NEIGHBOR BOMBS
def bombSurroundCount(x,y,board):
	# add 1 to all the grid areas surrounding a placed bomb
    for r in range(y-1, y+2):
        for c in range(x-1, x+2):
            if board[r][c] != '*':
                board[r][c] += 1

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# ACCEPT USER INPUT
def userGuess(solBoard, userBoard):
	# var to keep track of # of bombs found
	unopenedCells = 0

	while 1 == 1:
		# display current user display board
		printBoard(userBoard)

		# try/except to deal with input errors
		try:
			# user inputs coords: example is '4 3 flag'
			urGUESS = input("\n\n\nPlease enter your guess coordinates (ex: X Y f or 0 1 g):\n>>").split(" ")
			urXguess = int(urGUESS[1]) + 1
			urYguess = int(urGUESS[0]) + 1

			# user can flag coordinates if they suspect a bomb is at those coords
			if urGUESS[2] == 'f' or urGUESS[2] == 'flag':
				if userBoard[urXguess][urYguess] == '⚐':
					userBoard[urXguess][urYguess] = '█'
				elif userBoard[urXguess][urYguess] != '⚐':
					userBoard[urXguess][urYguess] = '⚐'
			# user can reveal a coordinate, if it is a bomb, they immediately die, if it isn't a bomb, then the space is revealed
			elif urGUESS[2] == 'g' or urGUESS[2] == 'guess':
				if solBoard[urXguess][urYguess] == '*':
					os.system('clear')
					print(Back.RED+"YOU DIED"+Style.RESET_ALL)
					break
				else:
					# if coord selection is = 0, then continue to display surrounding blocks
					if solBoard[urXguess][urYguess] == 0:
						userBoard[urXguess][urYguess] = solBoard[urXguess][urYguess]
						# function to display surrounding block
					# if coord selection isn't = 0, only display that specific block
					else:
						userBoard[urXguess][urYguess] = solBoard[urXguess][urYguess]

			# count # of unopened cells
			for row in range(1, yLen-1):
				for col in range(1, xLen-1):
					if userBoard[row][col] == '█':
						unopenedCells += 1

			# win condition check at end of each round, if # of unopened cells is = to the number of bombs, user has won the game
			if unopenedCells == numBombs:
				printBoard(userBoard)
				print("\n\n\n"+Back.GREEN+"CONGRATULATIONS! YOU WON!"+Style.RESET_ALL)
				break
			else:
				# reset the number of unopened cells if win condition is not satisfied
				unopenedCells = 0
		# deal with error when user inputs something wrong
		except IndexError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue
		except ValueError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME START
boardSetup(solBoard)
printBoard(solBoard) # temporary function to debug when needed
userGuess(solBoard,userBoard)