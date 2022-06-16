# 局部变量应用示例
import math


def circle(r):
    print("circle函数内局部变量r=%.2f" % r)
    s = math.pi * r * r  # 求面积
    r = 8  # 修改函数内变量r的值
    print("修改后 ,circle函数内局部变量r=%.2f" % r)
    return s  # 返回所求的面积


r = float(input("请输入圆的半径："))
print("circle函数外全局变量r=%.2f" % r)
# 调用函数求圆的面积
area = circle(r)
print("circle函数调用后，全局变量r=%.2f" % r)
print("半径为%.2f的圆,面积是%.2f" % (r, area))
print("在函数外输出circle函数内变量r的值%.2f" % (s))