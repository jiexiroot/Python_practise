import numpy as np
import pandas as pd
df = pd.DataFrame({'省份':['城市-A','城市-A','城市-B','城市-B','城市-C','城市-C'],
                   '编码':['ab33.33gp','ab33.335s','ab33.88ps','ab33.899g','ab33.92ag','ab33.92ap'],'城市':['城市-B','城市-C','城市-A','城市-C','城市-A','城市-B'],
                   'suzhilie1':[np.nan,211.86,211.87,211.87,211.85,211.85],
                   'suzhilie2':[33.88,33.92,np.nan,33.92,33.33,33.88],
                   'suzhilie3':[211.87,211.85,211.86,211.85,np.nan,211.87]},
                    columns=['省份','编码','城市','suzhilie1','suzhilie2','suzhilie3'])
print(df)
df1 = df.copy()         #深复制备份
print(df1)
print(df1.info())
df1['suzhilie3'].replace(211.85,'A',inplace=True) #对df1指定1列原地操作，数值211.85被字符A代替
print(df1)
#df1整体操作，前列表多个值，替换为后面1个值，类型不同
print(df1.replace(['A',33.88],'B') )
df1['城市'].replace(['城市-B','城市-A'],['A','E'],inplace=True)
print(df1)
print(df1.replace('[A-Z]','城市',regex=True))
print(df1)   #上一步操作没有给df1重新赋值，或使用原地inplace=True,因此df1未变
print(df1.replace(33.88,'B') )
df1['编码'] = df1['编码'].replace('33.88','B')
print(df1)
df1['编码']=df1['编码'].str.replace('33.88','B')
print(df1)
# suzhilie2列有空值NaN，不能更改数据格式
df1['suzhilie2'] = df1['suzhilie2'].astype(np.int64)







