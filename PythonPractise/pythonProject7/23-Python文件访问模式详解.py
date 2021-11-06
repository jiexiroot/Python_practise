# 1、打开文件
f = open('python.txt', 'rb')
# 2、读写文件
# f.write('\n555')
content = f.read(3)
print(content)
# 3、关闭文件
f.close()