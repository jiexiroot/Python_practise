# 计算三角形的面积
import math

# 输入三条边

a = float(input("请输入三角形的第一条边："))
b = float(input("请输入三角形的第二条边："))
c = float(input("请输入三角形的第三条边："))
# 计算面积

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# 输出结果

print(f"三角形的面积是：{area:f}")
