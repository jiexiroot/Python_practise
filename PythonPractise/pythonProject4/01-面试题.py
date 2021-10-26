# 有一物，不知其数，三三数之余二，五五数之余三，七七数之余二，问物几何？
# for循环
for i in range(1, 101):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)
# while循环
j = 1
while j <= 100:
    if j % 3 == 2 and j % 5 == 3 and j % 7 == 2:
        print(j)
    j += 1

