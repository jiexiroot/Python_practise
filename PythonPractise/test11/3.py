# 全局
mydic = {'张三': ['男', 58], '李四': ['女', 78], '王五': ['女', 83]}


# 按照索引位置添加字典
# index = 转换成列表获得最后一个元素的键
def modify_dict(key, value, index=list(mydic.keys())[-1]):
    """
    使用列表存储键，使用dict存储值的方式
    """
    my_keys = [key for key in mydic.keys()]
    source_dict = mydic
    my_keys.insert(my_keys.index(index) + 1, key)
    source_dict[key] = value
    new_dict = {}
    for k in my_keys:
        new_dict.update({k: source_dict[k]})
    return new_dict


print(mydic)
mydic = modify_dict('胡六', ['男', 90], '张三')
print(mydic)

mydic = modify_dict('刘七', ['女', 100])
print(mydic)

del mydic['李四']
print(mydic)

# mydic2 = {'张三':['女',60]}
# mydic.update(mydic2)
mydic['张三']=['女',60]
print(mydic)

list1 = mydic.get('王五')
print(list1)

sum1 = 0
for key,value in mydic.items():
    sum1+=value[1]
print('全班总成绩：',sum1)

mylist1 = [key for key in mydic.keys()]
print('mylist1',mylist1)

mylist1 = []
for key in mydic.keys():
    mylist1.append(key)
print('mylist1',mylist1)

mylist2 = [values[1] for values in mydic.values()]
print('mylist2',mylist2)

mylist2 = []
for values in mydic.values():
    mylist2.append(values[1])
print('mylist2',mylist2)