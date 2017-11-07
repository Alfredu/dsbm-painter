from PIL import Image
import time
im = Image.open("/home/alfredu/dsbm.png")

foto =  list(im.getdata())

def map_color(inputColor, fromBitNum, toBitNum):
	outMax = 2**toBitNum
	inMax = 2**fromBitNum
	outColor = inputColor * outMax / inMax

	return outColor

outFoto = foto

i=0
for color in foto:
	outFoto[i] = (map_color(color[0], 8, 5), map_color(color[1], 8, 6), map_color(color[2], 8, 5))
	print outFoto[i]
	i+=1