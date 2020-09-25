#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:05:35 2020

@author: prabhugantayat
"""

import cv2
import numpy as np

path = "images/phone.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(610,406))

circles = np.zeros((4,2),np.int)
counter = 0

def mouseClicks(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:  
        circles[counter] = x,y
        counter += 1
        print(circles)

while 1:
    
    if counter == 4:
        points = np.float32([circles[0],circles[1],circles[2],circles[3]])
    
        width, height = 200,400
        pointsNew = np.float32([[0,0],[width,0],
                                [0,height],[width, height]])
        
        matrix = cv2.getPerspectiveTransform(points, pointsNew)
        output = cv2.warpPerspective(img,matrix,(width, height))
        cv2.imshow("only",output)

    for i in range(circles.shape[0]):
        cv2.circle(img,(circles[i][0],circles[i][1]),5,(255,0,255),cv2.FILLED)

    
    cv2.imshow("str", img)
    cv2.setMouseCallback("str",mouseClicks)
    
    cv2.waitKey(1)
