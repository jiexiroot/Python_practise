import os

#
# path = os.path.isdir('E:/PycharmProjects/PythonPractise/test2')
# if path:
#     print('123')
# else:
#     print('456')
#
#
# x = os.path.dirname(__file__)
# print(x)
#
# # 对路径的拼接
join = os.path.dirname(__file__)
print(join)
path = os.path.join(join, 'log', '123.txt')
# # 对路径的拼接
print(path)
with open(path, mode='w', encoding='utf-8') as f:
    f.write('123465')
