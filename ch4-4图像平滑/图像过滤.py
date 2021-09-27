# 使用各种低通滤镜模糊图像 - 将定制的滤镜应用于图像（2D卷积）


# 2D卷积（图像过滤）
# 与一维信号一样，还可以使用各种低通滤波器（LPF），高通滤波器（HPF）等对图像进行滤波。LPF有助于消除噪声，使图像模糊等。HPF滤波器有助于在图像中找到边缘。
#
# OpenCV提供了一个函数**cv.filter2D**来将内核与图像进行卷积。例如，我们将尝试对图像进行平均滤波。5x5平均滤波器内核如下所示：


# 保持这个内核在一个像素上，\
# 将所有低于这个内核的25个像素相加，
# 取其平均值，然后用新的平均值替换中心像素。
# 它将对图像中的所有像素继续此操作。试试这个代码，并检查结果:


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('opencv-logo.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()