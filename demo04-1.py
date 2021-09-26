import numpy as np
import cv2 as cv



# bgr
green = np.uint8([[[0, 255, 0]]])

print(green)

hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
cv.waitKey(0)

#  hsv

rgb = '#869C90,#899F92,#8A9E92,#8A9F8E'
rgb = rgb.split(',')
# 转换为BGR格式，并将16进制转换为10进制
bgr = [[int(r[5:7], 16), int(r[3:5], 16), int(r[1:3], 16)] for r in rgb]

# 转换为HSV格式
hsv = [list(cv.cvtColor(np.uint8([[b]]), cv.COLOR_BGR2HSV)[0][0]) for b in bgr]
print(hsv)
hsv = np.array(hsv)
print('H:', min(hsv[:, 0]), max(hsv[:, 0]))
print('S:', min(hsv[:, 1]), max(hsv[:, 1]))
print('V:', min(hsv[:, 2]), max(hsv[:, 2]))





















