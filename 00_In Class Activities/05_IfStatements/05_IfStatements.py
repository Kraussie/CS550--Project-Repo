# Author: Nate K
# Date of Creation: 09/13/2019
# Date of Last Edit: 09/13/2019
# If-Statement In-Class Activities
# SOURCE: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/13/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

import time
from colorama import init
init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')

print(Fore.BLUE + "Hello World")

def gameStart():
	print("\n\n\n\n\n\n\nGood Evening")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	gameStart_UR = input("SHALL WE PLAY A GAME?")
	if gameStart_UR == "yes" or gameStart_UR == "yeah":
		print("How about Global Thermonuclear War?")
		gameSelect()


# def begin(): #creating a function
# 	park_choice = input("\n\n\n\n\n\nDo you want to go to the park?\n").lower().strip() #removes lower case, strip extra spaces from edges
# 	if park_choice == 'yes' or park_choice == 'yeah' or park_choice == 'y':
# 		print("Yeah! Horray! I will get the picnic blanket.")
# 		tiger()
# 	elif park_choice == 'no':
# 		print("oh that's too bad, I didn't wanna go anyway")
# 		homeLunch()
# 	else:
# 		print("rip.")

# def tiger():
# 	tiger = input("Oh, no! There's a tiger in the park. Should we feed it our lunch, or make a run for it? \n")
# 	if tiger == 'feed':
# 		print("yay he's not hungry anymore")
# 	elif tiger == 'run':
# 		print("he's faster than u. u died haha")

# def homeLunch():
# 	beverage = input("wat do u want to drink?")
# 	if beverage == 'yes':
# 		print("oh no you drank water near u computer and spilled it. haha")
# 	else:
# 		print('ok guess not baiiii')

# begin() #running function