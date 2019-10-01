"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/01/2019
Minesweeper Game
SOURCES: 

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 09/26/2019
"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random

# accept cmnd line arguments when running program
xLen = int(sys.argv[1])
yLen = int(sys.argv[2])
numBomb = int(sys.argv[3])

def nicePrint(listArg):
	for i in listArg:
		print(*i)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOARD CREATION
# 0 = no bomb in space or nearby
def boardCreate():
	mineBoard = [[0 for x in range(xLen)] for y in range(yLen)]
	nicePrint(mineBoard)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# BOMB ASSIGNMENT
# -1 = bomb in space
def bombAssign():
	mineBoard[random.randint(0,xLen)][random.randint(0,yLen)] = -1
	nicePrint(mineBoard)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# COUNT NEIGHBOR BOMBS


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# START GAME
boardCreate()
