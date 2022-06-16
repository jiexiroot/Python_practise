import pandas as pd

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20180101', periods=6),
                   "city": ['BeiJing', '  ShangHai  ', 'GuangZhou ', 'ShenZhen  ', '  NanJing', '  ChangZhou   '],
                   "age": [-18, 20, 28, 36, 36, 152],
                   "category": ['2018-A', '2018-B', '2018-C', '2018-D', '2018-E', '2018-F'],
                   "price": [1200, 2500, 5500, 5500, 4300, 6200]},
                  columns=['id', 'date', 'city', 'age', 'category', 'price'])

print(df)
df1 = df.copy()
print(df1)
df1['city'] = df1['city'].map(str.lstrip)  # 单独去除左边空格
print(df1)

df1['city'] = df1['city'].map(str.rstrip)  # 单独去除右边空格
print(df1)
df1['city'] = df1['city'].str.lower()  # 将city列转换成小写字母
print(df1)

df1['city'] = df1['city'].str.upper()  # 转换成大写字母
print(df1)

df1['city'] = df1['city'].map(str.lower)  # 转换成小写字母
print(df1)

df1['city'] = df1['city'].map(str.upper)    # 转换成大写字母

df1['city'] = df1['city'].map(str.title)  # 转换成首字母大写

