import numpy as np
import pandas as pd

s = pd.Series([1, 3, 4, 5, 6, np.nan, 8, np.nan, 10])
print(type(s))  # 输出s的类型，是Series类型

print(s.values)  # 输出s的values值

print(s.values)  # 输出s的values值，值是数组类型

print(type(s.values))  # 输出s.values的类型是ndarray数组类型
# 输出s每个元素对应是否为空值NaN，False表示非空值，True表示是空值
print(s.isnull())

# 查看列是否存在空值，True表示有空值, False表示无空值
print(s.isnull().any(axis=0))

print(s.isnull().any())  # 省略any()参数axis=0，功能同上

# 计算有空值列的数量，要么是1，要么是0，因为只有1列
print(s.isnull().any(axis=0).sum())
