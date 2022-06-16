import numpy as np
import pandas as pd

# 用Series()创建Series类型对象
# np.nan的值为NaN，表示数据值缺失
s = pd.Series([1, 3, 4, 5, 6, np.nan, 8, np.nan, 10])
print(s)  # 输出s，显示成一列，有索引，元素类型默认是float64

print(s.dtype)  # 输出s中元素类型，默认是float64


print(s.ndim)  # 输出s维数


print(s.shape)  # 输出s形状

