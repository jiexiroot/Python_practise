# names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']
# first_index = names.index('eva')
# new_list = names[first_index+1:]
# second_index = new_list.index('eva')
# location = (first_index+second_index+1)
# names[location] = 'EVA'
# print(names)
# print(location)
mytup = ('a','b','c','d','e','f','g','h')

t_value = mytup[3]
print(t_value)

for key,value in enumerate(mytup, start=1):
    print(value,end=' ')
print()

tup1 = mytup[0:3]
print('tup1=',tup1)

tup2 = mytup[-1:-4:-1]
print('tup2=',tup2)

tup3 = tup1 + tup2
print('tup3=',tup3)

mylist = list(mytup)
print(mylist)

del mytup