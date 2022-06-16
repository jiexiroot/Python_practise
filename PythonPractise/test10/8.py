import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [18, 88, 92, 22, 200],
                   'b': [22, 'a', 100, 90, 42],
                   'c': ['a', 'c', 'd', 'e', 'f'],
                   'd': ['d', 'e', 'a', 66, 'k'],
                   'e': ['q', 'z', '#', 'e', 'r']},
                  columns=list('abcde'))
print(df)

print(df.info())  # 查看df基本信息

print(df['a'].astype(np.string_))  # 将'a'列内容转换成字符串

df['a'] = df['a'].astype(np.string_)    # 修改'a'列内容，转换成字符串类型
print(df['a'])

print(df['a'].apply(lambda x: x.isdigit()))    # 判断'a'列字符串内容是否全部为数字
#注：添加import numpy as np

print(df)
