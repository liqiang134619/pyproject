print("hello")

import  numpy as np

########## 创建数组
# 没有初始化
x = np.empty([1,2,3],dtype=int)
print(x)
# 初始化0
x = np.zeros([3,3,3],dtype=int)
print(x)

# 指定范围和步长
x = np.arange(1,5,2)
print(x)

a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])

# 冒号 : 的解释：如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。如果为 [2:]，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

##### NumPy 高级索引
# 整数索引
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print  ('这个数组的四个角元素是：')
print (y)
print(x[2,2])
print  ('=------------------------"：')
print(x[0,0])

print("=======================================")

#  布尔索引
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])

print (x[x >  5])

