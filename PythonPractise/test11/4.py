def pow(x, n=2):
    sum = x
    # for i in range(n-1):
    #     sum*=x
    sum = sum ** n

    print(f'{x}^{n}={sum}')
    return sum

# pow(int(input('请输入x')))
# pow(int(input('请输入x')),int(input('请输入n')))

# y = lambda x: pow(x) + 2 * x + 1
# print(y(int(input('请输入x的值'))))

y2 = lambda x,y,z: pow(x) + pow(y) + z
print(y2(int(input('请输入x的值')),int(input('请输入y的值')),int(input('请输入z的值'))))
