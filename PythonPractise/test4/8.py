def div(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("除0错误！")
    except TypeError:
        print("类型错误！")
    except NameError:
        print("名字错误！")
    else:
        print("正确！")
    finally:
        print("执行finally语句块!")
        