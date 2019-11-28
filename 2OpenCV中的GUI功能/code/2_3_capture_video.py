import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) #创建对象

if not cap.isOpened():
    print('can not open camera')
    exit()
    
while True:
    ret, frame = cap.read()   
    if not ret:
        print('can not receive frame')
        break
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH),cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #灰度处理
 
    cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
