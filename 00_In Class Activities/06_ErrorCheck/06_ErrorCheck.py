import random

ranNum = random.randint(1,100)
print(ranNum)

def numberGame():
	guess = 5
	while guess > 0:
		userguess = input("\n\n\nI'm thinking of a number betweent 1 and 100.\nWhat is your guess?\n>>")
		try:
			if int(userguess) == ranNum:
				print("\n\n\nYou got it! Thanks for playing.")
				break;
			else:
				guess -= 1
				if guess > 0:
					print("\n\n\nTry again :(\nYou have", guess, "lives left!")
				else:
					print("\n\n\nGAME OVER. YOU LOST ALL YOUR LIVES")
		except ValueError:
			print("ERROR: Please enter a number (ex: 5)")

numberGame()