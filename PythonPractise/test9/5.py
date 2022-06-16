import numpy as np
import pandas as pd

print(np.random.randn(5, 4))
dates = pd.date_range('20180101', periods=5)
print(dates)
# 指定DataFrame的values、index和columns，用pandas的DataFrame()创建二维表格
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
print(df)

dates = pd.date_range('20180101', periods=5)
df = pd.DataFrame(np.random.randn(5,4), index=dates, columns=['A','B','C','D'])
print(df)

df = pd.DataFrame(np.random.randn(5,4))
print(df)
