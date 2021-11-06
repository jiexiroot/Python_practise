# 第一步：导入os
import os
# 第三步：引入time模块
import time

# 第二步：使用os.rename方法对python.txt进行重命名
os.rename('python.txt', 'linux.txt')

# 第四步：休眠20秒
time.sleep(20)

# 第五步：删除文件（linux.txt）
os.remove('linux.txt')

