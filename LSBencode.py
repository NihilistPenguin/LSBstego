#!/usr/bin/env python3

import bitarray
import sys
import base64
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("image", help="cover image filename")
parser.add_argument("message", help="secret message string", type=str)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-o", "--outfile", help="filename for output file (Default: outputfile.png)")
args = parser.parse_args()

#---- Transform Message into Bits ----#
message = args.message.encode("utf-8")
encoded_message = base64.b64encode(message)
# create empty bitarray
ba = bitarray.bitarray()
# convert encoded message into bits
ba.frombytes(encoded_message)#.encode('UTF-8'))
# put bits into an array
bit_array = [int(i) for i in ba]

input_image = args.image
im = Image.open(input_image)
# make a copy of the image
if args.outfile:
	im.save(args.outfile)
	im = Image.open(args.outfile)
else:
	im.save("outputfile.png")
	im = Image.open("outputfile.png")
width, height = im.size
# retrieve an array containing every pixel
# the format = [0-255, 0-255, 0-255]
pixels = im.load()

# replace LSBs in the first row of pixels with our own
i = 0
for x in range(0, width):
	# get the RGB values from iteration X pixel of first row
	r,g,b = pixels[x,0]
	if args.verbose:
		print("[+] Pixel : [%d,%d]"%(x,0))
		print("[+] \tBefore : (%d,%d,%d)"%(r,g,b))

	#~~~RED PIXEL~~~#
	# convert r pixel value (0-255) to binary
	r_bits = bin(r)
	# replace last bit with ours, and convert back to decimal(0-255)
	new_red_pixel = int(r_bits[:-1] + str(bit_array[i]), base=2)
	i += 1

	if i > len(bit_array) - 1:
		break

	#~~~GREEN PIXEL~~~#
	g_bits = bin(g)
	new_green_pixel = int(g_bits[:-1] + str(bit_array[i]), base=2)
	i += 1

	if i > len(bit_array) - 1:
		break

	#~~~BLUE PIXEL~~~#
	b_bits = bin(b)
	new_blue_pixel = int(b_bits[:-1] + str(bit_array[i]), base=2)
	i += 1

	if i > len(bit_array) - 1:
		break

	pixels[x,0] = (new_red_pixel, new_green_pixel, new_blue_pixel)
	if args.verbose:	
		print("[+] \tAfter: (%d,%d,%d)"%(new_red_pixel, new_green_pixel, new_blue_pixel))

pixels[x,0] = (new_red_pixel, new_green_pixel, new_blue_pixel)

if args.outfile:
	im.save(args.outfile)
else:
	im.save("outputfile.png")
