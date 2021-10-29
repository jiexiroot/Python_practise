# def greet(name):  # name就是在函数greet定义时，所编写的参数（形参）
#     return name + ',您好'
#
#
# # 调用函数
# name = '老王'
# print(greet(name))  # 在函数调用时，所传递的参数就是实际参数
def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')


# 调用函数
user_info('Tom', 23, '美国纽约')