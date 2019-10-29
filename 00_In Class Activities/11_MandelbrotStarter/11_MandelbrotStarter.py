from PIL import Image
# https://www.atopon.org/mandel/#

from progressbar import progressbar as bar

def mandelbrot(c, z=complex(0,0), count=0):
	z = z**2 + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,z,count)

maxIterations = 255
imgx,imgy = 5000,5000
xmin = -0.1151953125
xmax = -0.0962109375
ymin = -0.935302734375
ymax = -0.916318359375

image =  Image.new("RGB",(imgx,imgy))

for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		r = 0
		g = 0
		b = (mandelbrot(c)*50)%256
		image.putpixel((x,y),(r,g,b))


image.save("mandelbrot_class.png", "PNG")