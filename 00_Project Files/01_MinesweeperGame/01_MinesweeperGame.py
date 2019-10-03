"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/02/2019
Minesweeper Game
SOURCES: 

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 10/03/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random, colorama
from colorama import Fore, Back, Style

# accept cmnd line arguments when running program
xLen = int(sys.argv[1])
yLen = int(sys.argv[2])

def nicePrint(listArg):
	print('\n\n\n')
	for i in listArg:
		print(*i)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOARD CREATION [COMPLETE]
# 0 = no bomb in space or nearby
def boardCreate():
	# 1 layer buffer around playing field
	mineBoard = [['#' for x in range(xLen+2)] for y in range(yLen+2)]

	# add zeroes to field, keeping 1 layer buffer
	for row in range(1,1+xLen):
		for col in range(1,1+yLen):
			mineBoard[row][col] = 0

	bombAssign(mineBoard)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOMB ASSIGNMENT [COMPLETE]
# * = bomb in space
def bombAssign(mineBoard):
	#accept cmnd line argument for # of bombs
	numBomb = int(sys.argv[3])

	#loop until all bombs have been placed
	while numBomb > 0:
		mineBoard[random.randint(1,xLen)][random.randint(1,yLen)] = '*'
		numBomb -= 1

	bombLoop(mineBoard)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# COUNT NEIGHBOR BOMBS [COMPLETE]
def bombLoop(mineBoard):
	#go through entire list, if item isn't '*' or '#', then check the surrounding items
	for row in range(1,1+xLen):
		for col in range(1,1+yLen):
			if col != '*' and col != '#':
				searchSurround(mineBoard, row, col)

	addColor(mineBoard)

def searchSurround(mineBoard,row,col):
	#var to keep track of nearby bombs
	bombCount = 0

	#search surrounding items and assign val of # of bombs
	for neighborRow in range(row-1,row+2):
		for neighborCol in range(col-1,col+2):
			if mineBoard[row][col] != '*':
				if mineBoard[neighborRow][neighborCol] == '*':
					bombCount += 1
				mineBoard[row][col] = bombCount

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# ADD COLOR TO GRID
def addColor(mineBoard):
	for row in range(0,2+xLen):
		for col in range(0,2+yLen):
			if mineBoard[row][col] == '#':
				#dim the border of the list
				mineBoard[row][col] = Style.DIM+'#'+Style.RESET_ALL
			elif mineBoard[row][col] == '*':
				#make all bombs red
				mineBoard[row][col] = Fore.RED+'*'+Style.RESET_ALL
	nicePrint(mineBoard)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# START GAME
boardCreate()