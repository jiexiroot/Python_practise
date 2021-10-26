filename = input('请输入你要上传文件的名称：')
# 获取点号的索引
index = filename.find('.')
print(index)
name = filename[:index]
print(f'上传文件的名称：{name}')
# 使用切片截取文件的后缀
postfix = filename[index:]
print(f'上传文件的后缀：{postfix}')
