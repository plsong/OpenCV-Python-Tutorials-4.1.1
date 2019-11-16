"""
author:plsong
email:781637982@qq.com
creat date:2019.11.16
"""

import cv2 as cv
from  matplotlib import pyplot as plt

img = cv.imread('./src/messi.jpg',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([]) # 隐藏坐标轴
plt.show()
