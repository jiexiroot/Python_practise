num1 = 10
num2 = 20

if num1 > num2:
    print(f'最大值为{num1}')
else:
    print(f'最大值为{num2}')

max = num1 if num1 > num2 else num2
print(f'最大值为{max}')
