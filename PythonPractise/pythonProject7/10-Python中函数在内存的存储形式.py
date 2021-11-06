def fn1():
    return 100


# 调用fn1 函数
print(fn1)  # 返回fn1函数在内存中的地址
print(fn1())  # 代表找到fn1函数的地址并立即执行

fn2 = lambda: 100

print(fn2)  # 返回fn2在内存中的地址
print(fn2())


