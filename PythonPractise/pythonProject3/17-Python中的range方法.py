result = 0
for i in range(1, 101):
    if i % 2 == 0:
        result += i
print(f'1~100的偶数和为{result}')
