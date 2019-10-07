"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/07/2019
Minesweeper Game
SOURCES: 

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 10/07/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random, colorama
from colorama import Fore, Back, Style
try:
	# accept cmnd line arguments when running program
	xLen = int(sys.argv[1]) + 2
	yLen = int(sys.argv[2]) + 2
	numBombs = int(sys.argv[3])

	solBoard = [[0]*xLen for i in range(yLen)]
	userBoard = [['█' for x in range(xLen)] for y in range(yLen)]
except IndexError:
	print(Back.RED+"ERROR, Please enter a valid width, height, and number of bombs"+Style.RESET_ALL)


def print_board(board):
	print("\n\n\n")
	for row in board[1:-1]:
		print(*row[1:-1])

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOARD SETUP
def boardSetup(board):
    for i in range(numBombs):
        x = random.randint(1, xLen-2)
        y = random.randint(1, yLen-2)
        while board[y][x] == '*':
            x = random.randint(1, xLen-2)
            y = random.randint(1, yLen-2)
        board[y][x] = '*'
        bombSurroundCount(x, y, board)

# *+*+*+*+*+*+*+*+*+*+*+
# COUNT NEIGHBOR BOMBS
def bombSurroundCount(x,y,board):
    for r in range(y-1, y+2):
        for c in range(x-1, x+2):
            if board[r][c] != '*':
                board[r][c] += 1

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# ACCEPT USER INPUT
def userGuess(solBoard, userBoard):
	bombsFound = 0

	while numBombs != bombsFound:
		print_board(userBoard)

		try:
			urGUESS = input("\n\n\nPlease enter your guess coordinates (ex: X Y f or 0 1 g):\n>>").split(" ")
			urXguess = int(urGUESS[1]) + 1
			urYguess = int(urGUESS[0]) + 1
			solXguess = urXguess
			solYguess = urYguess
		except IndexError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue
		except ValueError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue

		try:
			if urGUESS[2] == 'f' or urGUESS[2] == 'flag':
				if userBoard[urXguess][urYguess] == '⚐':
					userBoard[urXguess][urYguess] = '█'
				elif userBoard[urXguess][urYguess] != '⚐':
					userBoard[urXguess][urYguess] = '⚐'
			elif urGUESS[2] == 'g' or urGUESS[2] == 'guess':
				if solBoard[solXguess][solYguess] == '*':
					print("YOU DIED")
					break
				else:
					if solBoard[solXguess][solYguess] == 0:
						userBoard[urXguess][urYguess] = solBoard[solXguess][solYguess]
						#display surrounding blocks
					else:
						userBoard[urXguess][urYguess] = solBoard[solXguess][solYguess]
		except IndexError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue
		except ValueError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL)
			continue

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME START
boardSetup(solBoard)
print_board(solBoard)
userGuess(solBoard,userBoard)