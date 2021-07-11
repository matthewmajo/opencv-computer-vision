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
    size = [640, 640]   # Size of canvas 640x640 pixels
    canvas = np.ones((size[0], size[1], 3), dtype=np.uint8) # Creates array of 1s with rgb value per pixel
    canvas = np.uint8(canvas * color)   # Makes colour of canvas the same as input color
    return canvas
    
    

# Display an image
def displayImage(image, WindowName):
    cv2.imshow(WindowName, image)   # Shows an input image 
    

# Load the color palette
palette_image = cv2.imread('C:/Users/matma/Documents/liveproject/colorblender/colorpalette/kHTKrqM.jpg')
# Reads color palette image
palette_resized = cv2.resize(palette_image, (640, 640),) # Resizes palette to 640x640 pixels

# Create canvas
canvas = createCanvas([255,255,255]) # Creates a white canvas

# Display the canvas and the 
# color palette
display_canvas = displayImage(canvas, 'Canvas') # Displays white canvas
display_palette = displayImage(palette_resized, 'Color Palete') # Displays images indefinately
cv2.waitKey(0)  # Shows images immediately
cv2.destroyAllWindows() # Allows closing of image windows
