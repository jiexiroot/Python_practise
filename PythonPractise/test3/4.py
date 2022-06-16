
def jia(x, y):
    m = x + y
    return m


def jian(x, y):
    m = x - y
    print(m)


def chen(x, y):
    m = x * y
    print(m)


def chu(x, y):
    m = x / y
    print(m)


if __name__ == '__main__':
    X = int(input("请输入X的值："))
    Y = int(input("请输入Y的值："))
    n = input("请输入运算符：")
    if n == '+':
        print(jia(X, Y))
    elif n == '-':
        print(jian(X, Y))
    elif n == '*':
        print(chen(X, Y))
    elif n == '/':
        print(chu(X, Y))
