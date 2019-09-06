# Author: Nate K
# Date of Creation: 09/06/2019
# Date of Last Edit: 09/06/2019
# This code has a short conversation with the user
# Sources:
# https://docs.python.org/3/library/webbrowser.html#module-webbrowser
# https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/06/2019

import webbrowser
import time

print('\n\n\n\n\n\nHello, World!') # Beginning of conversation
user_response_01 = input("What's your name?\n\n\n") # Asking for name
print("\n\n\nOh, hey " +user_response_01+". Nice to meet you!") # 1/2 Response to receiving name
print("My name is John Doe") # 2/2
user_response_02 = int(input("How's your day been on a scale from 1 (terrible) to 10 (amazing)?\n\n\n"))
if user_response_02 >= 8: # Asking about how day is going, responding accordingly and opening a video
	print("\n\n\nWow! I'm glad that it's going so well!Maybe you should go to sleep now so you can end the day well.")
	print("Here's some relaxing music.")
	time.sleep(3)
	webbrowser.open('https://www.youtube.com/watch?v=wlsdMpnDBn8')
elif user_response_02 < 8 and user_response_02 > 6:
	print("\n\n\nGlad it's going ok. Hope it gets better!") 
	print("Maybe a cute baby video?")
	time.sleep(3)
	webbrowser.open('https://www.youtube.com/watch?v=hkANcahJA4U')
elif user_response_02 <= 6 and user_response_02 >= 4:
	print("\n\n\nAn average day I guess. Hope something makes it a little brighter!")
	print("Maybe a video of the sun?")
	time.sleep(3)
	webbrowser.open('https://youtu.be/HFT7ATLQQx8?t=30')
elif user_response_02 < 4 and user_response_02 > 2:
	print("\n\n\nNot going too well? Maybe take a nap?")
	print("Here are some funny fail videos.")
	time.sleep(3)
	webbrowser.open('https://www.youtube.com/watch?v=YuwxJB-TOyM')
elif user_response_02 <= 2:
	print("\n\n\nYikes! Sounds like a terrible day. Hopefully, it can't get any worse!")
	print("Here are some cute dog videos :)")
	time.sleep(3)
	webbrowser.open('https://www.youtube.com/watch?v=PgD56JEUWFA')


print("\n\n\nI gotta go now :( Have a good day!")
print('Bye bye!\n\n\n\n\n\n')
time.sleep(2)
webbrowser.open('https://youtu.be/jWWW4q0VwP0?t=21')