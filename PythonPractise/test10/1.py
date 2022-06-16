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
print(df.shape)      #df的形状9行9列
print(df.isnull().any(axis=0).sum())   #df有空值列的列数量共计8列
print(df.isnull().all(axis=0).sum())   #df有全部是空值列的列数量共计1列
