# 学习不同的形态学操作，例如侵蚀，膨胀，开运算，闭运算等。 我们将看到不同的功能，例如：cv.erode(),cv.dilate(), cv.morphologyEx()等。


# 侵蚀

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt




img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
# 侵蚀
erosion = cv.erode(img,kernel,iterations = 1)
#  扩张
dilation = cv.dilate(img,kernel,iterations = 1)
# 开运算
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow("t",closing)
cv.waitKey(0)
cv.destroyAllWindows()

#
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
# plt.xticks([]), plt.yticks([])
# plt.show()