# Katelyn Lindsey
# Color Palette App
# generate_palette.py
# This program focuses on taking an image, getting its pixel data, 
# and choosing five colors from that data.

from PIL import Image
import os
import pathlib
from sys import stderr # for debugging

def generate_palette(image_path):
	"""
	Takes a path to an image and uses its pixel data in
	order to get a color palette. Returns a list of tuples
	of color values.
	"""

	# get the file path
	image_path = image_path[3:] # take away ../ at beginning of path
	image_path = os.path.abspath(image_path)

	# first, open the image and get its width and height
	image = Image.open(image_path)
	width, height = image.size

	# get five pieces of pixel data
	color_1 = image.getpixel((0, 0))
	color_2 = image.getpixel((width//5, height//5))
	color_3 = image.getpixel((width//3, height//3))
	color_4 = image.getpixel((width//2, height//2))
	color_5 = image.getpixel((width - 1, height - 1))

	# return the color tuples received
	return [color_1, color_2, color_3, color_4, color_5]