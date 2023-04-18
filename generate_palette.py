# Katelyn Lindsey
# Color Palette App
# generate_palette.py
# This program focuses on taking an image, getting its pixel data,
# and choosing five colors from that data.

from PIL import Image
import os


def get_five_rgb_colors(image, width, height):
    """
    Takes an opened image and returns a list of five color
    tuples in rgb format. Colors are found using the Pillow
    image library.
    """

    rgb_list = []

    rgb_list.append(image.getpixel((0, 0)))
    rgb_list.append(image.getpixel((width//5, height//5)))
    rgb_list.append(image.getpixel((width//3, height//3)))
    rgb_list.append(image.getpixel((width//2, height//2)))
    rgb_list.append(image.getpixel((width - 1, height - 1)))

    return rgb_list


def remove_0x(color_value):
    """
    Takes a hex value (string) and removes the 0x at the beginning,
    also adding a 0 at the beginning if the hex has only one value.
    Returns the resulting string.
    """

    color_value = color_value[2:]

    if len(color_value) == 1:
        color_value = "0" + color_value

    return color_value


def rgb_to_hex(rgb_list):
    """
    Takes a list of rgb color tuples and returns a list
    of the equivalent hex values.
    """

    hex_list = []

    for color in rgb_list:

        # get hex for each separate color value
        red = hex(color[0])
        green = hex(color[1])
        blue = hex(color[2])

        # remove 0x at beginning of hex string
        red = remove_0x(red)
        green = remove_0x(green)
        blue = remove_0x(blue)

        # concatenate and add to hex list
        complete_hex = red + green + blue
        complete_hex = complete_hex.upper()
        hex_list.append(complete_hex)

    return hex_list


def create_color_dictionary(rgb_list, hex_list):
    """
    Takes a list of rgb values and a list of hex values
    (both of the same length) and returns a dictionary
    of those values.
    """

    color_dict = {}

    for index in range(len(hex_list)):

        color_dict["color_" + str(index + 1)] = [rgb_list[index], hex_list[index]]

    return color_dict


def generate_palette(image_path):
    """
    Takes a path to an image and uses its pixel data in
    order to get a color palette with five colors.
    Returns a dictionary of colors with color names as the
    keys and a list of [RGB, hex] color values as the value.
    """

    # get the absolute file path
    image_path = image_path[3:]  # take away ../ at beginning of path
    image_path = os.path.abspath(image_path)

    # open the image and get its width and height
    image = Image.open(image_path)
    width, height = image.size

    # get list of five pixel colors in both rgb and hex format
    rgb_list = get_five_rgb_colors(image, width, height)
    hex_list = rgb_to_hex(rgb_list)

    # create a dicionary out of the color values to return
    color_dict = create_color_dictionary(rgb_list, hex_list)

    return color_dict
