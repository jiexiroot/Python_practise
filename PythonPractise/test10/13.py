import numpy as np
import pandas as pd
df = pd.DataFrame({'省份': ['城市-A', '城市-A', '城市-B', '城市-B', '城市-C', '城市-C'],
                   '编码': ['ab33.33gp', 'ab33.335s', 'ab33.88ps', 'ab33.899g', 'ab33.92ag', 'ab33.92ap'],
                   '城市': ['城市-B', '城市-C', '城市-A', '城市-C', '城市-A', '城市-B'],
                   'suzhilie1': [np.nan, 211.86, 211.87, 211.87, 211.85, 211.85],
                   'suzhilie2': [33.88, 33.92, 33.98, 33.92, 33.33, 33.88],
                   'suzhilie3': [211.87, 211.85, 211.86, 211.85, np.nan, 211.87]},
                  columns=['省份', '编码', '城市', 'suzhilie1', 'suzhilie2', 'suzhilie3'])
df1 = df.copy()

df1.columns = ['省份', '编码', '城市', 'suzhilie1', 'suzhilie2', 'suzhilie3']
print(df1)
df1.rename(columns={'省份':0,'编码':1,'城市':2,'suzhilie1':3,'suzhilie2':4,'suzhilie3':5})
print(df1 )  #非原地修改，df1的columns未变
df1.rename(columns={'省份':0,'编码':1,'城市':2,'suzhilie1':3,'suzhilie2':4,'suzhilie3':5},inplace=True)
print(df1)
