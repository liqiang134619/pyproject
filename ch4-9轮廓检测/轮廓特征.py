import numpy as np
import cv2 as cv

# 1. 特征矩

img = cv.imread('star.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
print( M )

# 轮廓面积
area = cv.contourArea(cnt)
# 轮廓周长
perimeter = cv.arcLength(cnt,True)

