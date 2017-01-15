
# coding: utf-8

# In[6]:

import numpy as np
import cv2
import sys


# In[7]:

def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)

    return filters


# In[8]:

def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum


# In[10]:

print __doc__

for i in range(8050,10063):

    img = cv2.imread(str(i) + ".png",0)

    if img is None:
        print 'Failed to load image file', img_fn
    else:
        filters = build_filters()
        result_image = process(img, filters)
        cv2.imwrite(str(i) + ".png", result_image)

