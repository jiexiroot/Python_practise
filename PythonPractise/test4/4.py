def div(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        print("程序出现异常，异常类型为：除数为0")


print(div(5, 0))
