# 1、接收用户输入的文件名（要备份的文件名称）
oldname = input('请输入要备份的文件名称：')  # Python.txt
# 2、规划备份文件名
# 搜索点号
index = oldname.rfind('.')
# 对index进行判断 判断是否合理（index > 0）
if index>0:

    # 返回文件名很文件后缀
    name = oldname[:index]
    postfix = oldname[index:]
    newname = name + '[备份]' + postfix
    print(newname)
    # 3、对文件进行备份操作
    old_f = open(oldname,'r')
    new_f = open(newname,'w')

    # 读取源文件内容写入新文件
    while True:
        content = old_f.read(1024)
        if len(content) == 0:
            break
        new_f.write(content)

    # 4、关闭文件
    new_f.close()
    old_f.close()
else:
    print("请输入正确的文件名称，否则无法进行备份操作。。。")
    