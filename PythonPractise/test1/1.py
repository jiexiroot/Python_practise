# 第一种：普通方式
print('*' * 100)
print(' 第一种：普通方式')
f = open('python2.txt', 'r', encoding='utf-8')
list1 = []
for i in f:
    name, sex, age, salary = i.split(' ')
    dict1 = {'name': name, 'sex': sex, 'age': age, 'salary': salary}
    list1.append(dict1)
print(list1)

# 求薪资
p = 0
for i in list1:
    p += int(i.get('salary'))
print(p)
# 求男人个数
for i in list1:
    if i.get('sex') == 'male':
        print(i.get('name'))

# 第二种：行列式
print('*' * 100)
print(' 第二种：行列式')
with open('python2.txt', 'r', encoding='utf-8') as i:
    list2 = [{'name': kk[0], 'sex': kk[1], 'age': kk[2], 'salary': kk[3]} for kk in [k.strip().split(' ') for k in i]]
    # 求薪水总和
    print('输出薪水总和：')
    p = sum(int(i.get('salary')) for i in list2)
    # 求男人姓名
    a = (i.get('name') for i in list2 if i.get('sex') == 'male')
    print('输出男人姓名：')
    for pp in a:
        print(pp)
    print(f'输出list：{list2}')
