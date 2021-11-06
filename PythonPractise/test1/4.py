list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = (i for i in list1 if i < 8)
print(a.__next__())
