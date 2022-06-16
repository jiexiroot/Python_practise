import pandas as pd
dfqc = pd.DataFrame({'a':[1,1,4,3,3],'b':[2,2,3,2,2],'c':[3,3,2,2,4]})
dfqc1 = dfqc
print("*"*50)
print(dfqc1)
#a列元素有重复第一行保留其余行去除
print("*"*50)
print(dfqc1.drop_duplicates(subset=['a'],keep='first',inplace=False))
#a列元素有重复，最后一行保留其余行去除
print("*"*50)
print(dfqc1.drop_duplicates(subset=['a'],keep='last'))
#a、 b、c列元素都有重复，第一行保留其余行去除
print(dfqc1.drop_duplicates(subset=['a'],keep=False))

# subset=None所有列元素相同的行去除
print(dfqc1.drop_duplicates(subset=['a','b','c']) )

#dfqc1值经过以上操作未变，因inplace默认为False，即生成一个副本未在原DataFrame上删除
print(dfqc1.drop_duplicates(subset=None,keep='first',inplace=False))
print(dfqc1)

#inplace=True在原DataFrame上删除重复行，默认False生成副本
print(dfqc1.drop_duplicates(inplace=True))
