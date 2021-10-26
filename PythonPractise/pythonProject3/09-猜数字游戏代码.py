import random

i = random.randint(1, 10)
print(i)
j = 0
while j < 3:
    key = int(input(f'请输入第{j + 1}次猜想的数（1~10）'))
    if i != key:
        s = '数字大了' if i < key else '数字小了'
        print(f'你猜的{s}')
    else:
        print(f'你猜对了，数字是{i}')
        break
    j += 1
