"""
Author: Nate K
Date of Creation: 10/01/2019
Date of Last Edit: 10/11/2019
Minesweeper Game
SOURCES: 
- https://docs.python.org/3/library/sys.html
- https://stackoverflow.com/questions/26853453/how-to-ignore-an-indexerror-on-python
- https://stackoverflow.com/questions/24582233/python-flush-input-before-raw-input

On my honor, I have neither given nor received unauthorized aid.
Signed: NK 10/07/2019

PREREQUESITES:
- NEED LIBRARY: "colorama"

How to install "colorama":
- CMND IN TERMINAL: "pip install colorama"

"""
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME SETUP
import sys, random, colorama, os, time, termios
from colorama import Fore, Back, Style

try:
	# accept cmnd line arguments when running program, sourced from python.org
	xLen = int(sys.argv[1]) + 2
	yLen = int(sys.argv[2]) + 2
	numBombs = int(sys.argv[3])

	# create the solution and user display boards
	solBoard = [['#']*xLen for i in range(yLen)]
	userBoard = [['█' for x in range(xLen)] for y in range(yLen)]
except IndexError:
	# deal with error when first running the program, likely due to forgetting the arguments or inputting arguments incorectly, sourced/researched from stackoverflow.com; Back.RED and Style.RESET_ALL changes the error text to red to make it easier to see for the user
	print(Back.RED+"ERROR, Please enter a valid width, height, and number of bombs"+Style.RESET_ALL)

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
	input("Press any button to start the game\n>>")

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

		# try/except to deal with input errors
		try:
			# user inputs coords: example is '4 3 flag'
			urGUESS = input("\n\n\nPlease enter your guess coordinates (ex: X Y f or 0 1 g):\n>>").split(" ")
			urXguess = int(urGUESS[0])
			urYguess = int(urGUESS[1])

			# user can flag coordinates if they suspect a bomb is at those coords
			if urGUESS[2] == 'f' or urGUESS[2] == 'flag':
				if userBoard[urYguess][urXguess] == Fore.RED+'⚐'+Style.RESET_ALL:
					userBoard[urYguess][urXguess] = '█'
				elif userBoard[urYguess][urXguess] != Fore.RED+'⚐'+Style.RESET_ALL:
					userBoard[urYguess][urXguess] = '⚐'
			# user can reveal a coordinate, if it is a bomb, they immediately die, if it isn't a bomb, then the space is revealed
			elif urGUESS[2] == 'g' or urGUESS[2] == 'guess':
				if solBoard[urYguess][urXguess] == '*':
					os.system('clear')
					print(Back.RED+"YOU DIED"+Style.RESET_ALL)
					break
				else:
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

			# count # of unopened cells
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
				break
			else:
				# reset the number of unopened cells if win condition is not satisfied
				unopenedCells = 0
		# deal with error when user inputs something wrong
		except IndexError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL+"\nReturning to game in:")
			countdown321()
			continue
		except ValueError:
			print(Back.RED+"ERROR, Please enter a valid coordinate pair"+Style.RESET_ALL+"\nReturning to game in:")
			countdown321()
			continue

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# GAME START
gameIntro()
boardSetup(solBoard)
printBoard(solBoard) # temporary function to debug when needed
userGuess(solBoard,userBoard)