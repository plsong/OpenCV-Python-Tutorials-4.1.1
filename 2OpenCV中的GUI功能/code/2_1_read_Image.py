"""
author:plsong
email:781637982@qq.com
creat date:2019.11.16
"""

import cv2 as cv

img = cv.imread('../src/messi.jpg',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
