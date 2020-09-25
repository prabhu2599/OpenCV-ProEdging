#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:31:22 2020

@author: prabhugantayat
"""

import cv2
import numpy as np
from improvedStacking import stackImages

path = "images/1.jpg"

kernel = np.ones((5,5),np.uint8)

img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img_gray, (7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel)
imgErode1 = cv2.erode(imgDilation,kernel)

# high_thresh, thresh_im = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# lowThresh = 0.5*high_thresh
# print(high_thresh,lowThresh)


hor1 = np.hstack((imgCanny,imgErode1))
hor2 = np.hstack((img_gray,imgBlur))
ver_s = np.vstack((hor1, hor2))
# cv2.imshow("hor", ver_s) this handled the desi way of stacking

si = stackImages(1,([img,imgBlur,imgCanny,imgErode1,imgDilation,img_gray]))
cv2.imshow("stacked pro",si)

# cv2.imshow("img",img)
# cv2.imshow("gray",img_gray)
# cv2.imshow("blur",imgBlur)
# cv2.imshow("canny",imgCanny)
# cv2.imshow("dil",imgDilation)
# cv2.imshow("erode",imgErode1)



cv2.waitKey(0)
