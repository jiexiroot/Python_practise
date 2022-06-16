import numpy as np
import pandas as pd
date = ['2017-6-26', '2017-6-27']
pd.to_datetime(date)
dates = ['2017-06-20', '2017-06-21', '2017-06-22', '2017-06-23', '2017-06-24', '2017-06-25', '2017-06-26', '2017-06-27']
s_date = pd.Series(dates)
print(s_date)      #数据类型为object
f_date = pd.to_datetime(s_date,format="%Y-%m-%d")
print(f_date)      #格式化后，类型变为datetime64[ns]
