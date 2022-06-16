total = 0  # 定义一个全局变量


def sum(a, b):
    """使用关键字'global'说明全局变量之后，才可以修改其值，否则只能引用其值，不能修改"""
    global total
    total = a + b


print("全局变量修改前的值为：%d" % total)
sum(25, 38)
print("全局变量修改后的值为：%d" % total)
