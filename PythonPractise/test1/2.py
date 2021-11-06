# for i in range(1, 101):
#     print(i)
#
# i = 1
# while i < 101:
#     print(i)
#     i += 1
#
#

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list1.__iter__()
i = 0
# while i < 10:
#     print(a.__next__())
#     i += 1

print(type(a.__next__()))