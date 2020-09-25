#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:09:26 2020

@author: prabhugantayat
"""

import numpy as np
import cv2

img = np.zeros((512,512,3), dtype=np.uint8)
img[:] = 125,0,0
print(img.shape)
print(img)

cv2.line(img,(0,0),(400,400),(134,255,34),thickness=3)
cv2.rectangle(img,(350,90),(300,250),(100,100,100),4)
cv2.rectangle(img,(35,290),(400,400),(160,160,180),cv2.FILLED)
cv2.circle(img,(300,300),50,(255,255,0),cv2.FILLED)
cv2.putText(img,"yahan hai 35",(35,400),cv2.FONT_HERSHEY_SCRIPT_COMPLEX ,1,(255,255,255))

cv2.imshow("img", img)
cv2.waitKey(0)