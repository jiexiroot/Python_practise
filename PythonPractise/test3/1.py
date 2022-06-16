import random

print("猜数字游戏,输入一个 1-100 以内的数字")
random_num = random.randint(1, 100)
print(random_num) # 打开注释可查看生成的随机数
for i in range(1, 6):
    number = input("请输入一个数字:")
    if number.isdigit() is False:
        print('请输入一个正确的数字')
    elif int(number) < 0 or int(number) > 100:
        print("请输入 1-100 范围的数字")
    elif random_num == int(number):
        print("恭喜你用了%d 次猜对了" % i)
        break
    elif random_num > int(number):
        print("很遗憾，你猜小了")
    else:
        print("很遗憾，你猜大了")
    if i == 5:
        print("很遗憾，%d 次机会已用尽，游戏结束,答案为%d" %
              (i, random_num))
