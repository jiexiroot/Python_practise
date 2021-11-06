class Girl():
    def __init__(self, name):
        self.name = name
        self.__age = 18

    # 公共方法：提供给外部的访问接口
    def get_age(self):
        return self.__age

    # 公共方法：提供给外部的设置接口
    def set_age(self, age):
        self.__age = age


xiaomei = Girl('小婷')
xiaomei.set_age(20)
print(xiaomei.get_age())
print(xiaomei.name)
