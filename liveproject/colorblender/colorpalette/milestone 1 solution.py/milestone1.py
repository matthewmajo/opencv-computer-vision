# Import required modules
import cv2
import numpy as np

# Create a white canvas
def createCanvas(color):
    # Use NumPy to create an array
    # full of ones
    # We will have the canvas of shape
    # 640x640
    # Datatype used is uint8 which is
    # unsigned 8-bit integer
    canvas = np.ones((640,640,3),dtype=np.uint8)
    # Next, multiply the canvas
    # with the specified color
    # This fills the canvas with the 
    # specified color
    # Again, we will use uint8
    canvas = np.uint8(canvas * color)
    # Return the canvas
    return canvas

# Display an image
def displayImage(image,windowName):
    # Use cv2.imshow function
    cv2.imshow(windowName,image)

# Load the color palette
colorPalette = cv2.imread("palette.jpg")
# Right now, the color palette
# is way too big, so let's resize it down
colorPalette = cv2.resize(colorPalette, (640,640))

# Create canvas
# Use the createCanvas function
# you have written above
# Let's create a white canvas
# White color in BGR is 255,255,255
# We are using BGR channels because
# OpenCV uses the same
canvas = createCanvas([255,255,255])

# Display the canvas and the 
# color palette
# Use the functions you have 
# written above
displayImage(canvas,"Canvas")
displayImage(colorPalette,"Color Palette")
cv2.waitKey(0)
cv2.destroyAllWindows()
