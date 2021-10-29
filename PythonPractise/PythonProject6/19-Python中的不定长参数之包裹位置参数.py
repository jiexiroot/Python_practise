def user_info(*args):
    print(f'我的名字是{args[0]},今年{args[1]}岁了，住在{args[2]}')


# 调用函数，传递参数
user_info('Tom', 23, '美国纽约')
