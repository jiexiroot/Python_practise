import numpy as np
import pandas as pd


#从3D ndarry类型的对象创建
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print(p['Item1'])
print(p.major_xs(1))
