import numpy as np
import cv2 as cv


img = cv.imread("1231.jpg")
px = img[100,100]
print(px)
# BGR 图像 指定维度
px = img[100,100,0]
print(px)
px = img[100,100,1]
print(px)
px = img[100,100,2]
print(px)
print("=======================================")
print(type(img))
# 图像属性
print(img.shape)
# 像素数
print(img.size)
# 图像数据类型
print(img.dtype)

print(type(1))
print(type("1"))
print(type(1.1))
print("=======================================")

# 更好的像素访问和编辑方法：
print(img.item(10, 10, 2))
print(img.itemset((10, 10, 2), 100))
print(img.item(10, 10, 2))
cv.imshow("img",img)
cv.waitKey(0)



