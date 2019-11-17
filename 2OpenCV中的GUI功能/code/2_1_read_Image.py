"""
author:plsong
email:781637982@qq.com
creat date:2019.11.16
"""

import cv2 as cv

img = cv.imread('../src/messi.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0) 
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('../src/newmessi.jpg',img)
    print('图片已保存')
    cv.destroyAllWindows()

