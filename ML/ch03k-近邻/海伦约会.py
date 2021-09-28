import kNN

import matplotlib
import matplotlib.pyplot as plt

# 读取到了数据哦
datingDataMat, datingLabels = kNN.file2matrix("datingTestSet.txt")

# 创建散点图

# kNN.showdatas(datingDataMat,datingLabels)

# normalmat, ranges, minvalus = kNN.auto_normal(datingDataMat)
# print(normalmat)
# print(ranges)
# print(minvalus)
kNN.datingClassTest()