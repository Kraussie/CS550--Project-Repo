# Author: Nate K
# Date of Creation: 10/31/2019
# Date of Last Edit: 11/XX/2019
# Mandelbrot Set and Fractals
# SOURCES/USEFUL LINKS:
# https://www.atopon.org/mandel/# 

#PREREQUESITES:
#- NEED LIBRARY: "progressbar2"

#How to install "numpy":
#- CMND IN TERMINAL: "pip3 install progressbar2"

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 10/26/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM SETUP
from PIL import Image
from progressbar import progressbar as bar

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM FUNCTIONS
def mandelbrot(c, z=complex(0,0), count=0):
	z = z**2 + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,z,count)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 1 RUN
'''
I wanted this image to represent a lively city and the connected highways that branch off from large cities like New York. The red/pink point to the highways that are constantly lit up, and the large concentrations of red/pink are example of small/large cities. At the top of the image, there is a smaller city while in the direct center, there is a large city.
'''
'''
maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1151953125
xmax = -0.0962109375
ymin = -0.935302734375
ymax = -0.916318359375

image1 =  Image.new("RGB",(imgx,imgy))

for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		r = (((mandelbrot(c)+1)//6)**2)
		g = 0
		b = (mandelbrot(c)*50)%256
		image1.putpixel((x,y),(r,g,b))

image1.save("mandelbrot_img1.png", "PNG")
image1.show()
'''
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 2 RUN
maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1594882621765136
xmax = -0.1537981567382812
ymin = -1.1101653785705567
ymax = -1.1158554840087893

image2 = Image.new("RGB",(imgx,imgy))

for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		if mandelbrot(c) > 10:
			r = int((mandelbrot(c)**2)/2)
			g = int((mandelbrot(c)**2)/2)
			b = 0
		elif mandelbrot(c) > 8:
			r = 0
			g = 0
			b = mandelbrot(c)*2
		elif: mandelbrot(c) > 7:
			r = 0
			g = 0
			b = 0
		else:
			r = 255
			g = 255
			b = 255
		image2.putpixel((x,y),(r,g,b))

image2.save("mandelbrot_img2.png","PNG")
image2.show()

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 3 RUN

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE COMBINE