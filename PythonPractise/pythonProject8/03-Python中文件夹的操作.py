import os

# # os.mkdir('python1.txt')
# print(os.getcwd())
# for i in os.listdir():
#     print(i)
# os.chdir('../pythonProject7')
# print(os.getcwd())
# for i in os.listdir():
#     print(i)
#


# 1、使用mkdir方法创建一个images文件夹
# os.mkdir('images')
# os.mkdir('images/avatar')

# 2、getcwd = get current work directory

# print(os.getcwd())

# 3、os.chdir , ch = change dir = directory
os.chdir('images/avatar')
print(os.getcwd())

# 切换到上一级目录 =》 images
os.chdir('../')

# 4、使用os.listdir打印当前所在目录下的所有文件，返回列表
print(os.listdir())

# 5、删除空目录
os.rmdir('avatar')
