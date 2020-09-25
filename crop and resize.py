#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:43:24 2020

@author: prabhugantayat
"""

import cv2

path = "1.jpg"

img = cv2.imread(path)

width, height = 400,400
img_resize = cv2.resize(img,(width, height))

img_crop1 = img[:,700:1100,:]
img_cropped_resized = cv2.resize(img_crop1, (img.shape[1],img.shape[0]))

print(img.shape,img_crop1.shape)

cv2.imshow("noraml",img)
cv2.imshow("resize",img_resize)
cv2.imshow("crop",img_crop1)
cv2.imshow("crop resize",img_cropped_resized)

cv2.waitKey(0)