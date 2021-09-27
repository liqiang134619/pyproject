import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

f = "D:/1231.jpg"


# 基础图像显示
def demo01():
    print(cv.__version__)
    # cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
    # cv.IMREAD_GRAYSCALE：以灰度模式加载图像
    # cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    # 注意
    # 除了这三个标志，你可以分别简单地传递整数1、0
    # 或 - 1。
    img = cv.imread(f, 0)
    cv.imshow('image', img)
    # 使用函数**cv.imwrite**()保存图像。
    # cv.imwrite("test.png",img)

    cv.waitKey(0)
    cv.destroyAllWindows()


# matplotlib 绘制图像
def demo02():
    img = cv.imread(f, cv.IMREAD_COLOR)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
    plt.show()


if __name__ == '__main__':
    demo02()
