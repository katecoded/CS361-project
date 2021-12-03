# Katelyn Lindsey
# Color Palette App
# generate_images.py
# This program generates images from the project's images/ folder 
# using a randomizer service.

import random, requests, os, json
from sys import stderr # for debugging

random.seed()


def randomize_theme():
	"""
	Returns a random theme from a list of themes.
	"""

	theme_list = ["ocean", "mountains", "forest", "city"]
	return random.choice(theme_list)


def get_image_list(theme):
	"""
	Returns a list of image file names based on the theme.
	"""

	# get absolute path to the relevant images folder
	image_folder = os.path.abspath("static/images/" + str(theme))

	# return a list of the images in that directory
	return os.listdir(image_folder)


def get_amount(amount):
	"""
	Returns an integer amount based on the given string.
	"""

	if amount == "small":
		return random.randint(2, 4)
	elif amount == "medium":
		return random.randint(5, 7)
	else:
		return random.randint(8, 10)


def get_relative_image_paths(image_list, theme):
	"""
	Returns the given image list altered to have image paths relative to
	the HTML pages.
	"""

	for index in range(len(image_list)):
		rel_path = "../static/images/" + str(theme) + "/" + str(image_list[index])
		image_list[index] = rel_path

	return image_list


def get_images(theme, amount):
	"""
	Chooses random images from the ../static/images folder based
	on the given theme (str) and amount of images (str) (utilizes a 
	randomizer service). 
	Returns a list of file paths relative to the HTML pages.
	"""

	theme = theme.lower()
	amount = amount.lower()

	if theme == "random":
		theme = randomize_theme()

	# get an integer based on the given string amount
	amount = get_amount(amount)

	image_list = get_image_list(theme)

	req_data = {"filenames":image_list, "num_wanted":amount}

	# request random filenames from service based on the given theme
	response = requests.get("https://services-361.herokuapp.com/api/randomizer", json=req_data)
	response = response.json()

	chosen_images = get_relative_image_paths(response, theme)

	return chosen_images
