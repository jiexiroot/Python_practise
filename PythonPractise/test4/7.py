def div(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("出现了以0为除数的异常！")  # 提示出现了异常
    except TypeError:
        print("被除数和除数应为数值类型！")
    else:
        return z

print(div(5, "b"))
print(div(5, 0
))
