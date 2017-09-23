# script open an image and wait for ESC key to close the image

import cv2 as opencv
import numpy

# read an image
# 0 - the color grey-scale
image = opencv.imread('image.jpg', 0)

# print the image type
print (type(image))

#show the image (but we need first a function to open it)
opencv.imshow('Test', image)

#we wait for key to be preseed -we will wait infinity time
exitOnKeyStoke = opencv.waitKey(0)

#the image will appear till the user clicks on keyboard
if exitOnKeyStoke == 27:
    opencv.destroyAllWindows()


