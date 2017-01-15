
# coding: utf-8

# In[23]:

from skimage.morphology import skeletonize
from skimage import draw
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import PIL.ImageOps
import os


# In[26]:

img = cv2.imread('8050.png',0)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)

ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False

while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True

# cv2.imwrite("temp.png", skel)

# image_file = Image.open("temp.png") # open colour image
# # image_file = image_file.convert('1') # convert image to black and white
# inverted_image = PIL.ImageOps.invert(image_file)
# inverted_image.save('skel_result.png')

# os.remove("temp.png")

image = Image.fromarray(skel)
inverted_image =  PIL.ImageOps.invert(image)
inverted_image.save('skel_result.png')

