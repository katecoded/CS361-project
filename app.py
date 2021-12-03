# Katelyn Lindsey
# Color Palette App
# app.py

from flask import Flask, render_template, request
from sys import stderr # for debugging
from generate_images import get_images
from generate_palette import generate_palette

# define app
app = Flask(__name__, static_url_path='/static')


# main route
@app.route("/", methods=["GET"])
def intro_page():
	"""
	Displays the main page of the website where users can choose 
	to create a palette.
	"""
	return render_template("index.html")


# route for choosing an image theme
@app.route("/choose_theme", methods=["GET"])
def choose_theme():
	"""
	Allows the user to choose a theme for their palette.
	"""
	return render_template("choose_theme.html")


# route for choosing the amount of images
@app.route("/choose_amount", methods=["GET"])
def choose_amount():
	"""
	Allows the user to choose the amount of images they can
	choose from.
	"""
	theme = request.args.get("theme")

	return render_template("choose_amount.html", theme=theme)


# route for displaying all images
@app.route("/images", methods=["GET"])
def display_images():
	"""
	Displays the randomly generated images to the user.
	"""

	theme = request.args.get("theme")
	amount = request.args.get("amount")
	
	# request paths to random images from service using theme and amount requested
	image_files = get_images(theme, amount)

	# render the page with the generated images
	return render_template("images.html", images=image_files, theme=theme, amount=amount)


# route for displaying color palette when image is clicked
@app.route("/palette", methods=["POST"])
def get_palette():
	"""
	Generates a palette using the given image file path.
	"""

	# store the image path clicked on and the theme
	chosen_image_path = request.form.get("filepath")
	theme = request.form.get("theme")

	# generate a palette as a dictionary in the form of color_1: [rgba, hex]
	color_dict = generate_palette(chosen_image_path)

	return render_template("palette.html", image=chosen_image_path, theme=theme, colors=color_dict)



# make the application run
if __name__ == "__main__":
	app.run()
