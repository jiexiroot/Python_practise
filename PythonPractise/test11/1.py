# 列表推导公式 lambda
# mylist = [int(input()) for i in range(7)]
from functools import reduce

mylist = [10, 12, 13, 13, 14, 15, 16]

# 1
print(len(mylist))
# 2
print(mylist.count(13))
# 3
# for index, value in enumerate(mylist, start=0):
#     if int(value) == 10:
#         mylist.insert(index+1,'11')
mylist.insert(mylist.index(10) + 1, 11)
print(mylist)

# 4 按索引号删除列表元素的第二个13
first_index = mylist.index(13)

mylist2 = mylist[first_index + 1:]
second_index = mylist2.index(13)

mylist.pop(first_index + second_index + 1)
print(mylist)

# 5
mylist.remove(14)

# 6
t_value = mylist[3]
print(t_value)

# 7
mylist[0] = 9

# 8
mylist.reverse()
print('mylist=',mylist)
# 9
sum1 = 0
for key, value in enumerate(mylist, start=1):
    sum1 += value
print('sum=',sum1)
# filter过滤  reduce叠加 sorted排序
# 必须需要两个参数 前一个参数为合计值，后一个为计算值
print('sum=',reduce(lambda x,y: x+y, mylist))

# 10
list1 = mylist[0:3]
print("list1=",list1)

# 11
list2 = mylist[-1:-4:-1]
print("list2=",list2)

# 12
del mylist[1:5]
print(mylist)

# 13
mytu = tuple(mylist)
print(mytu)

# 14
del mylist

# 15
list3 = list1
list3.extend(list2)
print('list3=',list3)

# 16
list2.clear()