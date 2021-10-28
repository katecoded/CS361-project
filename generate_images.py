# Katelyn Lindsey
# Color Palette App
# generate_images.py

import random, requests

def randomize_theme():
	"""
	Returns a random theme from a list of themes.
	"""

	theme_list = ["ocean", "mountains", "forest"]
	return random.choice(theme_list)

def get_images(theme):
	"""
	Chooses random images from the ../static/images folder
	based on the given theme (utilizes a service). 
	Returns a list of file paths.
	"""

	# if the theme is random, first choose a random theme
	if theme.lower == "random":
		theme = randomize_theme()

	# next, request random filenames from service based on 
	# the given theme
	# temporarily for MVP - hardcoded response
	response = {"filenames":[
			"../static/images/forest/fog.jpg",
			"../static/images/forest/forest-1.jpg",
			"../static/images/forest/trees.jpg",
			"../static/images/forest/jungle.jpg",
			"../static/images/forest/mushrooms.jpg",
			"../static/images/forest/night.jpg"
			]}

	# return the response
	return response["filenames"]
