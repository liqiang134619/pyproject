from numpy import  *

from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group,labels


# https://github.com/Jack-Cherish/Machine-Learning/blob/master/kNN/2.%E6%B5%B7%E4%BC%A6%E7%BA%A6%E4%BC%9A/kNN_test02.py
# k近邻算法
# 1. 计算已知类别数据集中的点与当前点之间的距离；
# 2. 按照距离递增次序排序；
# 3. 选取与当前点距离最小的k个点；
# 4. 确定前k个点所在类别的出现频率；
# 5. 返回前k个点出现频率最高的类别作为当前点的预测分类。
def classify0(inX,dataset,labels,k):
    dataSetSize = dataset.shape[0]
    # ❶（以下三行）距离计算  欧式距离公式
    diffmat = tile(inX,(dataSetSize,1)) - dataset
    sqDiffmat = diffmat ** 2
    sqDistances = sqDiffmat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # ❷ （以下两行）选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]



def file2matrix(filename):
    fr = open(filename,'r',encoding = 'utf-8')
    arrayOlines = fr.readline()
    # 文件行数
    numberOfLines  = len(arrayOlines)
    # 创建矩阵
    returnMat = zeros((numberOfLines,3))

    classLabelVector = []  # 列表
    index = 0

    # ❸ （以下三行）解析文件数据到列表

    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        # 最后一个元素
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

