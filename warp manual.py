#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:05:32 2020

@author: prabhugantayat
"""

import cv2
import numpy as np

path = "images/phone.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(610,406))
points = np.float32([[306,38],[430,105],
                     [158,295],[285,363]])

width, height = 200,410
pointsNew = np.float32([[0,0],[width,0],
                        [0,height],[width, height]])

matrix = cv2.getPerspectiveTransform(points, pointsNew)
output = cv2.warpPerspective(img,matrix,(width, height))

for i in range(points.shape[0]):
    cv2.circle(img,(points[i][0],points[i][1]),5,(255,0,255),cv2.FILLED)


cv2.imshow("only",output)
cv2.imshow("str", img)
cv2.waitKey(0)
