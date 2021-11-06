import time


def index(name, age):
    print(f'身份码 name:{name},年龄：{age}')
    time.sleep(3)


# def fun2(name,age):
# start = time.time()
# index(name, age)
#
# end = time.time()
# print(f'使用时间：{end - start}')


def fun3(x):
    def fun_3(*args, **kwargs):
        start = time.time()
        x(*args, **kwargs)
        end = time.time()
        print(f'使用时间：{end - start}')
    return fun_3


index = fun3(index)
index('xiaoming', 18)
