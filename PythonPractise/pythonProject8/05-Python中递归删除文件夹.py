# 导入os模块
import os, shutil

# 调用rmdir方法尝试删除非空目录static
# os.rmdir('static')
shutil.rmtree('static')
