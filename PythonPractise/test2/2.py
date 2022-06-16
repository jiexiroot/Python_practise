# 猜数字游戏
import random

x = random.randint(0, 100)
while True:
    print("欢迎来到猜数字游戏".center(16, "="))
    n = input('请输入一个数字:').strip()
    if not n.isdigit():
        print('错误输入'.center(15, "="))
        continue
    else:
        n = int(n)
    if n < x:
        print("值猜小了".center(10, "="))
    elif n > x:
        print("值猜大了".center(10, "="))
    else:
        print("猜对了")
        break
