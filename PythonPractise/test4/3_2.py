g_b = 3


def t1():
    global g_b  # 注释此段查看效果
    g_b = 2


t1()
print(g_b)
