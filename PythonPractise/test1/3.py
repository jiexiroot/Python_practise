# def range(start, stop, a):
#     while start < stop:
#         start += a
#         print(start)
#
#
# range(1, 100, 1)



def index(name):
    print(f'{name} 开始吃东西了')
    while True:
        x = yield
        print(f'{name} 开始吃{x}')

a = index('jiexi')
print(a.__next__())
print(a.send('屎坨坨'))

print(a.send('肉'))


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))