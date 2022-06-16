import numpy as np
import pandas as pd
df = pd.DataFrame({"id":[1001,1002,1002,1003,1004,1004,1005,1006,np.nan],
                   "date":pd.date_range('20180101', periods=9),
                   "city":['BeiJing', 'ShangHai','ShangHai   ','GuangZhou   ', 'ShenZhen','ShenZhen   ', 'NanJing', 'ChangZhou',np.nan],
                   "city":['BeiJing', 'ShangHai','ShangHai','GuangZhou ', 'ShenZhen','ShenZhen', 'NanJing', 'ChangZhou',np.nan],
                   "age":[-18,20,20,28,36,36,42,152,np.nan],
                   "category":['2018-A','2018-B','2018-B','2018-C','2018-D','2018-D','2018-E','2018-F',np.nan],
                   "age":[18,20,20,28,36,36,42,152,np.nan],
                   "price":[1200,np.nan,np.nan,2500,5500,5500,np.nan,4300,np.nan],
                   "na":[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]}, columns =['id','date','city','city','age','category','age','price','na'])
print(df)
df3 = df.copy()
# 删除任何包含空值的行，列不删除

print(df3.dropna(axis=0, how='any'))

print(df3.dropna(thresh=2))  # 一行中至少要有2个非空值的数据是可以保留下来

print(df3.dropna(thresh=8))  # 一行中至少要有8个非空值的数据是可以保留下来

# 删除一整行全为空值的行，参数axis可以省咯，默认是axis=0

df3 = df.dropna(axis=0, how='all')
print(df3)

# 修改第1，2行第7列前两个元素值为99
df3.iloc[0, 7] = 99
df3.iloc[1, 7] = 88
print(df3)

