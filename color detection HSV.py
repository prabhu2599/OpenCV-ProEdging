#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 08:52:53 2020

@author: prabhugantayat
"""

import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",1000,240)
cv2.createTrackbar("HUE min","HSV",0,179,empty)
cv2.createTrackbar("HUE max","HSV",179,179,empty)
cv2.createTrackbar("SAT min","HSV",0,255,empty)
cv2.createTrackbar("SAT max","HSV",255,255,empty)
cv2.createTrackbar("VALUE min","HSV",0,255,empty)
cv2.createTrackbar("VALUE max","HSV",255,255,empty)



frameWidth, frameHeight = 640,480

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

while 1:
    _,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
    
    hmin = cv2.getTrackbarPos("HUE min","HSV")
    hmax = cv2.getTrackbarPos("HUE max","HSV")
    smin = cv2.getTrackbarPos("SAT min","HSV")
    smax = cv2.getTrackbarPos("SAT max","HSV")
    vmin = cv2.getTrackbarPos("VALUE min","HSV")
    vmax = cv2.getTrackbarPos("VALUE max","HSV")
   
    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])
    
    mask = cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    
    print(mask.shape,result.shape)
    
    
    stack_n1 = np.hstack((img,imgHSV,result))
    cv2.imshow('stack',stack_n1)
    cv2.imshow("0 dim vala",mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()