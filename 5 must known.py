import cv2
import numpy as np

path = "1.jpg"

kernel = np.ones((5,5),np.uint8)

img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img_gray, (7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel)

high_thresh, thresh_im = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lowThresh = 0.5*high_thresh
print(high_thresh,lowThresh)

imgErode1 = cv2.erode(imgDilation,kernel)

cv2.imshow("img",img)
cv2.imshow("gray",img_gray)
cv2.imshow("blur",imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("dil",imgDilation)
cv2.imshow("erode",imgErode1)#



cv2.waitKey(0)
