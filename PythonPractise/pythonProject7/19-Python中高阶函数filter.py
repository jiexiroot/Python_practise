# 定义一个函数（获取所有的偶数）
def func(i):
    return i % 2 != 0


# 定义一个序列
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# 调用filter函数进行过滤操作
result = filter(func, list1)
print(list(result))

print(21 % 2)
print(20 % 2)
print(19 % 2)
print(19 % 5)