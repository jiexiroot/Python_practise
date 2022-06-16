import numpy as np
import pandas as pd
df = pd.DataFrame({'a':[18,88,92,22,200],'b':[22,'a',100,90,42],'c':['a','c','d','e','f'],
                   'd':['d','e','a',66,'k'],'e':['q','z','#','e','r']},columns=list('abce'))

df['b'] = df['b'].astype(np.string_)     # 修改'b'列内容，转换成字符串类型
print(df['b'].apply(lambda x: x.isdigit()))    # 判断' b'列内容是否全部为数字
print(df['c'].apply(lambda x: x.isalnum()) )  # 'c'列内容是否全部为字母和数字




print(df['e'].apply(lambda x: x.isalnum()) )  # 'e'列内容是否全部为字母和数字
print(df['c'].apply(lambda x: x.isalpha()))  # ‘c’列内容是否全部为字母

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1.describe().T)  # 查看数值型列的汇总统计，并转置
print(df1.describe().astype(np.int64))  # 查看数值型列的汇总统计，转换成整型
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)   #如最大值11和最小值0是异常值，可以使用replace函数替换异常数据
print(df1.replace([0,11],df1.values.mean()))
print(df1.mean())
print(df1.mean().mean() ) # df1各列的平均值再求平均值
print(df1.replace([0,11],df1.mean().mean()))
print(df1)    # df1值未改变
# inplace=True原地操作，df1值被改变
df1.replace([0,11],df1.mean().mean(),inplace=True)
print(df1)





