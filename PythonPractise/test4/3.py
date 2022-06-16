g_b = 3
g_l1 = [1, 2]
g_l2 = [1, 2, 3]


def t1(g_b, g_l1, g_l2):
    g_b = 2
    g_l1 = []
    g_l2.append(7)
    print(g_b, g_l1, g_l2)


t1(g_b, g_l1, g_l2)
print(g_b, g_l1, g_l2)
