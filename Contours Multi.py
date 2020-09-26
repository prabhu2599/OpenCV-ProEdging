#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:30:39 2020

@author: prabhugantayat
"""

import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Canny Edging")
cv2.resizeWindow("Canny Edging",1000,240)
cv2.createTrackbar("THRESH1","Canny Edging",150,255,empty)
cv2.createTrackbar("THRESH2","Canny Edging",255,255,empty)
cv2.createTrackbar("AREA","Canny Edging",5000,30000, empty)

# for coninuos
# frameWidth, frameHeight = 640,480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

cap = cv2.imread("images/phone.jpg")
cap = cv2.resize(cap,(610,406))



def getContours(img,imgContour):
    
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("AREA","Canny Edging")
        if area>areaMin:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),7) 
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(imgContour,"Points: "+ str(len(approx)),
                        (x+w+20,y+h-20),cv2.FONT_HERSHEY_TRIPLEX,
                        0.7,(0,255,0),2)
            cv2.putText(imgContour,"Area: "+ str(int(area)),
                        (x+w+20,y+h),cv2.FONT_HERSHEY_TRIPLEX,
                        0.7,(0,255,0),2)
    
while 1:  
    # _,img = cap.read() # for stream input
    
    img = cap.copy()
    imgContour = cap.copy()
    
    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    
    # print(imgBlur.shape,imgGray.shape)  
    
    THRESHOLD1 = cv2.getTrackbarPos("THRESH1","Canny Edging")
    THRESHOLD2 = cv2.getTrackbarPos("THRESH2","Canny Edging")
    
    imgCanny = cv2.Canny(imgGray,THRESHOLD1,THRESHOLD2)
    
    kernel = np.ones((5,5))
    imgDilated = cv2.dilate(imgCanny,kernel,iterations=1)
    
    getContours(imgDilated,imgContour)  
    
    # print(imgBlur.shape,imgGray.shape,imgCanny.shape,imgDilated.shape)
    imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
    imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
    imgDilated = cv2.cvtColor(imgDilated,cv2.COLOR_GRAY2BGR)
    # print(imgBlur.shape,imgGray.shape,imgCanny.shape,imgDilated.shape)
    
    stack1 = np.hstack((img,imgBlur,imgGray))
    stack2 = np.hstack((imgCanny,imgDilated,imgContour))
    stackFull = np.vstack((stack1,stack2))
    cv2.imshow('stack',stackFull)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()