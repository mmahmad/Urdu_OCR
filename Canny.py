
# coding: utf-8

# In[8]:

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import PIL.ImageOps


# In[9]:

for i in range(8050,10063):
    img = cv2.imread(str(i) + ".png",0)
    edges = cv2.Canny(img, 100,200) # get edges
    
    cv2.imwrite(str(i) + ".png", edges)

