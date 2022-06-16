# 23
name = "李强"
age = 12
print("你好，我叫%s，今年我%d岁了。" % (name, age))

# 24
name = "张明"
age = 21
print("你好！我的名字是：{}，今年我{}岁了。".format(name, age))

# 26
name = '张天'
age = 20
gender = '男'
print(f'我的名字是{name},今年{age}岁了,我的性别是：{gender}。')

# 31
alist = [1, 4, 2, 2, 3, 4, 4]
print(alist)
alist.append(2)  # 在列表尾部追加元素“2”
print(alist)
alist.insert(3, 8)  # 在第3（左边第一个元素的位置为0）个位置插入元素“8”，
print(alist)
pop = alist.pop()
print(pop)
print(alist)
print('-'*25)
# 35
alist = [3, 4, 2, 9, 12, 6, 18, -6]
print(alist[:])  # 取全部元素

print(alist[0:])  # 取全部元素

print(alist[:-1])  # 取除最后一个元素外的所有元素， alist[:-1]等价于x[0:-1:1]

print(alist[2:5])  # 取序号是2、3、4的元素，不包含最后一个序号的元素

print(alist[::2])  # 从0开始隔一个取一个元素

print(alist[1:5:2])  # 从1开始，每隔一个取一个元素，直到5为止

print(alist[::-1])  # 从右向左取全部成员

print(alist[5:0:-2])   # 从右向左隔一个取一个元素，不包含0

# alist[:-1]等价于x[0:-1:1]，-1表示最后一个位置。
