import base64
import sys
from PIL import Image

input_image = sys.argv[1]
image = Image.open(input_image)

extracted = ''

pixels = image.load()

for x in range(0, image.width):
	r,g,b = pixels[x,0]
	#extract LSB of each color
	extracted += bin(r)[-1]
	extracted += bin(g)[-1]
	extracted += bin(b)[-1]

chars = []
#print(extracted[0:160])
for i in range(0, len(extracted)/8):
	#byte from 0-8, 8-16, ...
	byte = extracted[i*8:(i+1)*8]
	#make string of each bit in a byte, convert to decimal int, convert to char
	chars.append(chr(int(''.join([str(bit) for bit in byte]), base=2)))

#print(chars)

#join chars in array into a string and decode
flag = base64.b64decode(''.join(chars) + "==")
print(flag)

