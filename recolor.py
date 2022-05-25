#!/usr/bin/env python3

""" 
This python script will find the closest color in the list of colors to the color of the pixel in the image.
The list of colors is a list of RGB values.
    

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Vitafeu"
__contact__ = "benji.feu.feu.feu@gmail.com"
__copyright__ = "Copyright 2022, Vitafeu"
__credits__ = "Vitafeu"
__date__ = "2022/05/25"
__deprecated__ = False
__email__ =  "benji.feu.feu.feu@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Vitafez"
__status__ = "Production"
__version__ = "0.0.1"

import numpy as np
from PIL import Image

# Function to find the closest color in the list of colors
def closest(list_colors,color):
    list_colors = np.array(list_colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((list_colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = list_colors[index_of_smallest]
    return smallest_distance 

# Get the list of colors from user
list_colors = input("Enter a list of colors in RBG (syntax : R,G,B;R,G,B) : ")
list_colors = list_colors.split(';')
list_colors = [i.split(",") for i in list_colors]
list_colors = [list( map(int,i) ) for i in list_colors]

# Open the image from the path
path = input("Enter the path of the image : ")
i = Image.open(path)

# Get the width and height of the image
width, height = i.size

# Replace the colors in the image with the closest color in the list
for x in range(0, width - 1):
    for y in range(0, height - 1):
        current_color = i.getpixel( (x,y) )
        current_color = current_color[:-1]
        new_color = closest(list_colors,current_color)
        new_color = new_color.flatten()
        new_color = tuple(new_color)
        i.putpixel( (x,y), new_color)

# Shows the image
i.show()

input("Press any key to exit")
