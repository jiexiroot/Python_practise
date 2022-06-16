import numpy as np
import pandas as pd
df = pd.DataFrame({'省份':['城市-A','城市-A','城市-B','城市-B','城市-C','城市-C'],
                   '编码':['ab33.33gp','ab33.335s','ab33.88ps','ab33.899g','ab33.92ag','ab33.92ap'],'城市':['城市-B','城市-C','城市-A','城市-C','城市-A','城市-B'],
                   'suzhilie1':[np.nan,211.86,211.87,211.87,211.85,211.85],
                   'suzhilie2':[33.88,33.92,np.nan,33.92,33.33,33.88],
                   'suzhilie3':[211.87,211.85,211.86,211.85,np.nan,211.87]},
                    columns=['省份','编码','城市','suzhilie1','suzhilie2','suzhilie3'])
print(df)
df1 = df.copy()
df1['suzhilie2'] = df1['suzhilie2'].fillna(df1['suzhilie2'].mean())
print(df1)
# suzhilie2列数据格式改为np.int64
df1['suzhilie2'] = df1['suzhilie2'].astype(np.int64)
print(df1)
df1['suzhilie2'] = df1['suzhilie2'].astype(np.float64)
print(df1)
print(df1.info())


