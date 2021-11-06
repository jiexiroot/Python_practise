# 1、定义一个类
class Person():
    # 初始化实例对象属性
    def __init__(self, name, age):
        # 赋予属性
        # self.实例化对象属性 = 参数
        self.name = name
        self.age = age


# 2、实例化对象并传入初始化属性值
p1 = Person('孙悟空', 500)
# 3、调用p1对象自身属性name和age
print(p1.name)
print(p1.age)
