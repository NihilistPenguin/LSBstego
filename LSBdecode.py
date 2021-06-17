#!/usr/bin/env python3

import base64
import sys
from PIL import Image
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("image", help="steg image filename")
args = parser.parse_args()

input_image = args.image
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

for i in range(0, int(len(extracted)/8)):
	# byte from 0-8, 8-16, ...
	byte = extracted[i*8:(i+1)*8]
	# make string of each bit in a byte, convert to decimal int, convert to char
	c = chr(int(''.join([str(bit) for bit in byte]), base=2))
	if c in string.printable:
		chars.append(c)


# join chars in array into a string and decode
# print(chars)
flag = base64.b64decode(''.join(chars) + "==")
print(flag)
