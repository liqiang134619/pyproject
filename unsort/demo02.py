import numpy as np
import cv2 as cv


img = np.zeros((512,512,3),np.uint8)

# 绘制一条厚度为5的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),1)

# 矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),1)
# 圆形
cv.circle(img,(447,63), 63, (0,0,255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
# 添加文本
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow("output",img)

cv.waitKey(0)
cv.destroyAllWindows()

