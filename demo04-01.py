import cv2
import numpy as np

path = "compass.jpg"
img = cv2.imread(path)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

sensitivity = 15

# define range of blue color in HSV
lower_blue = np.array([120 - sensitivity, 100, 100])
upper_blue = np.array([120 + sensitivity, 255, 255])
# Threshold the HSV image to get a range of blue color
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)  # 闭运算
mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)  # 开运算

# define range of red color in HSV
lower_red_0, upper_red_0 = np.array([0, 100, 100]), np.array([sensitivity, 255, 255])
lower_red_1, upper_red_1 = np.array([180 - sensitivity, 100, 100]), np.array([180, 255, 255])
# Threshold the HSV image to get a range of red color
mask_0 = cv2.inRange(hsv, lower_red_0, upper_red_0)
mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
mask_red = cv2.bitwise_or(mask_0, mask_1)

mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)

# 合并蓝色mask和红色mask
mask = cv2.bitwise_or(mask_blue, mask_red)
# Bitwise-AND mask
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('image', img)
# cv2.imshow('mask_blue', mask_blue)
# cv2.imshow('mask_red', mask_red)
cv2.imshow('res', res)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()