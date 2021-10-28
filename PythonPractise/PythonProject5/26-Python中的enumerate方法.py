list1 = [10, 20, 30, 40, 50]
n = 1
for i in list1:
    print(f'第{n}个数：{i}')
    n += 1

print('-' * 40)
for key, value in enumerate(list1, start=1):
    print(f'第{key}个数：{value}')

    
