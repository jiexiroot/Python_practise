import numpy as np
import pandas as pd
df=pd.DataFrame({"id":[1001,1002,1002,1003,1004,1004,1005,1006,np.NaN], \
                 "date":pd.date_range('20180101', periods=9),  \
                 "city":['Beijing','shanghai','Shanghai     ','Guangzhou   ','Shenzhen','Shenzhen','Nanjing','Changzhou', np.nan],  \
                 "city":['Beijing','shanghai','Shanghai     ','Guangzhou  ', 'Shenzhen','Shenzhen','Nanjing','Changzhou', np.nan],  \
                "age":[-18,20,20,28,36,36,42,152,np.NaN], \
                "category":['2018-A','2018-B','2018-B','2018-C','2018-D','2018-D','2018-E','2018-F',np.NaN],  \
                "age":[-18,20,20,28,36,36,42,152,np.NaN],  \
                "price":[1200,np.nan,np.nan,2500,5500,5500,np.nan,4300,np.nan],  \
                "na":[np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]},   \
                columns=['id','date','city','city','age','category','age','price','na'] )
print(df)
print(df.shape)
print(df.isnull().any(axis=0).sum())
print(df.isnull().all(axis=0).sum())
print(df.isnull().any(axis=0))
print(df.isnull().any(axis=0).sum())
print(df.isnull().all(axis=1).sum())
print(df.isnull().any(axis=1))
#2.处理缺失数据的方法
#①填充0或者均值
df1 = df
print(df1)
print(df1.fillna(value=0))
df1['price']=df1['price'].fillna(value=df['price'].mean())#对price列所有制的均值进行填充
print(df1)
#②删除不完整的行和列
print('②删除不完整的行和列')
print(df1.dropna(axis=1,how='all'))#删除全为空值（NaN）的列
print(df1.dropna(axis=1,how='any'))#删除任何空值（NaN）的列，行不删除
print(df1.dropna(axis=1,how='all').dropna(axis=0,how='any'))#删除任何空值（NaN）行、列
print('③其他处理方法')
print(df1.iloc[8,1])#选中8行1列元素
print(df1.iloc[1:4,3])#选取1/2/3行，第3列的数据
print(df1.loc[1:3,'city'])

df1.iloc[8,1] = np.nan#给df1的8行1列元素赋空值，由于该字段是时间类型，因此是NaT
print(df1)
df2 = df1.drop(['price'],axis=1)#删除price列，用del可以删除列，如del df1['price']
print(df2)
df3 = df2.dropna(axis=0,how='all')
print(df3)
df3.iloc[0,7] = 99
df3.iloc[1,7] = 88
print(df3)
print(df3.dropna(axis=0,how='any'))#删除任何包含空值的行。列不删除
print(df3.dropna(thresh=2))#一行中至少有2个非空值的数据才可以保留
print(df3.dropna(thresh=8))#一行中至少要有8个非控制的数据才可以保留下来
#2.去重
dfqc = pd.DataFrame({'a':[1,1,4,3,3],'b':[2,2,3,2,2],'c':[3,3,2,2,4]})
dfqc1 = dfqc
print(dfqc1)
dfqc1.drop_duplicates(subset=['a'],keep='first',inplace=False)
print(dfqc1)
dfqc1.drop_duplicates(subset=['a'],keep='last')
print(dfqc1)
dfqc1.drop_duplicates(subset=['a'],keep=False)
print(dfqc1)
dfqc1.drop_duplicates(subset=['a','b','c'])
print(dfqc1)
dfqc1.drop_duplicates(subset=None,keep='first',inplace=False)
print(dfqc1)
print(dfqc1)
dfqc1.drop_duplicates(inplace=True)
print(dfqc1)
print(dfqc)
#删除数据间的空格
df=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006], \
                 "date":pd.date_range('20180101',periods=6), \
                 "city":['BeiJing','          ShangHai','GuangZhou   ','ShenZhen   ','   NanJing','   ChangZhou'], \
                 "age":[-18,26,28,36,42,152], \
                 "category":['2018-A','2018-B','2018-C','2018-D','2018-E','2018-F'],  \
                 "price":[1200,2500,5500,5500,4300,6200]} , \
                 columns=['id','date','city', 'age','category', 'price'] )
print(df)
df1 = df.copy()
print(df1)
df1['city'] = df1['city'].map(str.lstrip)#单独去除左边的空格
print(df1)
df1['city'] = df1['city'].map(str.rstrip)#单独去除右边的空格
print(df1)
df1 = df
print(df1)
#4.字母大小写转换
df1['city'] = df['city'].str.lower()#转小写
print(df1)
df1['city'] = df['city'].str.upper()#转大写
print(df1)
df1['city'] = df['city'].map(str.lower)#转小写
print(df1)
df1['city'] = df['city'].map(str.upper)#转大写
print(df1)
df1['city'] = df['city'].map(str.title)#转换首字母为大写
print(df1)
#5.关键字内容统一检查
df = pd.DataFrame({'a':[18,88,92,22,200],'b':[22,'a',100,90,42],'c':['a','c','d','e','f'],'d':['d','e','a','66','k'],'e':['q','z','#','e','r']},columns=list('abcde'))
print(df)
print(df.info())
print(df['a'].astype(np.string_))
df['a'] = df['a'].astype(np.string_)
print(df)
print(df.info())
print(df['a'].apply(lambda x:x.isdigit()))
df['b'] = df['b'].astype(np.string_)
print(df['b'].apply(lambda x:x.isdigit()))
print(df['c'].apply(lambda x:x.isalnum()))
print(df['e'].apply(lambda x:x.isalnum()))
print(df['c'].apply(lambda x:x.isalpha()))
#6.异常值和极端值查看
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
print(df1.describe().T)
print(df1.describe().astype(np.int64))
#7.数据替换
print(df1)
#df1.replace([0,11],df.mean())#用平均值替换，抛出异常，平均值形状不一致
print(df1.mean())
print(df1.mean().mean())#各列平均值再求平均值
df1.replace([0,11],df1.mean().mean())
print(df1)
df1.replace([0,11],df1.mean().mean(),inplace=True)
print(df1)
df = pd.DataFrame({'省份':['城市-A','城市-A','城市-B','城市-B','城市-C','城市-C'],
                   '编码':['ab33.33gp','ab33.335s','ab33.88ps','ab33.899g','ab33.92ag','ab33.92ap'],
                    '城市':['城市-B','城市-C','城市-A','城市-C','城市-A','城市-B'],
                   'suzhilie1':[np.nan,211.86,211.87,211.87,211.85,211.85],
                   'suzhilie2':[33.88,33.92,np.nan,33.92,33.33,33.88],
                   'suzhilie3':[211.87,211.85,211.86,211.85,np.nan,211.87]},
                  columns=['省份','编码','城市','suzhilie1','suzhilie2','suzhilie3'])
print(df)
df1=df.copy()#深拷贝
print(df1)
print(df1.info())
df1['suzhilie3'].replace(211.85,'A',inplace=True)
print(df1)
print(df1.info())
print(df1.replace(['A',33.88],['B',100]))
print(df1)



