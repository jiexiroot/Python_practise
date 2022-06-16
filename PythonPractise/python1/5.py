def jisuan(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x / y
    else:
        print("输入有误")
        return None


if __name__ == '__main__':
    print(jisuan(5, 2, '+'))
    print(jisuan(5, 2, '-'))
    print(jisuan(5, 2, '*'))
    print(jisuan(5, 2, '/'))
    print(jisuan(5, 2, 'a'))
