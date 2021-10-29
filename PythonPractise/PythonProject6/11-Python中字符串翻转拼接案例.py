def func(str2):
    str2 = str2[::-1]
    return str2.replace('.', '-')


def func2(str2):
    list1 = str2.split('.')
    list1.reverse()
    return '-'.join(list1)


# 调用函数实现字符串翻转拼接
str1 = '1.2.3.4.5'
print(func(str1))  # 5-4-3-2-1
print(func2(str1))  # 5-4-3-2-1
