# for i in range(1, 10):
#     for j in range(1, i+1):
#         # print(str(i) + "*" + str(j) + "=" +str( i * j), end= "   ")
#         # print(i, "*", j, "=", i*j, end="  ")
#         print(f'{i}*{j}={i*j}', end="  ")
#     print("")


i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}', end="  ")
        j += 1
    print('')
    i += 1
