import numpy as np
import pandas as pd

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],"date":pd.date_range('20180101', periods=6),"city":['Beijing', 'shanghai', 'guangzhou ', 'Shenzhen', 'nanjing', 'changzhou'], "age":[18,26,28,36,42,52],"category":['2018-A','2018-B','2018-C','2018-D','2018-E','2018-F'], "price":[1200,np.nan,2500,5500,np.nan,4300]},columns =['id','date','city','category','age','price'])
print(df)                                                           #显示df的值，带索引列（自动添加）和column行
df1=df
print(df1)
print("*"*60)
print('df的类型\n',type(df))           #输出df的类型
print("*"*60)
print('df的维数\n',df.ndim)            #输出df的维数
print("*"*60)
print('df的形状\n',df.shape)           #输出df的形状
print("*"*60)
print('df各列数据类型\n',df.dtypes)         #输出df各列数据类型
df1=df
print(df1)
print("*"*60)
print(df.info())
print("*"*60)
print(df['date'])             # 输出DataFrame ‘date’列的值
print("*"*60)
print(df[['age','price']])  # 输出DataFrame ’age’,’price’列的值

print(df.isnull())      # 以二维表格形式，输出每个元素对应是否为空值NaN

print(df.isnull().any(axis=0))  # 查看各列是否存在空值，True表示有空值, False表示无空值
print(df.values )                      # df.values的类型是二维数组类型

print(df.columns)           # 输出df的列名称，df.columns的类型是Index类型


print(df.index)               # 输出df的索引，是Int64Index类型

print(type(df.index))      # 输出df.index的类型，是Int64Index类型
