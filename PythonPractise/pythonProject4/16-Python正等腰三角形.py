# 初始化计数器
i = 1
while i <= 6:
    j = 1
    # 输出空格
    print(' ' * (6 - i), end='')
    # 编辑循环条件
    while j <= (2 * i - 1):
        print('*', end='')
        j += 1
    # 更新计数器
    i += 1
    print('')