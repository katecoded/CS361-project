# Katelyn Lindsey
# Color Palette App
# app.py

from flask import Flask, render_template, request
import sys, os
from generate_images import get_images
from generate_palette import generate_palette

# define app
app = Flask(__name__, static_url_path='/static')


# main route
@app.route("/", methods=["GET"])
def intro_page():
	"""
	Displays the main page of the website where users can choose 
	to look at random images.
	"""
	return render_template("index.html")


# route for displaying all images
@app.route("/images", methods=["GET"])
def display_images():
	"""
	Displays the randomly generated images to the user.
	"""

	# store the theme
	theme = request.args.get("theme")
	
	# request paths to random images from service using theme requested
	image_files = get_images(theme)

	# render the page with the generated images
	return render_template("images.html", images=image_files, theme=theme)


# route for displaying color palette when image is clicked
@app.route("/palette", methods=["POST"])
def get_palette():
	"""
	Generates a palette using the given image file path.
	"""

	# store the image path clicked on and the theme
	chosen_image_path = request.form.get("filepath")
	theme = request.form.get("theme")

	# generate a palette from the image received
	color_list = generate_palette(chosen_image_path)

	return render_template("palette.html", image=chosen_image_path, theme=theme, color_1=color_list[0], color_2=color_list[1], color_3=color_list[2], color_4=color_list[3], color_5=color_list[4])



# make the application run
if __name__ == "__main__":
	app.run()
