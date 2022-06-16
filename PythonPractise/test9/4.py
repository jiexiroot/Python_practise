import numpy as np
import pandas as pd

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],"date":pd.date_range('20180101', periods=6),"city":['Beijing', 'shanghai', 'guangzhou ', 'Shenzhen', 'nanjing', 'changzhou'], "age":[18,26,28,36,42,52],"category":['2018-A','2018-B','2018-C','2018-D','2018-E','2018-F'], "price":[1200,np.nan,2500,5500,np.nan,4300]},columns =['id','date','city','category','age','price'])
print(df.head())              #查看前5行数据
print(df.tail())                 #查看后5行数据
