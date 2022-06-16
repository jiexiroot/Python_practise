import numpy as np
import pandas as pd

# 1.数据表合并
# 1.1使用merge()方法进行合并
df1 = pd.DataFrame({'id': ['1001', '1002', '1003'], 'name': ['mily', 'jake', 'merry']})
print(df1)
df2 = pd.DataFrame({'id': ['1001', '1002', '1004'], 'score': [82, 95, 77]})
print(df2)
df3 = pd.merge(df1, df2)  # 默认以重叠的列名当做连接键
print(df3)
# 当2个DateFrame对象的列名不相同时，需要用left_on和right_on进行设置
df22 = pd.DataFrame({'sid': ['1001', '1002', '1004'], 'score': [82, 95, 77]})
print(df22)
# df1中的id和df22中的sid作为连接键
df33 = pd.merge(df1, df22, left_on='id', right_on='sid')
# 左连接，保留左边df1中的所有行，如果有的列中没有数据，则以NaN填充
print(pd.merge(df1, df2, how="left"))
# 右连接，保留右边df2中的所有行，如果有的列中没有数据，则以NaN填充
print(pd.merge(df1, df2, how="right"))
# 外连接，相当于df1，df2的并集
print(pd.merge(df1, df2, how="outer"))
# 内连接，相当于df1,df2的交集
print(pd.merge(df1, df2, how='inner'))

# 1.2使用concat()方法进行拼接
df3 = pd.concat([df1, df2], axis=0, sort=True)  # axis=0是纵轴拼接，索引直接拼接
print(df3)
df4 = pd.concat([df1, df2], axis=1)  # axis=1是横轴拼接
print(df4)
print(pd.concat([df1, df2], axis=0, join='outer'))  # 并集
print(pd.concat([df1, df2], axis=0, join='inner'))  # 交集

# 1.2摄制索引列
df3 = pd.concat([df1, df2], axis=0)  # axis=0是轴拼接，索引直接拼接
print(df3)
# 使用reset_index()设置索引，原行索引作为一列保留，列名为index
print(df3.reset_index())
print(df3)  # 重新索引，inplace默认为False,所以df3保持原状
print(df3.reset_index(drop=True))  # 删除原索引列
# drop为True,就会移出该列的数据，设置id列为新索引
df4 = df3.set_index('id', inplace=False, drop=True)
print(df4)
print(df4.index)
print(df4.values)
# drop为False,就不移掉该列的数据
print(df3.set_index('id', inplace=False, drop=False))
df = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['A', 'B', 'C'])
print(df)
# 索引值不错在，引入缺失值NaN,增加D列，值为NaN
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D']))
print(df)  # 创建一个适应新索引的新对象，原对象不变
# 填充默认值
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D'], fill_value=0))
print(df)  # 创建一个适应新索引的新对象，原对象不变
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D'], method='ffill'))  # 向前填充
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D'], method='pad'))  # 同上
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D'], method='bfill'))  # 向后
print(df.reindex(index=['a', 'b', 'c', 'd'], columns=list(df.columns) + ['D'], method='backfill'))  # 向后

# 1.3按照索引列排序
print(df3)
print(df3.sort_index())  # 按索引排序
print(df4)
print(df4.sort_index())  # 按索引排序

# 1.4按照特定列的值排序
print(df3)
print(df3.sort_values(by=['score']))  # 按照score列排序

# 1.5根据条件填充列
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20180101', periods=6),
                   "city": ['Beijing', 'shanghai', 'guangzhou', 'Shenzhen', ' nanjing', 'changzhou'],
                   "age": [-18, 20, 28, 36, 36, 152],
                   "category": ['2018-A', '2018-B', '2018-C', '2018-D', '2018-E', '2018-F'],
                   "price": [1200, 2500, 5500, 5500, 4300, 6200]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
print(df)
# 增加一列group,并填充high或low
df['group'] = np.where(df['price'] > 3000, 'high', 'low')
print(df)
# 对符合条件的数据进行分组标记
# 此处NangJing前面有一个空格
df.loc[(df['city'] == ' nanjing') & (df['price'] >= 4000), 'sign'] = 1
print(df)

# 1.6 分列（拆分列）
df_split = pd.DataFrame((x.split('-') for x in df['category']), index=df.index, columns=['category', 'size'])
print(df_split)
# 合并数据
df = pd.merge(df, df_split, right_index=True, left_index=True)
print(df)
