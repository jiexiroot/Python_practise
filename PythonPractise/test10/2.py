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
df1 = df
print(df1)
#用0进行填充，当然填的值要根据具体处理对象进行选择
print('填充0操作：\n',df1.fillna(value=0))
#对price列所有值的均值填充
df1['price'] = df1['price'].fillna(value=df1['price'].mean())
print('填充均值操作：\n',df1)
