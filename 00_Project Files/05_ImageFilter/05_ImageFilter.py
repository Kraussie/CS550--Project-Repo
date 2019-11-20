from PIL import Image, ImageEnhance
from progressbar import progressbar as bar
import os

os.system('clear')

img = Image.open("tree.jpg").convert('RGB')
#newImg = img.convert('1')


for y in bar(range(3456)):
	for x in range(5184):
		r, g, b = img.getpixel((x,y))
		img.putpixel((x,y),(r,int(g / 2.25),0))

img.save('result.png',"PNG")
img.show()
 
'''

im = Image.open('image.gif')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

print(r, g, b)
(65, 100, 137)

'''