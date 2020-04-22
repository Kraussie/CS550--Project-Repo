# Author: Nate K
# Date of Creation: 10/17/2019
# Date of Last Edit: 10/17/2019
# Drawing, USE PYTHON 2
# SOURCES: 
# - https://pillow.readthedocs.io/en/stable/installation.html

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 10/17/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
from PIL import Image, ImageEnhance
import random

dimx = 800
dimy = 800

file = Image.new("RGB",(dimx,dimy))

curtisImg = Image.open("sm-DrAlexCurtis.jpg")
contrast = ImageEnhance.Contrast(curtisImg)
contrastFin = contrast.enhance(1)
sharpness = ImageEnhance.Sharpness(contrastFin)
sharpnessFin = sharpness.enhance(100)
brightness = ImageEnhance.Brightness(sharpnessFin)
brightnessFin = brightness.enhance(1)
color = ImageEnhance.Color(brightnessFin)
color.enhance(1).show()



'''
lines = 100

while lines > 0:
	red = random.randint(0,255)
	green = random.randint(0,255)
	blue = random.randint(0,255)
	initX = random.randint(10,90)

	for y in range(0,300):
		file.putpixel((initX,y),(red,green,blue))
		initX += random.randint(-1,1)
	lines -= 1

file.save("demo_image.png","PNG")
'''


'''
for x in range(0,4000):
	for y in range(0,4000):
		file.putpixel((x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		counter+=1
		print("COMPLETED:", (counter/160000), "%")
		file.save("demo_image.png","PNG")
'''

'''
#RED:
#X = 0, 100, 200, 300, 400, 500
#Y = 0, 100, 
for x in list(range(100,200)) + list(range(300,400)) + list(range(525,575)) + list(range(700,800)):
	for y in list(range(0,50)) + list(range(200,300)) + list(range(425,475)) + list(range(600,700)):
		file.putpixel((x,y),(255,0,0))

for x in list(range(0,100)) + list(range(200,300)) + list(range(400,500)) + list(range(600,700)):
	for y in list(range(100,200)) + list(range(300,400)) + list(range(500,600)) + list(range(700,800)):
		file.putpixel((x,y),(255,0,0))
'''

'''
for x in range(10,21):
	for y in range(10,21):
		file.putpixel((x,y),(255,0,0))
	for y in range(45,91):
		file.putpixel((x,y),(255,0,0))

for x in range(80,91):
	for y in range(10,21):
		file.putpixel((x,y),(255,0,0))
	for y in range(45,91):
		file.putpixel((x,y),(255,0,0))

for x in range(10,91):
	for y in range(45,91):
		file.putpixel((x,y),(255,255,0))
'''

file.save("demo_image.png","PNG")