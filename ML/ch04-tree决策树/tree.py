# 信息期望值 H = -Σi=1,N p(x1)log2p(x1)




from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}

    # ❶ （以下五行）为所有可能分类创建字典
    for featVec in dataSet:
        # 没错啊 最后一列的值
        currentLabel = featVec[-1]
        # 每个map 键值 都记录了当前类别出现的次数,
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    # 香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        # 选择该标签(Label)的概率
        prob = float(labelCounts[key]) / numEntries
        # ❷ 以2为底求对数
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt



def createDataSet():
    dataSet = [
                [1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no'],

               ]
    labels = ['no surfacing','flippers']

    return dataSet,labels





data,lables = createDataSet()
print(calcShannonEnt(data))