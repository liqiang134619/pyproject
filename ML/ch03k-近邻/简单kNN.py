import  kNN

group,lables = kNN.createDataSet()

print(kNN.classify0([1, 1], group, lables,3))