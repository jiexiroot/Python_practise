def user_info(**kwargs):
    # print(kwargs)  # 字典类型数据，对传递参数没有顺序要求，格式要求key = value值
    print(f'我的名字是{kwargs["name"]}，今年{kwargs["age"]}岁了，住在{kwargs["address"]}')


# 调用函数，传递参数
user_info(name='Tom', address='美国纽约', age=23)
