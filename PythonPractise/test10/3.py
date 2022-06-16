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
print("*"*60)
print(df.dropna(axis=1,how='all'))  #删除一整列全为空值NaN的列
df1=df
print(df1)
print("*"*60)
print(df1.dropna(axis=0,how='any') ) #删除任何包含空值NaN的行，列不删除
print("*"*60)
print(df1.dropna(axis=1,how='any') ) #删除任何包含空值NaN的列，行不删除
print("*"*60)
print(df1.dropna(axis=1,how='all').dropna(axis=0,how='any'))#删除全为空值NaN的列和有空值NaN的行
df1=df
print(df1)
print("*"*60)
print(df1.iloc[8,1])      # 选取8行1列元素
print("*"*60)
print(df1.iloc[1:4,5] )      #选取1、2、3行，第5列的数据
print("*"*60)
print(df1.loc[1:3,"city"])      #选取1、2、3行，“city”列的数据
df1=df
print(df1)
print("*"*60)
#iloc是根据行号来索引的，从0行开始，loc是根据行的索引号来索引的
df1.iloc[8,1] = np.nan   # 给df1的8行1列元素赋空值NaN，由于该字段是时间类型因此是NaT
print(df1)
print("*"*60)
df2 = df1.drop(['price'],axis=1)  # 删除price列；用del也可以删除列del df1['price']
print(df2)


