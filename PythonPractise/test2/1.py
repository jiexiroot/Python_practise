import random

# n = random.randint(1,3)
# n1 = random.randint(1,3)
# list1 = [1, 3, 5, 7, 9]
#
# n = random.randrange(1, 3)
# n2 = random.sample(list1, 3)
# print(n)
# print(n2)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(list1)
# print(list1)
# 生成6位验证  数字+大写字母的验证嘛

for i in range(3):
    x = str(random.randint(0, 9))
    y = chr(random.randint(65, 90))
    z = x + y
    print(z, end='')
