def div(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("出现了以0为除数的异常")  # 提示出现了异常
        y = float(input("请输入一个非0的值："))  # 要求重新提供一个非0的值
        z = x / y
        return z
    else:
        return z


print(div(5, 0))
print(div(5, 7))
