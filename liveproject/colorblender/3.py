# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:11:30 2021
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
    
def mouseCALLbackFunction(event, x, y, flags, image):   # Fuction to return pixel color on mouse press
    global color1
    if event == cv2.EVENT_LBUTTONDOWN:
        color1 = findColor(palette, x, y)   # Finds the color at mouse position
        
def findColor(img, x, y):
        bgr_color = img[x, y] # Returns the BGR values from input image
        rgb_color = bgr_color[::-1] # Reorders color to RGB
        return rgb_color
    
def mixColors(color1, color2):
    mixed_color = np.uint8(color1+color2) # Mixes colors using simple color blending equation
    return mixed_color

# Load the color palette
palette_image = cv2.imread('C:/Users/matma/Documents/liveproject/colorblender/colorpalette/kHTKrqM.jpg')
# Reads color palette image
palette = cv2.resize(palette_image, (640, 640),) # Resizes palette to 640x640 pixels

# Create canvas
canvas = createCanvas([255,255,255]) # Creates a white canvas

# Names the windows used in the color blender
cv2.namedWindow('Canvas')
cv2.namedWindow('Color Palette')
cv2.setMouseCallback('Color Palette', mouseCALLbackFunction)  # Sets mousecallback function for the palette window

color1 = None # Sets initial color chosen on palette

while 1:
    displayImage(canvas, 'Canvas')  # Displays canvas
    displayImage(palette, 'Color Palette')  # Displays palette
    if color1 is not None:  # If user selects a color
        color2 = findColor(canvas, 0, 0)  # Finds the color of the canvas
        new_color = mixColors(color1, color1)*255 # Creates blended color
        canvas = createCanvas(new_color)  # Paints canvas new color
        last_color = color2[::-1] # Sets last color to the previous canvas color
        color1 = None # Sets selected color back to None
    k = cv2.waitKey(20) # K = any key pressed for longer than 20ms
    if k == 27: #if esc key pressed
        break
    if k == ord('r'):
        canvas = createCanvas([255, 255, 255])  # Makes canvas blank
    if k == ord('s'):   
        cv2.imwrite('C:/Users/matma/Documents/liveproject/colorblender/colorpalette/blended_canvas.jpg', canvas)    # Saves canvas
    if k == ord('u'):
        canvas = createCanvas(last_color)   # Changes canvas to previous color
    if k == ord('i'):
        canvas = createCanvas(new_color)    # Changes canvas back to new color
cv2.destroyAllWindows() # Closes all windows
