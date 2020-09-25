import cv2

frameWidth = 640
frameHeight= 360

capture = cv2.VideoCapture('1.mp4')
#capture.set(3, frameWidth)
#capture.set(4, frameHeight)

while 1:
    success,img = capture.read()
    img = cv2.resize(img,(frameWidth, frameHeight))
    cv2.imshow("succ",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
