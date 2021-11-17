# Katelyn Lindsey
# Color Palette App
# generate_images.py

import random, requests, os, json
from sys import stderr # for debugging


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

	# first, get path to the relevant images folder based on theme
	image_folder = os.path.abspath("static/images/" + str(theme))

	# return a list of the images in that directory
	return os.listdir(image_folder)


def get_relative_image_paths(image_list, theme):
	"""
	Returns the given list to have paths usable in the html pages.
	"""

	for index in range(len(image_list)):
		# replace the file name with the full file path
		rel_path = "../static/images/" + str(theme) + "/" + str(image_list[index])
		image_list[index] = rel_path

	return image_list


def get_images(theme):
	"""
	Chooses random images from the ../static/images folder
	based on the given theme (utilizes a service). 
	Returns a list of file paths.
	"""

	theme = theme.lower()

	# if the theme is random, first choose a random theme
	if theme == "random":
		theme = randomize_theme()

	# next, get a list of all of the images in that theme's directory
	image_list = get_image_list(theme)

	# format the JSON for the request
	req_data = {"filenames":image_list, "num_wanted":6}

	# request random filenames from service based on the given theme
	response = requests.get("https://services-361.herokuapp.com/api/randomizer", json=req_data)
	response = response.json()

	# get the relative paths of the filenames (relative to static html pages)
	chosen_images = get_relative_image_paths(response, theme)

	# return the response
	return chosen_images
