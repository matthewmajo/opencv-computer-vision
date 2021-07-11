# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:22:31 2021

@author: matma
"""

# Import required modules
import numpy as np
import cv2

# Create a white canvas
def createCanvas(color):
    size = [640, 640]
    canvas = np.ones((size[0], size[1], 3), dtype=np.uint8)
    canvas = np.uint8(canvas * color)
    return canvas
    
    

# Display an image
def displayImage(image, WindowName):
    cv2.imshow(WindowName ,image)
    

# Load the color palette
# Your code here
palette_image = cv2.imread('C:/Users/matma/Documents/liveproject/colorblender/colorpalette/kHTKrqM.jpg')
palette_resized = cv2.resize(palette_image, (640, 640),)

# Create canvas
# Use the createCanvas function
# you have written above
# Your code here
canvas = createCanvas([255,255,255])

# Display the canvas and the 
# color palette
# Use the functions you have 
# written above
# Your code here
display_canvas = displayImage(canvas, 'Canvas')
display_palette = displayImage(palette_resized, 'Color Palete')
cv2.waitKey(0)
cv2.destroyAllWindows()
