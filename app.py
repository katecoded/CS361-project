# Katelyn Lindsey
# Color Palette App
# app.py

from flask import Flask, render_template, request
import sys, os
from generate_images import get_images

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

# route for displaying images
@app.route("/images", methods=["GET", "POST"])
def display_images():
	"""
	Displays the randomly generated images to the user.
	"""
	
	# request and refresh random images from service using random theme
	# get_images(request.form.get("theme"))
	image_files = get_images("Random")

	return render_template("images.html", images = image_files)




# make the application run
if __name__ == "__main__":
	app.run()
	