# Author: Nate K
# Date of Creation: 11/07/2019
# Date of Last Edit: 11/07/2019
# Fall Final Project
# SOURCES/USEFUL LINKS:

#PREREQUESITES:
#- NEED LIBRARY: "colorama"

#How to install "colorama":
#- CMND IN TERMINAL: "pip install colorama"

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 11/20/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM SETUP
from PIL import Image
from progressbar import progressbar as bar
import os, time, math

images = []

# saves the start time of the program
startTime = time.time()

os.system('clear')
print("FRACTAL IMAGE RENDERING:")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM FUNCTIONS

class Complex:
	#initialization of class arguments, re = x, im = y * i
	def __init__(self, re, im):
		self.re = re
		self.im = im

	#custom addition/subtraction function
	def __add__(self, other):
		return Complex(self.re + other.re, self.im + other.im)

	def __sub__(self,other):
		return Complex(self.re - other.re, self.im - other.im)

	#custom multiplication function
	def __mul__(self, other):
    	mulRE1 = self.re * other.re
    	mulRE2 = self.im * other.im
    	mulIM1 = self.re * other.im
    	mulIM2 = self.im * other.re
		return Complex(mulRE1 - mulRE2, mulIM1 + mulIM2)

	#custom power function
	def __pow__(self, other):
		return Complex(self.re**other,self.im**other)

	#custom absolute value function
	def __abs__(self):
		return math.hypot(self.re, self.im)

	#custom string representation
	#def __str__(self):

def mandelbrot(c, power=2, z=Complex(0,0), count=0):
	z = z**power + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,power,z,count)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 1 RUN
'''
I wanted this image to represent a lively city and the connected highways that branch off from large cities like New York. The red/pink point to the highways that are constantly lit up, and the large concentrations of red/pink are example of small/large cities. At the top of the image, there is a smaller city while in the direct center, there is a large city.
'''
maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1151953125
xmax = -0.0962109375
ymin = -0.935302734375
ymax = -0.916318359375

image1 =  Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 1 PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = Complex(cx,cy)
		fractResult = mandelbrot(c)

		r = (((fractResult+1)//6)**2)
		g = 0
		b = (fractResult*50)%256
		image1.putpixel((x,y),(r,g,b))

images.append(image1)


# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 2 RUN
'''
While exploring the mandelbrot fractal, I noticed that there were a few parts of the fractal that resembled a lightning bolt. That's pretty much what I wanted to show with this image, but I wanted to go a bit further by using if/elif functions to colorcode different parts of the image. 
'''
'''
maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1594882621765136
xmax = -0.1537981567382812
ymin = -1.1101653785705567
ymax = -1.1158554840087893

image2 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 2 PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = Complex(cx,cy)
		fractResult = mandelbrot(c)

		if fractResult > 14:
			r = int((fractResult**2)/2)
			g = int((fractResult**2)/2) 
			b = 0
		elif fractResult > 9:
			r = int((fractResult**3)/20)
			g = int((fractResult**3)/20)
			b = int((fractResult**2.1)/2.5)
		elif fractResult > 7:
			r = 0
			g = 0
			b = 0
		else:
			r = 0
			g = mandelbrot(c)*15
			b = 0
		image2.putpixel((x,y),(r,g,b))

images.append(image2)
'''
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 3 RUN
'''
I essentially chose this fractal because I liked the symmetrical pattern it created. After playing around with the colors for awhile, I figured out an equation that created a really awesome silhouette effect with the fractal. From there I continued to play around with the exact colors, proportions, and brightness. 
'''
'''
maxIterations = 255
imgx,imgy = 1000,1000
xmin = -1
xmax = 1
ymin = -1
ymax = 1

image3 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 3 PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = Complex(cx,cy)
		fractResult = mandelbrot(c, 5)
		r = int(((int(fractResult**2.25))%256)*1.25)
		g = int(((int(fractResult**2.25))%256)*0.6) #*0.6 creates the orange in combination with the red
		b = 0

		image3.putpixel((x,y),(r,g,b))

images.append(image3)
'''
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE COMBINE/SAVE
offsetX = 0
imgx, imgy = (len(images) * 1000), 1000
fullImg = Image.new("RGB",(imgx,imgy))

# sourced from stackoverflow.com
for im in images:
  fullImg.paste(im, (offsetX,0))
  offsetX += 1000

print("\n\n\nCheck the currently active directory for a file labled 'nkrauss_combinedImg.png' and other files")
image1.save("nkrauss_image1.png","PNG")
#image2.save("nkrauss_image2.png","PNG")
#image3.save("nkrauss_image3.png","PNG")
fullImg.save("nkrauss_combinedImg.png","PNG")
fullImg.show()

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# RUN TIME CALCULATION

#saves the end time of the program
endTime = time.time()
#calculates total time elapsed
totalTime = endTime - startTime
#translate total time into minutes and seconds
totalTimeMin = int(totalTime//60)
totalTimeSec = totalTime%60
print("PROGRAM RUN-TIME:", totalTimeMin, "Minutes and", totalTimeSec, "Seconds")

'''
PEER REVIEW COMMENTS
Roshni - image 1 has cool colors and results in a color with complimentary colors, image 2 looks like a lightning bolt hitting the ground-great imagery, image 3 has cool symmetry and a great red effect around the actual mandelbrot
'''
