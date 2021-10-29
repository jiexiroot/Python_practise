import random

str1 = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
list1 = []
code = ""
for i in range(0, 4):
    number = random.randint(0, len(str1)-1)
    list1.append(str1[number])
    code += str1[number]
print(list1)
print(code)


#
# import random
#
#
# # 1、定义一个字符串
# str1 = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
# code = ""
# # 2、编写循环，只循环4次
# for i in range(4):   # 0 1 2 3
#     # 3、随机获取str1中的某个字符
#     index = random.randint(0, len(str1) - 1)
#     code += str1[index]
# # 4、打印4位随机验证码
# print(code)