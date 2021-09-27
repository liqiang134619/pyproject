import numpy as np
import cv2 as cv


# 图像操作

img = cv.imread("1231.jpg")
# b = img[:,:,0]
# r = img[:,:,1]
# g = img[:,:,2]
b,g,r = cv.split(img)

cv.imshow("all",img)
cv.imshow("blue",b)
cv.imshow("red",r)
cv.imshow("green",g)
cv.waitKey(0)